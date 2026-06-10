import boto3
import json

db = boto3.resource('dynamodb')
permissions_table = db.Table("FilePermissions")

def get_email_from_token(event):
    try:
        claims = event['requestContext']['authorizer']['jwt']['claims']
        return claims.get('email', 'Unknown')
    except:
        return 'Unknown'

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

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type,authorization",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
        },
        "body": "shared"
    }
