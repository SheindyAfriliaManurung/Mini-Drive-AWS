import boto3

s3 = boto3.client('s3')
BUCKET = "mini-drive-storage-823405633682-us-east-1-an"

def lambda_handler(event, context):
    key = event['queryStringParameters']['key']
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET, 'Key': key},
        ExpiresIn=300
    )
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS"
        },
        "body": url
    }
