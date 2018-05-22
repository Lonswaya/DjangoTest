from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

import datetime

class PollsConfig(AppConfig):
    name = 'polls'
    def ready(self):
        #f=open("C:\\inetpub\\wwwroot\\mysite\\.debug","w+")
        #f.write("Starting debug\n")
        #def tick():
            #print("ticking")
            #f= open("C:\\inetpub\\wwwroot\\mysite\\.debug","a")
            #f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        scheduler = BackgroundScheduler()
        global job
        #job = scheduler.add_job(tick, 'interval', seconds=15)
        scheduler.start()
	