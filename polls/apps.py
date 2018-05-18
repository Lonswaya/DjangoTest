from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

import datetime

class PollsConfig(AppConfig):
    name = 'polls'
    def ready(self):
	    f=open("~/.debug","+w")
        f.write("Starting debug")
        def tick():
            #print("ticking")
            f= open("~/.debug","a")
            f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        scheduler = BackgroundScheduler()
        global job
        job = scheduler.add_job(tick, 'interval', seconds=15)
        scheduler.start()
	