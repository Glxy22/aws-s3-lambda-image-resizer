# aws-s3-lambda-image-resizer
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

## 🗂️ Project Structure
