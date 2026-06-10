# Mini Drive AWS

Mini Drive AWS is a web-based cloud storage application built entirely on Amazon Web Services (AWS). The application allows users to securely upload, store, view, rename, share, download, and delete files through a simple web interface.

The project demonstrates the integration of multiple AWS services to implement a scalable serverless architecture with authentication, authorization, file management, and cloud storage capabilities.

---

# Architecture Diagram

<p align="center">
  <img src="architecture-diagram.png" width="600">
</p>

---

# AWS Services Used

## Amazon Cognito

Used for user authentication and JWT token generation.

<p align="center">
  <img src="Amazon Cognito.png" width="800">
</p>

---

## Amazon API Gateway

Used to expose and secure REST API endpoints.

<p align="center">
  <img src="API Gateway.png" width="800">
</p>

---

## AWS Lambda

Used as the serverless backend for business logic processing.

<p align="center">
  <img src="Lambda.png" width="800">
</p>

---

## Amazon S3

Used for cloud file storage.

<p align="center">
  <img src="Amazon S3.png" width="800">
</p>

---

## Amazon DynamoDB

Used to store file metadata, ownership information, and permissions.

<p align="center">
  <img src="DynamoDB.png" width="800">
</p>

---

## Amazon CloudWatch

Used for monitoring and logging.

<p align="center">
  <img src="CloudWatch.png" width="800">
</p>

---

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

<p align="center">
  <img src="login.png" width="800">
</p>

---

## Dashboard

<p align="center">
  <img src="dashboard.png" width="800">
</p>

---

## File Sharing

### Share Example 1

<p align="center">
  <img src="share1.png" width="800">
</p>

### Share Example 2

<p align="center">
  <img src="share2.png" width="800">
</p>

---

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
