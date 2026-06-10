import json
import boto3
import uuid
import base64
from datetime import datetime

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')
table = db.Table("FilesTable")
permissions_table = db.Table("FilePermissions")
BUCKET = "mini-drive-storage-823405633682-us-east-1-an"

CONTENT_TYPES = {
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'html': 'text/html',
    'csv': 'text/csv'
}

def get_email_from_token(event):
    try:
        claims = event['requestContext']['authorizer']['jwt']['claims']
        return claims.get('email', 'Unknown')
    except:
        return 'Unknown'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    filename = body['fileName']
    fileid = str(uuid.uuid4())
    key = "uploads/" + filename
    ext = filename.split('.')[-1].lower()
    content_type = CONTENT_TYPES.get(ext, 'application/octet-stream')
    is_base64 = body.get('isBase64', False)
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    uploaded_by = get_email_from_token(event)

    if is_base64:
        content = base64.b64decode(body['content'])
    else:
        content = body['content'].encode('utf-8')

    s3.put_object(Bucket=BUCKET, Key=key, Body=content, ContentType=content_type)

    table.put_item(Item={
        "fileId": fileid,
        "fileName": filename,
        "s3Key": key,
        "uploadedBy": uploaded_by,
        "uploadedAt": now,
        "lastModifiedBy": uploaded_by,
        "lastModifiedAt": now
    })

    permissions_table.put_item(Item={
        "fileId": fileid,
        "userEmail": uploaded_by,
        "role": "owner"
    })

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type,authorization",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
        },
        "body": "uploaded"
    }
