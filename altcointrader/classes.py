import time
import requests
import logging

from json import JSONDecodeError
from pprint import pprint, pformat

logging.basicConfig(level=logging.INFO)
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

        log.debug("Initializing...")
        self.update()

    def update(self):
        try:
            result = requests.get("https://www.altcointrader.co.za/api/v2/live-stats").json()

        except JSONDecodeError as e:
            result = None
            log.warning("JSONDecodeError: %s" % e)

        log.debug("\nresult: \n{}\n".format(pformat(result)))

        self.btc = result['BTC'] if result else None
        self.bcc = result['BCC'] if result else None
        self.dash = result['DASH'] if result else None
        self.eth = result['ETH'] if result else None
        self.ltc = result['LTC'] if result else None
        self.nmc = result['NMC'] if result else None
        self.xrp = result['XRP'] if result else None
        self.zec = result['ZEC'] if result else None

        return True

    def run(self):
        while True:
            self.update()
            time.sleep(1)

if __name__ == '__main__':
    altws = Channels()
    # altws.update()