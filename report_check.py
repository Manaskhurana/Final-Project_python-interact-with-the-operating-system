#!/usr/bin/env python3
import sys
import re
import operator
import csv


per_user = {} 
errors = {}

with open('syslog.log') as file:
    
    for line in file.readlines():
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        if error_msg not in errors.keys():
            errors[error_msg] = 1
        else:
            errors[error_msg] += 1

        if user not in per_user.keys():
            per_user[user] = {}
            per_user[user]['INFO'] = 0
            per_user[user]['ERROR'] = 0
    
        if code == 'INFO':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]["INFO"] += 1
        elif code == 'ERROR':
            if user not in per_user.keys():
                per_user[user] = {}
                per_user[user]['INFO'] = 0
            else:
                per_user[user]['ERROR'] += 1


errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

file.close()
errors_list.insert(0, ('Error', 'Count'))


with open('user_statistics.csv', 'w', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' +
                       str(value['INFO']) + ',' + str(value['ERROR'])+'\n')


with open('error_message.csv', 'w', newline='') as error_csv:
    for key, value in errors_list:
        error_csv.write(str(key) + ' ' + str(value))
