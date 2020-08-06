#!/usr/bin/env python3
from setuptools import setup

setup(
    name='discord-webhooks',
    version='0.0.1',
    description='Simple library for sending logs to discord webhooks',
    url='https:/github.com/fumenoid/JHDBot/tree/webhook-logging/discord-webhooks',
    author='JHD dev team',
    author_email='johnhammond010@gmail.com',
    packages=['discord-webhooks'],
    install_requires=[
        'requests'
        ],
    classifiers=[],
)
