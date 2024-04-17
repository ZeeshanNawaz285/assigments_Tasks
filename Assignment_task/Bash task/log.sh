#!/bin/bash 


who |awk '{print "User:", $1, "Last Login:", $3, $4}'

