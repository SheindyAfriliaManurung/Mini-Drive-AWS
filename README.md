# Mini Drive AWS

Mini Drive AWS is a web-based cloud storage application built entirely on Amazon Web Services (AWS). The application allows users to securely upload, store, view, rename, share, download, and delete files through a simple web interface.

The project demonstrates the integration of multiple AWS services to implement a scalable serverless architecture with authentication, authorization, file management, cloud storage, and real-time notification capabilities.

---

# Architecture Diagram
<img width="1535" height="286" alt="arsitektur" src="https://github.com/user-attachments/assets/c8f42fd6-5ad5-48ed-9084-7ace3f626f19" />

# AWS Services Used

## Amazon Cognito
Used for user authentication and JWT token generation.
<img width="926" height="434" alt="Amazon Cognito" src="https://github.com/user-attachments/assets/d14f3aee-f9ff-405e-bb59-1636c8a90a12" />

## Amazon API Gateway
Used to expose and secure REST API endpoints.
<img width="872" height="299" alt="API Gateway" src="https://github.com/user-attachments/assets/3fa9a1a7-1495-43cd-837a-4533470e6708" />

## AWS Lambda
Used as the serverless backend for business logic processing.
<img width="955" height="333" alt="Lambda" src="https://github.com/user-attachments/assets/f0433870-3adb-4d7b-97b6-2f76589bae13" />

## Amazon S3
Used for cloud file storage and static website hosting.
<img width="959" height="294" alt="Amazon S3" src="https://github.com/user-attachments/assets/8dcb2944-8f63-4585-8a8b-99eb88d87363" />

## Amazon DynamoDB
Used to store file metadata, ownership information, and permissions.
<img width="959" height="174" alt="DynamoDB" src="https://github.com/user-attachments/assets/38c32d12-fccc-4614-b5b6-144bb3a73ce8" />

## Amazon SNS
Used to send automatic email notifications to users when file activities occur, such as upload, delete, rename, and share.
<img width="945" height="173" alt="Amazon SNS" src="https://github.com/user-attachments/assets/36ea4a39-387c-4a87-a9a0-a3919fc4b57c" />

# Features

### Authentication & Security

- User authentication using Amazon Cognito
- JWT-based authorization
- Protected API endpoints
- User identity verification

### File Management

- Upload files
- View files
- Download files
- Rename files
- Delete files

### Sharing & Permissions

- Owner role
- Editor role
- Viewer role
- File ownership management
- Role-based access control

### Notifications
- Email notification on file upload
- Email notification on file delete
- Email notification on file rename
- Email notification on file share

# Application Screenshots

## Login Page
<img width="309" height="275" alt="login" src="https://github.com/user-attachments/assets/65d8bd5b-9de6-44ef-88a6-29b00f1a6dd0" />

## Dashboard
<img width="948" height="476" alt="dashboard" src="https://github.com/user-attachments/assets/6983ceb1-633a-47ae-a98a-fecf588aec94" />


## File Sharing
<img width="335" height="164" alt="share1" src="https://github.com/user-attachments/assets/5ee7e55f-f040-49b0-af52-de1455db5337" />

<img width="335" height="161" alt="share2" src="https://github.com/user-attachments/assets/50d2050f-e229-4a80-b46d-3abf826cc49f" />

## Notifications 
<img width="694" height="103" alt="Notifications" src="https://github.com/user-attachments/assets/7d929b2c-44a0-4b1a-9dda-3495e077a912" />

# Architecture Overview

User
 │
 ▼
Amazon Cognito
(Authentication)
 │
 ▼ JWT Token
Frontend (index.html hosted on S3)
 │
 ▼ API Request + JWT
API Gateway
 │
 ▼
AWS Lambda
 ├── Amazon S3          (File Storage & Static Website Hosting)
 ├── DynamoDB           (Metadata & Permissions: Owner, Editor, Viewer)
 └── Amazon SNS         (Email Notifications: Upload, Delete, Rename, Share)

# AWS Services

| Service | Purpose |
|----------|----------|
| Amazon Cognito | Authentication & Authorization |
| Amazon API Gateway | REST API Management |
| AWS Lambda | Serverless Backend |
| Amazon S3 | File Storage & Static Website Hosting |
| Amazon DynamoDB | Metadata & Permission Storage |
| Amazon SNS | Email Notifications |

---

# API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | /files | Get all files |
| POST | /upload | Upload file |
| GET | /file | View/Download file |
| PUT | /files/{id} | Rename file |
| DELETE | /files/{id} | Delete file |
| POST | /files/{id}/share | Share file |
| POST | /notifications/subscribe| Subscribe to notifications |

---

# Permission Model

## Owner

- View
- Download
- Rename
- Delete
- Share

## Editor

- View
- Download
- Rename

## Viewer

- View
- Download

---

# Learning Outcomes

This project demonstrates:

- Cloud-native application development
- Serverless architecture
- Authentication and authorization
- REST API implementation
- Cloud storage management
- Role-based access control
- Real-time email notifications
- Integration of multiple AWS services

---
