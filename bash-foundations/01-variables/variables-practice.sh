#!/bin/bash

echo "===== Variables ====="

file="report"
name="Amritesh"
directory="/home/kali"

echo
echo "Variable expansion"

echo "$file"
echo "${file}.txt"

echo
echo "$name"
echo "${name}_backup"

echo
echo "${file}.log"

echo
echo "${directory}/logs"

echo
echo "===== Command Substitution ====="

today=$(date)

echo "$today"

echo
echo "===== Quoting Example ====="

folder="My Report.txt"

echo
echo "Without quotes:"
echo cat $folder

echo
echo "With quotes:"
echo cat "$folder"
