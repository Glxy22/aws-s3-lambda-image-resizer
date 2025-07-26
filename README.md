**# aws-s3-lambda-image-resizer**
This project implements a serverless image resizing pipeline using **AWS Lambda**, **S3**, and **Python**.

## ✅ Project Overview
- Uploading an image to **S3 Bucket A** triggers a Lambda function.
- The Lambda function:
  - Downloads the image
  - Resizes it using **Pillow**
  - Uploads the resized image to **S3 Bucket B**
- Fully implemented and tested using **AWS Cloud resources only** 

## 🧰 Technologies Used

- AWS Lambda (Python 3.12)
- AWS S3
- Lambda Layer for Pillow (built on Amazon Linux 2023)
- Python + Pillow
- IAM (Lambda execution role with S3 access)
  
**Highlights**
100% cloud-native workflow
Solves common Lambda packaging issue with Pillow (_imaging import error)
Demonstrates AWS automation, event-driven design, and real use of IAM/S3/Lambda

**🧪 Test Results**
Uploaded test.jpg to Bucket A
✔️ Resized image resized-test.jpg appeared in Bucket B


