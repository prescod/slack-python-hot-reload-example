import os

# Use the package we installed
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from slack_controller import SlackController

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

controller = SlackController("controller.py", app)


@app.event("message")
def handle_message_events(body, logger, ack):
    ack()
    controller.handle_message_events(vars())


@app.middleware  # or app.use(log_request)
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    controller.update_home_tab(vars())


@app.command("/foo")
def respond(ack, say, command, client):
    ack()
    controller.foo(vars())


@app.action("actionId-0")
def handle_some_action(ack, body, say):
    ack()
    controller.handle_some_action(vars())


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
