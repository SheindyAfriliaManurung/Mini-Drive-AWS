import boto3
import json

db = boto3.resource('dynamodb')
table = db.Table("FilesTable")
permissions_table = db.Table("FilePermissions")

def get_email_from_token(event):
    try:
        claims = event['requestContext']['authorizer']['jwt']['claims']
        return claims.get('email', 'Unknown')
    except:
        return 'Unknown'

def lambda_handler(event, context):
    user_email = get_email_from_token(event)
    
    perms = permissions_table.query(
        IndexName='userEmail-index',
        KeyConditionExpression=boto3.dynamodb.conditions.Key('userEmail').eq(user_email)
    )

    file_ids = [p['fileId'] for p in perms['Items']]
    roles = {p['fileId']: p['role'] for p in perms['Items']}

    files = []
    for fid in file_ids:
        item = table.get_item(Key={"fileId": fid})
        if 'Item' in item:
            f = item['Item']
            f['myRole'] = roles[fid]
            files.append(f)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type,authorization",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS,PUT"
        },
        "body": json.dumps(files)
    }
