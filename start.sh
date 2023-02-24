#########################################################################
# File Name: s.sh
# Method: 
# Author: Jerry Shi
# Mail: jerryshi0110@gmail.com
# Created Time: Fri 24 Feb 2023 12:47:36 PM UTC
#########################################################################
#!/bin/bash
cd ./service

echo $(pwd)

nohup python3 service.py > /dev/null 2>nohup.out &
