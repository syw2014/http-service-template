#########################################################################
# File Name: s.sh
# Method: 
# Author: Jerry Shi
# Mail: jerryshi0110@gmail.com
# Created Time: Fri 24 Feb 2023 12:47:36 PM UTC
#########################################################################
#!/bin/bash

# TODO, modified the pid filename the same as sanice-name
main_process_pid=$(cat ./logout/ai-nlp-techs-main-pid.txt)

echo "${main_process_pid}"

kill ${main_process_pid} 
