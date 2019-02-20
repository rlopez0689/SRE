#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='Most Active Group')

parser.add_argument('passwd')
parser.add_argument('group')
arguments = parser.parse_args()

passwd_file = open(arguments.passwd, "r")
group_file = open(arguments.group, "r")
groups_users = {}
groups = {}
available_users = []
for line in passwd_file:
    item = line.split(":")
    if 'nologin' not in item[6]:
        groups_users.setdefault(item[3], []).append(item[0])
        available_users.append(item[0])

for line in group_file:
    item = line.split(":")
    groups[item[2]] = item[0]
    if item[3].rstrip():
        users = item[3].rstrip().split(',')
        for user in users:
            if user in available_users and user not in groups_users[item[2]]:
                groups_users[item[2]].append(user)

max_value = len(max(groups_users.items(), key=lambda x: len(set(x[1])))[1])
max_groups = [key for key, val in groups_users.items() if len(val) == max_value]
for group in max_groups: print("{}:{}".format(groups[group], max_value))

