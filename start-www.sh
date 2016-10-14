#!/bin/bash

while true
do
    python www/app.py

    echo 'restarting ...'
    for((i=5; i>0; i--))
    do
        echo "$i";
        sleep 1;
    done
done
