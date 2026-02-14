import json
import boto3

def lambda_handler(event, context):
    # This is the main Lambda function entry point.
    # 'event' contains request data from API Gateway.
    # 'context' contains runtime information about the Lambda execution.

    # Create a connection to DynamoDB service in the specified AWS region (Ohio - us-east-2)
    # boto3 is the AWS SDK used to interact with AWS services
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

    # Connect to the DynamoDB table named 'studentData'
    # This table stores all student records
    table = dynamodb.Table('studentData')

    # Perform a scan operation to retrieve all records from the table
    # Scan reads every item in the table (used here to fetch all students)
    response = table.scan()

    # Extract the actual list of student items from the response
    data = response['Items']

    # DynamoDB scan may not return all records at once if the dataset is large.
    # If 'LastEvaluatedKey' exists, it means more records are available.
    # Continue scanning until all records are retrieved.
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])  # Add newly fetched records to the existing list

    # Return the complete list of student records back to API Gateway
    # This data will then be sent to the frontend application
    return data
