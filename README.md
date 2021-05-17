A nano-framework for building Slack apps with SocketModeHandler in a way that allows hot code reload on every event.

The server is in slack-event-handler.py.

This file must be edited to add endpoints. The endpoints are just proxies to controller functions in controller.py.

slack_controller.py does the proxying and te hot reloading.
