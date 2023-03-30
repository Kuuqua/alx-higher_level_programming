#!/bin/bash
# Script that makes a request to causes an specific response
curl -sLX PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me -o /dev/null -w "You got me!"
