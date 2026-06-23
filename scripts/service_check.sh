#!/bin/bash

# Script 2: Check if a service is running
# Usage: ./service_check.sh sshd

SERVICE=${1:-"sshd"}

if systemctl is-active --quiet "$SERVICE"; then
    echo "[✓ UP]   $SERVICE is RUNNING"
else
    echo "[✗ DOWN] $SERVICE is NOT running"
fi
