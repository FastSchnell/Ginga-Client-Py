# -*- coding: utf-8 -*-
import datetime
import time

from threading import Thread

from gcp import Client


def do(i):
    c = Client(token='test_token_1', host='0.0.0.0', port=1903, nonce="ssss")
    while 1:
        try:
            c.lock()
            print datetime.datetime.now(), i
            time.sleep(1)
        finally:
            c.unlock()


def main():
    for i in range(100):
        Thread(target=do, args=(i,)).start()

    time.sleep(10000000)


if __name__ == '__main__':
    main()
