import boto3

def lambda_handler(event, context):
    s3_event = event['Records'][0]['s3']
    source_bucket = s3_event['bucket']['name']
    key = s3_event['object']['key']

    s3_client = boto3.client('s3')

    try:
        response = s3_client.copy_object(
            Bucket='s3-finish',
            Key=key,
            CopySource={'Bucket': source_bucket, 'Key': key}
        )
        print("Object copied successfully:", response)
        return {
            'statusCode': 200,
            'body': 'File copied successfully!'
        }
    except Exception as e:
        print("Error copying object:", e)
        return {
            'statusCode': 500,
            'body': 'Error copying file!'
        }
