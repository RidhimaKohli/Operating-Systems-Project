#!/bin/bash
mem=$(grep MemTotal /proc/meminfo) 
memory_file="memory.txt"
echo $mem>$memory_file
st=$(grep MemFree /proc/meminfo)
echo $st>>$memory_file
st2=$(grep MemAvailable /proc/meminfo)
echo $st2>>$memory_file
proc_count=$(grep -c processor /proc/cpuinfo)
p="Number of processor : "
cpu_file="cpu.txt"
p+=$proc_count
echo $p>$cpu_file
model_name=$(grep "model name" /proc/cpuinfo | head -1 | cut -d: -f2 | sed 's/^[ \t]*//;s/[ \t]*$//')
m="Model : "
m+=$model_name
echo $m>>$cpu_file