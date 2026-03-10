import json

api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

data = json.loads(api_response)

request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

if confidence_score < 0.9:
    print("Warning: Low confidence score")

follow_up = {
    "processed": True,
    "original_id": request_id,
    "message": "Result processed successfully"
}

json_output = json.dumps(follow_up, indent=4)

with open("response.json", "w") as file:
    file.write(json_output)
