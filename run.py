#!/usr/bin/env python3
from botFlask import app
try:
    app.run(host='185.243.131.130',port =80)
except BaseException as e:
    print('BaseException')
    print(e)
    exit()
