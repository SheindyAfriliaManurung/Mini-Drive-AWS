import boto3
import json

db = boto3.resource('dynamodb')
sns = boto3.client('sns')
permissions_table = db.Table("FilePermissions")
table = db.Table("FilesTable")
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
    target_email = body['email']
    role = body['role']
    requester = get_email_from_token(event)

    owner_check = permissions_table.get_item(
        Key={"fileId": fileid, "userEmail": requester}
    )
    if 'Item' not in owner_check or owner_check['Item']['role'] != 'owner':
        return {
            "statusCode": 403,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "content-type,authorization",
                "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
            },
            "body": json.dumps({"message": "Only owner can share files"})
        }

    permissions_table.put_item(Item={
        "fileId": fileid,
        "userEmail": target_email,
        "role": role
    })

    file_item = table.get_item(Key={"fileId": fileid})
    filename = file_item['Item']['fileName'] if 'Item' in file_item else fileid

    notify(target_email, "File Dibagikan - Mini Drive",
           f"File '{filename}' telah dibagikan kepada Anda oleh {requester} sebagai {role}.")

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type,authorization",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
        },
        "body": "shared"
    }
