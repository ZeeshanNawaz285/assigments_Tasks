#!/bin/bash



#cd /home/eurus/Trash
#if(($? == 0)); then  rm *; fi



Trash_dir="/home/eurus/Trash"


find "$Trash_dir" -type f -mtime +1 -exec rm -f {} +



