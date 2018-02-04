#!/usr/bin/python

import uuid
import requests
import urllib2
import subprocess
from ConfigParser import ConfigParser

# ip_address = ['40.71.217.187', '40.76.213.148', '52.55.20.102']  # new API, Azure DEV(old API), AWS DEV
ip_address = ['localhost:8080']  # new API, Azure DEV(old API), AWS DEV
urls = []
test_url = '/deaddrop/'

mymac = uuid.getnode()
print mymac

alldevices = ''
individual = ''
ver2 = None

s = requests.Session()
r = s.get("http://localhost:8080/ping/1234567890")
print r.text

r = s.get("http://localhost:8080/deaddrop/1234567890")
print r.text
