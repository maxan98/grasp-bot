#!/usr/bin/env python3
from botFlask import app
from tasks import *

try:
    stopFlag = Event()
    thread = TaskThread(stopFlag)
    thread.start()
    app.run(host='185.243.131.130',port =80)

except BaseException as e:
    print('BaseException')
    print(e)
    exit()
