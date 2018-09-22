#!/bin/sh
# launcher.sh
# navigate to repo/doorbell then run the doorbell script, then back to home

cd /
cd home/pi/repo/doorbell
sudo python doorbell.py
cd /

