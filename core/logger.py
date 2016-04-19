
# -*- coding: utf-8 -*-

import inspect
import logging
import traceback


class Logger(object):

    @classmethod
    def __generate_trace(cls, msg):

        """
        Try to add some info about the origin of the given log text.
        :param msg: Text to log.
        """

        caller = inspect.getouterframes(inspect.currentframe(), 3)[2]
        caller_cls = caller[0].f_locals["self"].__class__.__name__ if "self" in caller[0].f_locals else "Unknown"
        caller_method = caller[3]
        return "%s.%s $ %s" % (caller_cls, caller_method, msg)

    @classmethod
    def debug(cls, msg, *args, **kwargs):

        """
        Log the given text as 'debug'.
        :param msg: Text to log.
        :param args: Arguments tuple.
        :param kwargs: Arguments dictionary.
        """

        try:
            logging.debug(cls.__generate_trace(msg), *args, **kwargs)
        except BaseException, e:
            logging.error(e)

    @classmethod
    def info(cls, msg, *args, **kwargs):

        """
        Log the given text as 'info'.
        :param msg: Text to log.
        :param args: Arguments tuple.
        :param kwargs: Arguments dictionary.
        """

        try:
            logging.info(cls.__generate_trace(msg), *args, **kwargs)
        except BaseException, e:
            logging.error(e)

    @classmethod
    def warning(cls, msg, *args, **kwargs):

        """
        Log the given text as 'warning'.
        :param msg: Text to log.
        :param args: Arguments tuple.
        :param kwargs: Arguments dictionary.
        """

        try:
            logging.warning(cls.__generate_trace(msg), *args, **kwargs)
        except BaseException, e:
            logging.error(e)

    @classmethod
    def error(cls, msg, *args, **kwargs):

        """
        Log the given text as 'error'.
        :param msg: Text to log.
        :param args: Arguments tuple.
        :param kwargs: Arguments dictionary.
        """

        try:
            trace = traceback.format_exc()
            if trace is not None:
                logging.error(trace)
            logging.error(cls.__generate_trace(msg), *args, **kwargs)
        except BaseException, e:
            logging.error(e)
