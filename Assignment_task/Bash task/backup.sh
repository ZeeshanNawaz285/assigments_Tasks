#!/bin/bash


backupt1="backup_Task1.$(date +%Y%m%d_%H%M%S).tar"


find /home/eurus/Assignment_task -type f -mtime -1 -print0 | tar -czvf "$backupt1" --null -T -

