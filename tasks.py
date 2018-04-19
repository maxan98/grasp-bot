import time
import threading
from threading import Timer,Thread,Event
from litedb import *
import vkapi
from settings import token

def gettime():
    hour,mine = (time.localtime(time.time())[3],time.localtime(time.time())[4])
    return (hour,mine)


class TaskThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        self.jobs = {}
        self.keys = []

    def run(self):
        while not self.stopped.wait(60.0):
            print('Timer is running ')
            db = Database()
            answer = db.execread("SELECT vkid, pending FROM users WHERE pending <> 'NULL' ")
            db.close()
            if len(answer)>0:
                self.jobs = dict(answer)
                self.keys = self.jobs.keys()
                print(self.jobs)
            for i in self.keys:
                hour = self.jobs[i][12:14]
                mine = self.jobs[i][15:17]
                messa = self.jobs[i][18:]
                x, y = gettime()
                print(hour,mine,messa,x,y)
                if x == hour and y == mine:
                    vkapi.send_message(i, token, messa, '')
                    self.jobs.pop(i)
                    print('Напомнили', i,messa)











def main():
    stopFlag = Event()
    thread = TaskThread(stopFlag)
    thread.start()



if __name__ == '__main__':
    main()
