#!/bin/bash
while IFS= read -r line; do
    echo "Text read from file: $line"
    a=( $line )
#     cronjob="${a[0]} ${a[1]} * ${a[2]} ${a[3]} /usr/bin/python /home/saptashrungi/Downloads/Operating-Systems-Project-main/Operating-Systems-Project-main/meet.sh >> /home/saptashrungi/Downloads/Operating-Systems-Project-main/Operating-Systems-Project-main/meet.log 2>&1"
# (crontab -u saptashrungi -l; echo "$cronjob" ) | crontab -u saptashrungi -
    echo ${a[0]}
    echo ${a[1]}
    echo ${a[2]}
    echo ${a[3]}
done < details.txt