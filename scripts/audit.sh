#!/bin/bash

# GATE 1: Linux Security Audit Script
# Finds world-writable files and root processes


# ============================================
# Gate 1 - Linux Security Audit Script
# ============================================

# Create output directory if it doesn't exist
mkdir -p ~/audit-output

# Generate Timestamp
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)

# Build output filename
OUTFILE=~/audit-output/audit_${TIMESTAMP}.txt


# Write report Header
echo "============================" > "$OUTFILE"
echo " Linux Security Audit Report" >> "$OUTFILE"
echo " Generated: $TIMESTAMP" >> "$OUTFILE"
echo "============================"  >> "$OUTFILE"



# Blank Line
echo "" >> "$OUTFILE"

# ============================================
# World-Writable Files
# ============================================


echo "[WORLD-WRITABLE FILES IN /tmp]" >> "$OUTFILE"

find /tmp -type f -perm -o+w 2>/dev/null >> "$OUTFILE"




echo "" >> "$OUTFILE"
# ============================================
# Root Processes
# ============================================

echo "[ACTIVE ROOT PROCESSES]" >> "$OUTFILE"


ps aux | awk '$1=="root"'  >>  "$OUTFILE"
echo "" >> "$OUTFILE"


echo "========== END OF REPORT ==========" >> "$OUTFILE"

echo "Audit complete. Report saved to: $OUTFILE"
