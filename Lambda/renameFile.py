import boto3
import json
from datetime import datetime
from boto3.dynamodb.conditions import Key

s3 = boto3.client('s3')
sns = boto3.client('sns')
db = boto3.resource('dynamodb')
table = db.Table("FilesTable")
permissions_table = db.Table("FilePermissions")
BUCKET = "mini-drive-storage-823405633682-us-east-1-an"
TOPIC_ARN = "arn:aws:sns:us-east-1:823405633682:MiniDriveNotifications"

def get_email_from_token(event):
    try:
        claims = event['requestContext']['authorizer']['jwt']['claims']
        return claims.get('email', 'Unknown')
    except:
        return 'Unknown'

def notify(email, subject, message):
    try:
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject=subject,
            Message=message,
            MessageAttributes={
                'email': {'DataType': 'String', 'StringValue': email}
            }
        )
    except Exception as e:
        print("SNS error:", e)

def lambda_handler(event, context):
    fileid = event['pathParameters']['id']
    body = json.loads(event['body'])
    new_name = body['newName']
    requester = get_email_from_token(event)
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    perm = permissions_table.get_item(Key={"fileId": fileid, "userEmail": requester})
    if 'Item' not in perm or perm['Item']['role'] not in ['owner', 'editor']:
        return {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "content-type,authorization",
                "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
            },
            "body": "Only owner or editor can rename files"
        }

    item = table.get_item(Key={"fileId": fileid})
    old_key = item['Item']['s3Key']
    old_name = item['Item']['fileName']
    new_key = "uploads/" + new_name

    s3.copy_object(Bucket=BUCKET, CopySource={'Bucket': BUCKET, 'Key': old_key}, Key=new_key)
    s3.delete_object(Bucket=BUCKET, Key=old_key)

    table.update_item(
        Key={"fileId": fileid},
        UpdateExpression="SET fileName = :fn, s3Key = :sk, lastModifiedBy = :mb, lastModifiedAt = :ma",
        ExpressionAttributeValues={
            ":fn": new_name,
            ":sk": new_key,
            ":mb": requester,
            ":ma": now
        }
    )

    all_perms = permissions_table.query(
        KeyConditionExpression=Key('fileId').eq(fileid)
    )
    for p in all_perms['Items']:
        notify(p['userEmail'], "File Diubah Nama - Mini Drive",
               f"File '{old_name}' telah diganti nama menjadi '{new_name}' oleh {requester}.")
               
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type,authorization",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
        },
        "body": "renamed"
    }
