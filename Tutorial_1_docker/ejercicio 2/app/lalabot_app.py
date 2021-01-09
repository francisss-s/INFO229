import os
from slack import WebClient
import slack
from lalabot import LalaBot

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Create a new lalaBot
lala_bot = LalaBot("#varios")

# Get the onboarding message payload
message = lala_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)