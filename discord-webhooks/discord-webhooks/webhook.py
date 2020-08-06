#!/usr/bin/env python3
import requests

class WebhookLogger:
    '''
    Class to create logging objects using a webhook url.
    '''
    def __init__(self, url: str):
        '''
        Create a new webhook logger with the specified url.
        
            Parameters:
                url (str): URL of the discord webhook
        '''
        self.url = url
        self.__testConnection(url)

    def __testConnection(self, url: str):
        '''
        Test the connection to the discord api

            Parameters:
                url (str): URL of the discord webhook
        '''
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception(f"Error setting up webhook logger. Spcified URL returned a {r.status_code}.")
        return



if __name__ == '__main__':
    log = WebhookLogger('')
