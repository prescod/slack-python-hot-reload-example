import os, re

# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


@app.command("/foo")
def respond(ack, say, command):
    ack(
        blocks=[
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Step 1",
                            "emoji": True,
                        },
                        "value": "click_me_123",
                        "action_id": "actionId-0",
                    }
                ],
            }
        ],
        text="ABCDE",
    )


@app.action("actionId-0")
def handle_some_action(ack, body, logger, say):
    ack()
    say(
        blocks=[
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Step 2",
                            "emoji": True,
                        },
                        "value": "click_me_123",
                        "action_id": "actionId-0",
                    }
                ],
            }
        ],
        text="ABCDE",
    )

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
