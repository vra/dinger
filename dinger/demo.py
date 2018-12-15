""" some complete pipeline demos. """
import os
import time

from dinger import Dinger
from jobs import say_hello_world
from utils import get_webhook

code_path = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.join(code_path, '..')
webhook_path = os.path.join(project_root, 'webhook.txt')

ding_url = get_webhook(webhook_path)
msg = say_hello_world()

dinger = Dinger(ding_url, msg, '2018-12-04 08:31:00', second='0-1')
dinger.begin()
