import requests

# Set up a session to persist cookies across requests
session = requests.Session()

# Log in to the website using your OpenAI API key
api_key = "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"
response = session.post(
    "https://api.openai.com/v1/user/authenticate",
    json={"api_key": api_key}
)
if response.status_code != 200:
    print("Failed to authenticate with API key")
    exit()

# Start a new conversation and send a message
conversation_id = "org-AGs9Fb28TJcODadDQNOWZo5w"
response = session.post(
    f"https://api.openai.com/v1/conversations/{conversation_id}/messages",
    headers={"Content-Type": "application/json"},
    json={"text": "Hello, how are you?"}
)
if response.status_code == 200:
    print("Message sent successfully")
else:
    print("Failed to send message")
