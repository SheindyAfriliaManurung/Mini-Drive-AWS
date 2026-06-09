import boto3

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')
table = db.Table("FilesTable")
BUCKET = "mini-drive-storage-823405633682-us-east-1-an"

def lambda_handler(event, context):
    fileid = event['pathParameters']['id']
    item = table.get_item(Key={"fileId": fileid})
    key = item['Item']['s3Key']
    s3.delete_object(Bucket=BUCKET, Key=key)
    table.delete_item(Key={"fileId": fileid})
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS"
        },
        "body": "deleted"
    }
