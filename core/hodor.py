
# -*- coding: utf-8 -*-


class HodorQuote(object):

    HODOR_QUOTES = (
        "Hodor",
        "Hodor!",
        "Hodor?",
        "Hodor hodor, hodor?",
        "Hooodooor!!!",
        "Hodor hodor hodor, hodor hodor.",
        "Hodor, hodor?",
        "Hodor! Hodor! Hodor!",
        "Hodor...",
        "Hodor? Hodor..."
        "Hodor! Hodor..."
    )

    @classmethod
    def get_random_quote(cls):

        """
        Get a random Hodor quote.
        :return: The quote.
        """

        from random import randint

        return cls.HODOR_QUOTES[randint(0, len(cls.HODOR_QUOTES) - 1)]
