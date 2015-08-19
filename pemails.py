#!/usr/bin/evn python
# Pull emails out of file
# Work in progress
# By: Spencer Heckathorn
import re

source = open("news emails", "r")
regex = re.compile(r'[\w\.-]+@[\w\.-]+')

for line in source:
    email_address = regex.findall(line)
    for emailAdd in email_address:
        print emailAdd
