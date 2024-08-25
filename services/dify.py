import requests

# Class to handle Dify Request for Response
class Dify:
  def __init__(self, api_key):
    # Define the Key for Dify API
    self.api_key = api_key
    self.baseUrl = "https://api.dify.ai/v1"
    self.headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
  }

  def sendMessage(self, message):
    # Define the URL for Dify API
    url = f"{self.baseUrl}/chat-messages"
    # Define the data to be sent to Dify API
    data = {
        "inputs": {},
        "query": message,
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "abc-123",
        "files": []
    }
    # Send the data to Dify API
    response = requests.post(url, headers=self.headers, json=data)

    return response.json()