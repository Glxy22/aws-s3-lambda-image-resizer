import boto3
from PIL import Image
import os
import io

s3 = boto3.client('s3')

# Target bucket name
DEST_BUCKET = 'image-resized-23987794'  # Replace with your Bucket B name

def lambda_handler(event, context):
    try:
        # Extract bucket and object key from the event
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Download image from S3
        response = s3.get_object(Bucket=source_bucket, Key=object_key)
        image_data = response['Body'].read()

        # Resize image using Pillow
        image = Image.open(io.BytesIO(image_data))
        resized_image = image.resize((300, 300))  # Resize to 300x300

        # Save resized image to memory
        buffer = io.BytesIO()
        resized_image_format = image.format if image.format else 'JPEG'
        resized_image.save(buffer, format=resized_image_format)
        buffer.seek(0)

        # Define new object key
        new_key = f"resized-{object_key}"

        # Upload resized image to destination bucket
        s3.put_object(
            Bucket=DEST_BUCKET,
            Key=new_key,
            Body=buffer,
            ContentType=response['ContentType']
        )

        return {
            'statusCode': 200,
            'body': f"Image resized and uploaded to {DEST_BUCKET}/{new_key}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error processing image: {str(e)}"
        }
