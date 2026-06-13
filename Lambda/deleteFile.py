import boto3
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
    requester = get_email_from_token(event)

    perm = permissions_table.get_item(Key={"fileId": fileid, "userEmail": requester})
    if 'Item' not in perm or perm['Item']['role'] != 'owner':
        return {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "content-type,authorization",
                "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
            },
            "body": "Only owner can delete files"
        }

    item = table.get_item(Key={"fileId": fileid})
    key = item['Item']['s3Key']
    filename = item['Item']['fileName']

    s3.delete_object(Bucket=BUCKET, Key=key)
    table.delete_item(Key={"fileId": fileid})

    all_perms = permissions_table.query(
        KeyConditionExpression=Key('fileId').eq(fileid)
    )
    for p in all_perms['Items']:
        notify(p['userEmail'], "File Dihapus - Mini Drive",
               f"File '{filename}' telah dihapus oleh {requester}.")
        permissions_table.delete_item(Key={"fileId": fileid, "userEmail": p['userEmail']})
        
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type,authorization",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
        },
        "body": "deleted"
    }
