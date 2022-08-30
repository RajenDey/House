import slack
import os

SLACK_TOKEN = os.environ["HOUSE_SLACK_KEY"]
client = slack.WebClient(token=SLACK_TOKEN)

for message in client.chat_scheduledMessages_list()["scheduled_messages"]:
    print(message["id"])
    client.chat_deleteScheduledMessage(channel=message["channel_id"], scheduled_message_id=message["id"])
print("done")