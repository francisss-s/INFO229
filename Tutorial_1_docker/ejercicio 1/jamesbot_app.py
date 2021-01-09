import os
from slack import WebClient
from jamesbot import JamesBot

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Create a new lalaBot
james_bot = JamesBot("#varios")

# Get the onboarding message payload
message = james_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)