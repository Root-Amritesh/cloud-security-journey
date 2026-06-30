#!/bin/bash

#########################################
# FIND COMMAND CHEAT SHEET
#########################################

# Find by name
find . -name "*.txt"

# Find directories
find . -type d

# Find files
find . -type f

# Find empty files
find . -empty

# Find by size
find / -size +100M

# Find modified within last 7 days
find . -mtime -7

# Find executable files
find / -type f -executable

# Find SUID files
find / -perm -4000 -type f 2>/dev/null

# Find SGID files
find / -perm -2000 -type f 2>/dev/null

# Find world writable files
find / -perm -0002 -type f 2>/dev/null

# Find owned by root
find / -user root

# Find log files
find /var/log -name "*.log"

# Delete empty files
find . -empty -delete

# Find and remove *.tmp files
find . -name "*.tmp" -delete

# Find files older than 30 days
find . -mtime +30

# Find recently accessed files
find . -atime -7

# Find recently changed permission files
find . -ctime -7
