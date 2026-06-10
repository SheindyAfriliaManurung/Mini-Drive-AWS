# Mini Drive AWS

Mini Drive AWS is a web-based cloud storage application built entirely on Amazon Web Services (AWS). The application allows users to securely upload, store, view, rename, share, download, and delete files through a simple web interface.

The project demonstrates the integration of multiple AWS services to implement a scalable serverless architecture with authentication, authorization, file management, and cloud storage capabilities.

---

# Architecture Diagram
<img width="487" height="735" alt="architecture-diagram" src="https://github.com/user-attachments/assets/2728f302-cb68-4c4f-b924-ec72de730c0f" />

# AWS Services Used

## Amazon Cognito

Used for user authentication and JWT token generation.
<img width="926" height="434" alt="Amazon Cognito" src="https://github.com/user-attachments/assets/e2926092-3e4a-4ab0-a547-b98f9536e508" />

## Amazon API Gateway

Used to expose and secure REST API endpoints.
<img width="952" height="302" alt="API Gateway" src="https://github.com/user-attachments/assets/c806712f-28cb-4d5d-a642-06c4ecafa80b" />


## AWS Lambda

Used as the serverless backend for business logic processing.
<img width="959" height="347" alt="Lambda" src="https://github.com/user-attachments/assets/a847d0f0-b6ea-488b-bde8-fe4cbae28710" />


## Amazon S3

Used for cloud file storage.
<img width="959" height="294" alt="Amazon S3" src="https://github.com/user-attachments/assets/8dcb2944-8f63-4585-8a8b-99eb88d87363" />

## Amazon DynamoDB

Used to store file metadata, ownership information, and permissions.
<img width="959" height="174" alt="DynamoDB" src="https://github.com/user-attachments/assets/38c32d12-fccc-4614-b5b6-144bb3a73ce8" />


## Amazon CloudWatch

Used for monitoring and logging.
<img width="773" height="406" alt="CloudWatch" src="https://github.com/user-attachments/assets/906a6936-13df-4ed1-b43d-c1700877b2ae" />

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

---

# Application Screenshots

## Login Page
<img width="309" height="275" alt="login" src="https://github.com/user-attachments/assets/65d8bd5b-9de6-44ef-88a6-29b00f1a6dd0" />

## Dashboard
<img width="948" height="476" alt="dashboard" src="https://github.com/user-attachments/assets/6983ceb1-633a-47ae-a98a-fecf588aec94" />


## File Sharing
<img width="335" height="164" alt="share1" src="https://github.com/user-attachments/assets/5ee7e55f-f040-49b0-af52-de1455db5337" />

<img width="335" height="161" alt="share2" src="https://github.com/user-attachments/assets/50d2050f-e229-4a80-b46d-3abf826cc49f" />

# Architecture Overview

```text
User
 │
 ▼
Amazon Cognito
(Authentication)
 │
 ▼ JWT Token
Frontend (index.html)
 │
 ▼
API Gateway
 │
 ▼
AWS Lambda
 ├── Amazon S3 (File Storage)
 ├── DynamoDB (Metadata & Permissions)
 └── CloudWatch (Logs & Monitoring)
```

---

# AWS Services

| Service | Purpose |
|----------|----------|
| Amazon Cognito | Authentication & Authorization |
| Amazon API Gateway | REST API Management |
| AWS Lambda | Serverless Backend |
| Amazon S3 | File Storage |
| Amazon DynamoDB | Metadata Storage |
| Amazon CloudWatch | Monitoring & Logging |

---

# API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | /files | Get all files |
| POST | /files | Upload file |
| GET | /file | Download file |
| PUT | /files/{id} | Rename file |
| DELETE | /files/{id} | Delete file |
| POST | /files/{id}/share | Share file |

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
- Monitoring and observability
- Integration of multiple AWS services

---
