import logging
import os

import backoff
import requests

logging.getLogger('backoff').addHandler(logging.StreamHandler())


def backoff_hdlr(details):
    print("Backing off {wait:0.1f} seconds after {tries} tries "
          "calling function {target} with args {args} and kwargs "
          "{kwargs}".format(**details))


def backoff_hdlr1(details):
    print("Backing off 1 -> {wait:0.1f} seconds after {tries} tries "
          "calling function {target} with args {args} and kwargs "
          "{kwargs}".format(**details))


def giveup_hdlr(details):
    print("Give up seconds after {tries} tries "
          "calling function {target} with args {args} and kwargs "
          "{kwargs}".format(**details))


def success_hdlr(details):
    print("Success up  seconds after {tries} tries "
          "calling function {target} with args {args} and kwargs "
          "{kwargs}".format(**details))


def is_non_retriable_error(par):
    return False


@backoff.on_exception(backoff.expo,
                      ConnectionResetError, giveup=is_non_retriable_error, max_tries=2, on_giveup=giveup_hdlr,
                      on_success=success_hdlr,
                      on_backoff=[backoff_hdlr, backoff_hdlr1], max_time=1)
def get_url():
    raise ConnectionResetError
    a = requests.get("https://google1.com")
    print(a.headers)


if __name__ == "__main__":
    get_url()
