import boto3
import json

db = boto3.resource('dynamodb')
table = db.Table("FilesTable")

def lambda_handler(event, context):
    data = table.scan()
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS"
        },
        "body": json.dumps(data['Items'])
    }
