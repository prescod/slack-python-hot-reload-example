from time import sleep
from threading import Thread


def handle_some_action(context, ack, body, say):
    app = context["app"]
    data = app.client.chat_postMessage(text="XYZZY", channel="testing")
    ts = data["ts"]
    app.client.chat_postMessage(text="Nothing happens", channel="testing", thread_ts=ts)
    say(tuple(body["state"]["values"].values())[0]['plain_text_input-action']["value"][::-1])

    def later():
        for i in range(20):
            sleep(60)
            app.client.chat_postMessage(text=f"{i} minutes passed", channel="testing", thread_ts=ts)

    t = Thread(target=later)
    t.start()


def foo(context, ack, say, command, client):
    ack(
        blocks=[
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action",
                    "initial_value": command["text"],
                },
                "label": {"type": "plain_text", "text": "Recipe", "emoji": True},
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Generate",
                            "emoji": True,
                        },
                        "value": "click_me_123",
                        "action_id": "actionId-0",
                    }
                ],
            },
        ],
        text="ABCDEFG",
    )


def handle_message_events(context, body, logger, ack):
    print("XXXX")


def update_home_tab(client, event, logger):
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        client.views_publish(
            # the user that opened your app's app home
            user_id=event["user"],
            # the view object that appears in the app home
            view={
                "type": "home",
                "callback_id": "home_view",
                # body of the view
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Welcome to your _App's Home_* :tada:",
                        },
                    },
                    {"type": "divider"},
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app.",
                        },
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {"type": "plain_text", "text": "Click me!"},
                                "action_id": "home_button_click",
                            }
                        ],
                    },
                ],
            },
        )
        print("Opened home page")

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
