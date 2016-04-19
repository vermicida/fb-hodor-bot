
# -*- coding: utf-8 -*-


class FacebookMessengerBot(object):

    def __init__(self):

        """
        Class constructor.
        :return: An instance of this class.
        """

        from os import getenv

        super(FacebookMessengerBot, self).__init__()

        # Set the Facebook Messenger API URL.
        self._fb_messenger_api_url = "%s?access_token=%s" % (
            getenv("FB_MESSENGER_API_URL", ""),
            getenv("FB_PAGE_ACCESS_TOKEN", "")
        )

        # Set the Facebook Messenger verification token.
        self._fb_messenger_verify_token = getenv("FB_MESSENGER_VERIFY_TOKEN", "")

    def _post_message(self, message):

        """
        Send the given message to the Facebook Messenger platform.
        :param message: The message to post.
        :return: The Facebook Messenger response.
        """

        from core.logger import Logger
        from google.appengine.api import urlfetch
        from json import dumps

        try:
            # Post the message to the Facebook Messenger platform.
            r = urlfetch.fetch(
                url=self._fb_messenger_api_url,
                method=urlfetch.POST,
                headers={"Content-Type": "application/json"},
                payload=dumps(message)
            )

            # Parse the response.
            response = r.content if r.status_code == 200 else None
            Logger.info("Facebook response:\n%s" % response)

        # In case of error.
        except BaseException as e:
            Logger.error(e)
            response = None

        # Return the parsed response.
        return response

    def verify_bot(self, challenge, verify_token):

        """
        Verify this bot for the given Facebook App challenge and verification token.
        :param challenge: The challenge code.
        :param verify_token: The verification token.
        :return: The given challenge if the verification was successful.
        """

        return challenge if self._fb_messenger_verify_token == verify_token else "The verify token is not valid."

    def post_text_reply(self, sender_id, text):

        """
        Post a reply message to the given user.
        :param sender_id: The user identifier.
        :param text: The message to send.
        :return: The Facebook Messenger response.
        """

        # The request body.
        data = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": text
            }
        }

        # Sends the message to the user.
        self._post_message(data)
