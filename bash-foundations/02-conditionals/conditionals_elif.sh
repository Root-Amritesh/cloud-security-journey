#!/bin/bash

score=89

if [ "$score" -ge 90 ]
then
    echo "Grade A"

elif [ "$score" -ge 75 ]
then
    echo "Grade B"

elif [ "$score" -ge 60 ]
then
    echo "Grade C"

else
    echo "Fail"

fi
