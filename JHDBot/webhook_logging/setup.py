#!/usr/bin/env python3
from setuptools import setup

setup(
    name='webhook_logging',
    version='0.0.4',
    description='Simple library for sending logs from python logging to webhooks',
    url='https:/github.com/fumenoid/JHDBot/tree/webhook_logging/webhook_logging',
    author='JHD dev team',
    author_email='johnhammond010@gmail.com',
    packages=['webhook_logging'],
    install_requires=[
        'requests',
        ],
    classifiers=[],
)
