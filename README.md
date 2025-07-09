<<<<<<< HEAD
# order-status-sms-notifier
=======
# 📦 Order Status SMS Notifier (AWS + HTML)

This project sends SMS updates to customers when their order status changes and logs them to DynamoDB.

## ✅ Technologies Used

- AWS Lambda (Python)
- Amazon SNS (for SMS)
- DynamoDB (`Amazon` table with `id` as partition key)
- API Gateway (POST /order/update)
- S3 Static Hosting (or GitHub Pages for frontend)

## 🚀 How It Works

1. User enters their phone number and order status on a web page.
2. The form sends a POST request to an API Gateway endpoint.
3. API Gateway triggers a Lambda function:
   - Sends an SMS via SNS
   - Logs the data into DynamoDB

## 📁 Folder Structure


## ⚙️ To Deploy

### Frontend

- Upload `frontend/index.html` to:
  - GitHub Pages, OR
  - S3 Static Website Hosting (public-read or CloudFront)

### Backend

1. Deploy `lambda_function.py` to a new AWS Lambda function
2. Add IAM permissions:
   - `sns:Publish`
   - `dynamodb:PutItem`
3. Create API Gateway with:
   - POST method
   - Lambda Proxy Integration
   - Enable CORS (POST and OPTIONS)
4. Deploy API to a stage (`prod`)

### DynamoDB Table

- Table Name: `Amazon`
- Partition Key: `id` (String)

## 📝 Example DynamoDB Record

```json
{
  "id": "b01e3-9ff1-443c-a11c-1d032",
  "phone_number": "+919533723709",
  "status": "Order Shipped",
  "timestamp": "2025-07-09T06:30:00.000Z"
}

---

>>>>>>> 5f950e3 (first commit)
