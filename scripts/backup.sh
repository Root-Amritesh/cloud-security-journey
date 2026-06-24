#!/bin/bash

# Script 3: Create a timestamped compressed backup
# Usage: ./backup.sh /home/kali/documents /tmp/backups

SOURCE_DIR="$1"
BACKUP_DIR="${2:-/tmp/backups}"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

ARCHIVE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"

mkdir -p "$BACKUP_DIR"

tar -czf "$ARCHIVE" "$SOURCE_DIR"

echo "Backup created: $ARCHIVE"
