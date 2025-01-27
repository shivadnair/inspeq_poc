import boto3
import json

def initialize_bedrock_client(region="ap-south-1"):
    try:
        client = boto3.client('bedrock-runtime', region_name=region)
        print("Bedrock client initialized successfully")
        return client
    except Exception as e:
        print(f"Error initializing Bedrock client: {e}")
        return None
    
def generate_resp(client, prompt):
    try:
        payload = {
            "inputText": prompt
        }
        response = client.invoke_model_with_response_stream(
            modelId="amazon.titan-text-lite-v1",
            accept="application/json",
            contentType="application/json",
            body=json.dumps(payload)
        )
        
         # Process the response stream
        result = ""
        for event in response["body"]:
            chunk = event.get("chunk")
            if chunk:
                # Decode the 'bytes' field and parse as JSON
                chunk_data = json.loads(chunk["bytes"].decode("utf-8"))
                if "outputText" in chunk_data:
                    result += chunk_data["outputText"]

        return result
    
    except Exception as e:
        print(f"Error generating response: {e}")
        return None
