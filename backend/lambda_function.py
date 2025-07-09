import json
import boto3
import uuid
from datetime import datetime

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Amazon')  # Your DynamoDB table

def lambda_handler(event, context):
    try:
        if not event.get('body'):
            return response(400, {"message": "Missing request body"})

        body = json.loads(event['body'])
        phone_number = body.get('phone_number')
        status = body.get('status')

        if not phone_number or not status:
            return response(400, {"message": "Missing phone_number or status"})

        message = f"Your order status: {status}"

        sns.publish(
            PhoneNumber=phone_number,
            Message=message
        )

        # Log to DynamoDB
        log_entry = {
            'id': str(uuid.uuid4()),
            'phone_number': phone_number,
            'status': status,
            'timestamp': datetime.utcnow().isoformat()
        }

        table.put_item(Item=log_entry)

        return response(200, {"message": "SMS sent and logged to DB"})

    except Exception as e:
        return response(500, {"message": f"Error: {str(e)}"})

def response(code, body):
    return {
        'statusCode': code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }
