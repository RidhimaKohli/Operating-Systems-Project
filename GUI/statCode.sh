
#!/bin/bash
mem=$(grep MemTotal /proc/meminfo)
filename="out.txt"
echo $mem>$filename
st=$(grep MemFree /proc/meminfo)
echo $st>>$filename
st2=$(grep MemAvailable /proc/meminfo)
echo $st2>>$filename