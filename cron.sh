#!/bin/bash
cronjob="* * * * * /usr/bin/python /home/saptashrungi/Downloads/Operating-Systems-Project-main/Operating-Systems-Project-main/test_cron.py >> /home/saptashrungi/Downloads/Operating-Systems-Project-main/Operating-Systems-Project-main/cron.log 2>&1"
(crontab -u saptashrungi -l; echo "$cronjob" ) | crontab -u saptashrungi -