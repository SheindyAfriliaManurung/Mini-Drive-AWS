import json
import boto3
import uuid
import base64

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')
table = db.Table("FilesTable")
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

def lambda_handler(event, context):
    body = json.loads(event['body'])
    filename = body['fileName']
    fileid = str(uuid.uuid4())
    key = "uploads/" + filename
    ext = filename.split('.')[-1].lower()
    content_type = CONTENT_TYPES.get(ext, 'application/octet-stream')
    is_base64 = body.get('isBase64', False)

    if is_base64:
        content = base64.b64decode(body['content'])
    else:
        content = body['content'].encode('utf-8')

    s3.put_object(Bucket=BUCKET, Key=key, Body=content, ContentType=content_type)
    table.put_item(Item={
        "fileId": fileid,
        "fileName": filename,
        "s3Key": key
    })

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS"
        },
        "body": "uploaded"
    }
