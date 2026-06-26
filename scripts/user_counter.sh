#!/bin/bash

echo ""

# Script 4: List and Count interactive shell user
# No arguments needed - reads /etc/passwd directly

echo "=== INTERACTIVE SHELL USERS ==="

echo ""

grep -E "(/bin/bash|/bin/sh|/bin/zsh)$" /etc/passwd 

echo ""

grep -E "(/bin/bash|/bin/sh|/bin/zsh)$" /etc/passwd | awk -F: '{print $1}'

echo ""

TOTAL=$(grep -E "(/bin/bash|/bin/sh|/bin/zsh)$" /etc/passwd | wc -l)

echo "Total: $TOTAL interactive users"


