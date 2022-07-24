#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
import re
import sys
import signal


toMatch = re.compile(
                     r'^\d{1,3}\.\d{1,3}\.\d{1,3} \
                     \.\d{1,3}\s\-\s\[[0-9]{4}\-[0-9] \
                     {1,2}\-[0-9]{1,2}\s[0-9]{1,2}\: \
                     [0-9]{1,2}\:[0-9]{1,2}.[0-9]{1,6}\] \
                     \s\"GET\s\/projects\/260\sHTTP\/ \
                     1\.1\"\s\d{3}\s\d{1,4}$')
statusCodeTracker = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
fileSizeTracker = 0
lineCount = 0


def handler():
    return True


for line in sys.stdin:
    lineCount += 1
    if toMatch.match(line) is False:
        continue
    withoutDash = line.replace('-', '')
    arrayFromString = withoutDash.split(' ')
    try:
        statusCode = int(arrayFromString[6])
        if arrayFromString[5] and isinstance(int(arrayFromString[6]), int):
            statusCodeTracker[arrayFromString[6]] += 1
        fileSizeTracker += int(arrayFromString[7])
        if lineCount == 10 or signal.signal(signal.SIGINT, handler):
            print('File size: {}'.format(fileSizeTracker))
            for key, value in statusCodeTracker.items():
                if statusCode not in statusCodeTracker.keys():
                    continue
                print('{}: {}'.format(key, value))
            lineCount = 0
    except:
        pass
