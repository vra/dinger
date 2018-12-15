""" Module for scheduling different tasks using package apscheduler. """
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


class Dinger:
    def __init__(self, api_url, msg, start_date, trigger='cron', hour='0-23', minute='0-59', second='0-59'):
        self.api_url = api_url
        self.msg = msg

        self.sched = BlockingScheduler()

        job = self.create_job
        self.sched.add_job(func=job, start_date=start_date, trigger=trigger,
                           hour=hour, minute=minute, second=second)

    def create_job(self):
        requests.post(self.api_url, json=self.msg)

    def begin(self):
        requests.post(self.api_url, json=self.msg)
        self.sched.start()
