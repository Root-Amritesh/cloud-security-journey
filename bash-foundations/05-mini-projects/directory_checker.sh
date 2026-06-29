#!/bin/bash

directory="${1:-/var/log}"

if [ -d "$directory" ]
then
    echo "Directory exists."
    echo
    echo "Contents:"

    for file in "$directory"/*
    do
        echo "$(basename "$file")"
    done

else
    echo "Directory does not exist."
fi
