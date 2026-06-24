# 2026-06-23 — Script 3: Timestamped Compressed Backup Utility

## Task Objective

Create a Bash script capable of:

* Accepting a source directory as input
* Accepting a backup destination as input
* Generating a timestamp automatically
* Creating a compressed `.tar.gz` archive
* Saving the archive inside the destination directory
* Producing a unique backup filename on every execution

This task serves as Script 3 of 4 for Gate 1 preparation.

The primary learning objective is not backup creation itself.

The primary learning objective is understanding:

* Command substitution
* Dynamic variable generation
* Timestamp creation
* Archive management
* Automated file naming

These concepts will later be reused in audit scripts, logging systems, security tooling, and automation workflows.

---

# Deliverable

## backup.sh

```bash
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
```

---

# Lab Environment

Operating System:

```text
Kali Linux
```

Working Repository:

```text
cloud-security-journey
```

Script Location:

```text
cloud-security-journey/scripts/backup.sh
```

---

# Commands Executed

### Create Script

```bash
nano backup.sh
```

### Make Executable

```bash
chmod +x backup.sh
```

### Verify Permissions

```bash
ls -l backup.sh
```

### Create Test Directory

```bash
mkdir -p ~/backup-test
```

### Create Test Files

```bash
echo "Linux" > ~/backup-test/file1.txt

echo "Cyber" > ~/backup-test/file2.txt

echo "Security" > ~/backup-test/file3.txt
```

### Verify Test Data

```bash
ls ~/backup-test
```

### Execute Backup

```bash
./backup.sh ~/backup-test ~/backups
```

### Verify Backup Creation

```bash
ls -lh ~/backups
```

### Verify Archive Contents

```bash
tar -tzf ~/backups/backup_*.tar.gz
```

---

# Output Evidence

## Script Execution

```text
Backup created: /home/kali/backups/backup_20260623_145830.tar.gz
```

## Archive Verification

```text
backup-test/
backup-test/file1.txt
backup-test/file2.txt
backup-test/file3.txt
```

Result:

```text
Archive successfully created and verified.
```

---

# Line-by-Line Analysis

## Source Directory Variable

```bash
SOURCE_DIR="$1"
```

Stores the first command-line argument.

Example:

```bash
./backup.sh ~/backup-test
```

Results in:

```bash
SOURCE_DIR=/home/kali/backup-test
```

---

## Backup Destination Variable

```bash
BACKUP_DIR="${2:-/tmp/backups}"
```

Uses the second command-line argument.

If none is supplied:

```bash
/tmp/backups
```

is used automatically.

This prevents the script from failing when a destination is omitted.

---

## Command Substitution

```bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
```

Most important concept introduced in this task.

Structure:

```bash
$(command)
```

Meaning:

```text
Execute command.
Capture output.
Insert output into variable.
```

Example:

```bash
USER=$(whoami)
```

Produces:

```bash
USER=kali
```

---

## Date Formatting

```bash
date +%Y%m%d_%H%M%S
```

Example output:

```text
20260623_145830
```

Breakdown:

```text
%Y = Year
%m = Month
%d = Day
%H = Hour
%M = Minute
%S = Second
```

This creates filenames that are:

* Unique
* Sortable
* Safe for Linux filesystems

---

## Dynamic Archive Naming

```bash
ARCHIVE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"
```

Example result:

```text
/home/kali/backups/backup_20260623_145830.tar.gz
```

Advantages:

* No overwriting previous backups
* Easy chronological organization
* Easier auditing and tracking

---

## Automatic Directory Creation

```bash
mkdir -p "$BACKUP_DIR"
```

Creates the destination directory if it does not exist.

The `-p` flag prevents errors if the directory already exists.

This makes the script safe to run repeatedly.

---

## Archive Creation

```bash
tar -czf "$ARCHIVE" "$SOURCE_DIR"
```

Flags used:

```text
c = create archive
z = gzip compression
f = filename follows
```

Produces:

```text
backup_20260623_145830.tar.gz
```

A compressed archive containing the source directory.

---

## User Feedback

```bash
echo "Backup created: $ARCHIVE"
```

Provides immediate confirmation of success.

Without this line the script would complete silently.

---

-----------NOTES-----------

# What Was Actually Learned Today

Most people would describe this task as:

```text
Learning how to create backups.
```

That is not the real lesson.

The actual lesson was learning how Bash can generate values dynamically during execution.

The most important concept introduced was:

```bash
$(...)
```

Command substitution.

This allows scripts to execute commands and immediately use their output.

Examples:

```bash
$(date)

$(whoami)

$(hostname)

$(pwd)
```

This pattern appears constantly in:

* Security automation
* Audit reporting
* Incident response scripts
* Reconnaissance tooling
* Cloud automation
* DevOps workflows

---

# Security Relevance

Timestamped archives are frequently used for:

* Evidence preservation
* Log collection
* Incident response
* Configuration backups
* System snapshots
* Security reporting

A security engineer often needs uniquely named output files to avoid overwriting evidence or historical data.

Timestamp generation solves this problem.

---

# Verification Mindset

Creating a backup is not enough.

Verification is mandatory.

After archive creation:

```bash
tar -tzf archive.tar.gz
```

was used to inspect archive contents.

This reinforces an important engineering principle:

```text
Never assume success.

Verify success.
```

---

# Issues Encountered

During Git operations an incorrect path was initially used:

```bash
git add logs/filename.md
```

while already inside:

```bash
cloud-security-journey/logs
```

This caused Git to search for:

```bash
logs/logs/filename.md
```

which did not exist.

Resolution:

```bash
git add filename.md
```

Lesson Learned:

Always verify current working directory using:

```bash
pwd
```

before staging files.

---

# Toolbox Expansion

New Bash capabilities acquired:

✓ Command substitution

```bash
$(command)
```

✓ Timestamp generation

```bash
date +%Y%m%d_%H%M%S
```

✓ Dynamic filename creation

```bash
backup_${TIMESTAMP}.tar.gz
```

✓ Automatic directory creation

```bash
mkdir -p
```

✓ Compressed archive creation

```bash
tar -czf
```

✓ Archive inspection

```bash
tar -tzf
```

✓ Backup verification workflow

---

# Why This Task Exists In The Roadmap

The purpose of this task is not backup creation.

The purpose is introducing timestamp generation and command substitution before Gate 1.

Future tasks will require:

* Timestamped audit reports
* Timestamped scan results
* Timestamped log files
* Automated output generation

This script teaches the exact mechanism that those future tasks depend on.

-----------END NOTES-----------

---

# Skills Demonstrated

✓ Bash scripting

✓ Variables

✓ Command-line arguments

✓ Default values

✓ Command substitution

✓ Date formatting

✓ Dynamic file naming

✓ Directory creation

✓ tar archive management

✓ gzip compression

✓ Archive verification

✓ Basic automation design

---

# Result

Successfully created, executed, and verified a timestamped compressed backup utility.

The script generates unique archive names automatically and safely stores compressed backups in a specified destination directory.

Script 3 of 4 completed.

---
