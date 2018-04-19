import time
import threading
from threading import Timer,Thread,Event
from litedb import *
import vkapi
from settings import token

def gettime():
    hour,mine = (time.localtime(time.time())[3],time.localtime(time.time())[4])
    return (str(hour),str(mine))


class TaskThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        self.jobs = {}
        self.keys = []
        self.todelkeys = []

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
                if len(hour) == 1:
                    hour = '0'+hour
                mine = self.jobs[i][15:17]
                if len(mine) == 1:
                    mine = '0'+mine
                messa = self.jobs[i][18:]
                x, y = gettime()
                if len(x) == 1:
                    x = '0'+x

                if len(y) == 1:
                    y = '0'+y
                print(hour,mine,messa,x,y)
                if x == hour and y == mine:
                    vkapi.send_message('!!!НАПОМИНАНИЕ!!!\n'+i, token, messa, '')
                    self.todelkeys.append(i)
                    print('Напомнили', i,messa)
            for i in self.todelkeys:
                self.jobs.pop(i)
            todelkeys.clear()











def main():
    stopFlag = Event()
    thread = TaskThread(stopFlag)
    thread.start()



if __name__ == '__main__':
    main()
