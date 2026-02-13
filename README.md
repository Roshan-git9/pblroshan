📚 Serverless Student Management System

A fully serverless web application built on AWS that allows users to perform CRUD (Create, Read, Update, Delete) operations on student records.

This project demonstrates how to design and deploy a scalable cloud-native application without managing any servers.

🚀 Project Overview

The Student Management System enables users to:

Add new student records

View all students

Update student information

Delete student entries

The entire backend is built using AWS serverless services, ensuring scalability, reliability, and cost efficiency.

🏗 Architecture

The application follows a serverless architecture:

User (Browser)
→ Static Website hosted on Amazon S3
→ REST API exposed through Amazon API Gateway
→ Business logic handled by AWS Lambda
→ Data stored in Amazon DynamoDB

This architecture eliminates the need for traditional server infrastructure.

🛠 AWS Services Used
1. Amazon S3

Hosts the static frontend (HTML, CSS, JavaScript)

Configured for static website hosting

CORS enabled for API communication

2. Amazon API Gateway (REST API)

Creates HTTP endpoints for frontend interaction

Handles GET, POST, PUT, DELETE methods

CORS configured to allow browser-based requests

3. AWS Lambda

Executes backend logic

Processes API requests

Performs database operations

Logs execution details to CloudWatch

4. Amazon DynamoDB

NoSQL database storing student records

Uses a partition key for uniquely identifying each student

Designed for high performance and scalability

5. IAM (Identity and Access Management)

Manages secure permissions between services

Lambda execution role configured with required access policies

6. Amazon CloudWatch

Used for monitoring logs and debugging

🔐 Security & Permissions

IAM roles ensure secure interaction between Lambda and DynamoDB

Only necessary permissions are granted to backend services

API endpoints are deployed in controlled stages

🌍 CORS Configuration

To enable communication between the S3-hosted frontend and API Gateway:

CORS enabled on API Gateway methods

Gateway responses configured for 4XX and 5XX errors

S3 bucket configured to allow cross-origin requests

This ensures smooth browser-based communication without cross-origin errors.

📦 Deployment Workflow

Create DynamoDB table

Create Lambda function

Configure IAM execution role

Create REST API in API Gateway

Integrate API methods with Lambda

Enable CORS

Deploy API to stage

Update API endpoint in frontend

Upload frontend files to S3

Enable static website hosting

📊 Key Learning Outcomes

Understanding serverless architecture

Implementing REST APIs using API Gateway

Managing IAM roles and permissions

Debugging CORS issues

Handling region-specific AWS services

Monitoring with CloudWatch

💡 Why Serverless Architecture?

No server management

Automatic scaling

High availability

Pay-per-use pricing

Faster deployment

🔮 Future Enhancements

User authentication with Amazon Cognito

Input validation and error handling improvements

Pagination for large datasets

Infrastructure as Code (Terraform or CloudFormation)

CI/CD pipeline integration

🎯 Conclusion

This project demonstrates how to build a complete full-stack cloud application using AWS serverless services. It highlights modern cloud development practices, scalable architecture design, and secure service integration.
