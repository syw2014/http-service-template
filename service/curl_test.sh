#########################################################################
# File Name: curl_test.sh
# Method: 
# Author: Jerry Shi
# Mail: jerryshi0110@gmail.com
# Created Time: Fri 24 Feb 2023 12:55:57 PM UTC
#########################################################################
#!/bin/bash
curl -X POST -d @data.json http://172.31.6.84:6006/ai/nlp/test
