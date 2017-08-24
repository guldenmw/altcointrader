import time
import requests
import logging

from json import JSONDecodeError
from pprint import pprint, pformat

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class Channels(object):
    def __init__(self):
        self.btc = None
        self.bcc = None
        self.dash = None
        self.eth = None
        self.ltc = None
        self.nmc = None
        self.xrp = None
        self.zec = None

        self.update()

    def update(self):
        try:
            result = requests.get("https://www.altcointrader.co.za/api/v2/live-stats").json()

        except JSONDecodeError as e:
            result = None
            log.warning("JSONDecodeError: %s" % e)

        self.btc = result['BTC'] if result else None
        self.bcc = result['BCC'] if result else None
        self.dash = result['DASH'] if result else None
        self.eth = result['ETH'] if result else None
        self.ltc = result['LTC'] if result else None
        self.nmc = result['NMC'] if result else None
        self.xrp = result['XRP'] if result else None
        self.zec = result['ZEC'] if result else None

        return True
