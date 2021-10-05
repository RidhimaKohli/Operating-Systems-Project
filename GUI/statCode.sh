
#!/bin/bash
mem=$(grep MemTotal /proc/meminfo)
filename="out.txt"
echo $mem>$filename
st=$(grep MemFree /proc/meminfo)
echo $st>>$filename