from os import environ
from slack import WebClient

SLACK_TOKEN = environ["HOUSE_SLACK_KEY"]
client = WebClient(token=SLACK_TOKEN)

for message in client.chat_scheduledMessages_list()["scheduled_messages"]:
    print(message["id"])
    client.chat_deleteScheduledMessage(channel=message["channel_id"], scheduled_message_id=message["id"])
print("done")
