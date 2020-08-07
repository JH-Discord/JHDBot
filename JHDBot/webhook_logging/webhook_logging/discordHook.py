#!/usr/bin/env python3
import logging
import requests
import json

class DiscordHandler(logging.Handler):
    '''
    Class for sending logging records to discord webhooks.
    '''
    def __init__(self, url: str) -> None:
        """
        Override the constructor because all of those stupid parameters aren't needed.
        """
        logging.Handler.__init__(self)

        self.url = url
        self.__testConnection(url)

    def __testConnection(self, url: str) -> None:
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception(f"Could not establish connection for webhook logging. URL returned a {r.status_code}")
        return

    def mapLogRecord(self, record):
        return self.format(record)

    def emit(self, record) -> None:
        """
        Emit a record.

        Send the record to the Web server as a percent-encoded dictionary
        """
        try:
            url = self.url
            logMsg = self.mapLogRecord(record)
            data = json.dumps({"content": str(logMsg)})
            headers = {"content-type": "application/json"}
            r = requests.post(url, headers=headers, data=data)
        except Exception:
            self.handleError(record)
