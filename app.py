
# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():

    """
    Handles the Hodor Bot website.
    :return: The HTML containing the website.
    """

    from flask import render_template
    from os import getenv

    return render_template(
        "index.html",
        fb_messenger_app_id=getenv("FB_MESSENGER_APP_ID", ""),
        fb_messenger_app_privacy_policy_url=getenv("FB_MESSENGER_APP_PRIVACY_POLICY_URL", "")
    )


@app.route("/webhook", methods=["POST", "GET"])
def webhook():

    """
    Handles the Facebook Messenger webhook requests.
    :return: The HTTP response according the action requested.
    """

    from core.facebook import FacebookMessengerBot
    from flask import request

    # Create a Facebook Messenger bot.
    bot = FacebookMessengerBot()

    # If the request method is GET.
    if request.method == "GET":

        # Retrieve the challenge code and the verification token from the request.
        challenge = request.args.get("hub.challenge")
        verify_token = request.args.get("hub.verify_token")

        # Try to verify the bot with the given info.
        response = bot.verify_bot(challenge, verify_token)

    # In the request method is POST.
    else:

        from core.hodor import HodorQuote

        # Iterate the received events and reply the messages.
        for event in request.json["entry"][0]["messaging"]:
            if "message" in event and "text" in event["message"] and event["message"]["text"] != "":

                # Post a random Hodor quote.
                bot.post_text_reply(
                    event["sender"]["id"],
                    HodorQuote.get_random_quote()
                )

        # The response.
        response = "", 200

    # Return the response.
    return response
