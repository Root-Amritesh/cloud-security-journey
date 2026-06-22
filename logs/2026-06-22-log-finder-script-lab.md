# 2026-06-22 — Bash Scripting Lab 01: Log Finder Script

## Lab Information

| Field     | Value                               |
| --------- | ----------------------------------- |
| Date      | 2026-06-22                          |
| Phase     | Phase 0 — Linux Foundations         |
| Week      | Week 2                              |
| Task      | Script 1 of 4                       |
| Script    | log_finder.sh                       |
| Objective | Find `.log` files older than 7 days |

---

# Objective

The objective of this lab was to create a Bash script capable of identifying log files that have not been modified in more than seven days.

The lab introduces several fundamental Bash scripting concepts:

* Shebangs
* Variables
* Positional Parameters
* Default Values
* File Searching
* File Filtering
* Script Permissions
* Bash Debugging

---

# Deliverable

Created:

```bash
log_finder.sh
```

Final Script:

```bash
#!/bin/bash

# Script 1: Find old log files
# Usage: ./log_finder.sh /var/log

TARGET_DIR=${1:-"/var/log"}

echo "=== .log files older than 7 days in: $TARGET_DIR ==="

find "$TARGET_DIR" -name "*.log" -mtime +7 -type f
```

---

# Commands Executed During Lab

## Script Creation

```bash
nano log_finder.sh
```

Purpose:

Create and edit the Bash script.

---

## Make Script Executable

```bash
chmod +x log_finder.sh
```

Purpose:

Add execute permission so Linux can run the file directly.

---

## Verify Permissions

```bash
ls -alpsh
```

Purpose:

Verify file existence and permissions.

Observed:

```text
-rwxrwxr-x
```

Meaning:

* Owner: Read, Write, Execute
* Group: Read, Write, Execute
* Others: Read, Execute

---

## Test 1

```bash
./log_finder.sh /var/log
```

Purpose:

Run script against the system log directory.

---

## Test 2

```bash
./log_finder.sh
```

Purpose:

Verify default value behavior.

Expected default:

```text
/var/log
```

---

## Test 3

```bash
./log_finder.sh hello.txt
```

Purpose:

Observe script behavior when supplied with a file rather than a directory.

---

## Test 4

```bash
./log_finder.sh /tmp
```

Purpose:

Verify argument handling with a different directory.

---

# Errors Encountered

## Error 1 — Incorrect Variable Expansion

Incorrect:

```bash
TARGET_DIR=#{1:-"/var/log"}
```

Correct:

```bash
TARGET_DIR=${1:-"/var/log"}
```

Cause:

Bash variable expansion uses `$`, not `#`.

---

## Error 2 — Missing Space After echo

Incorrect:

```bash
echo"Hello"
```

Correct:

```bash
echo "Hello"
```

Cause:

Bash interpreted `echo"Hello"` as a command name rather than the `echo` command.

---

# ---------------- NOTES ----------------

# Understanding What This Script Actually Does

Imagine a Linux server that has been running for months.

Applications continuously generate log files:

```text
/var/log/auth.log
/var/log/syslog
/var/log/nginx/access.log
```

Over time these files accumulate.

A Linux administrator may need to:

* Identify old logs
* Archive logs
* Delete stale logs
* Investigate incidents

Instead of repeatedly typing a long command, we automate the task using a Bash script.

This follows a core Linux principle:

> If you perform a task repeatedly, automate it.

---

# What Is A Bash Script?

A Bash script is simply a text file containing Linux commands.

Example:

```bash
#!/bin/bash

echo "Hello World"
```

When executed:

```bash
./script.sh
```

Linux reads the file line by line and executes each command sequentially.

Execution Flow:

```text
Line 1
 ↓
Line 2
 ↓
Line 3
 ↓
Output
```

---

# Understanding The Shebang

```bash
#!/bin/bash
```

This line is called the **Shebang**.

Purpose:

Tell Linux which interpreter should execute the script.

Examples:

```text
#!/bin/bash      → Bash
#!/usr/bin/python3 → Python
#!/usr/bin/perl     → Perl
```

Without a shebang Linux may not know how to execute the file correctly.

---

# Understanding Positional Parameters

When a script is executed:

```bash
./script.sh one two three
```

Linux automatically creates:

```bash
$1 = one
$2 = two
$3 = three
```

These are called Positional Parameters because their meaning depends on their position.

Example:

```bash
echo $1
```

Output:

```text
one
```

---

# Understanding Default Values

The most important line in this lab:

```bash
TARGET_DIR=${1:-"/var/log"}
```

General Pattern:

```bash
${VARIABLE:-DEFAULT_VALUE}
```

Meaning:

```text
Use VARIABLE

If VARIABLE does not exist

Use DEFAULT_VALUE
```

Example 1:

```bash
./log_finder.sh /tmp
```

Result:

```text
TARGET_DIR=/tmp
```

Example 2:

```bash
./log_finder.sh
```

Result:

```text
TARGET_DIR=/var/log
```

This pattern is heavily used in production Bash scripts.

---

# Understanding Variables

Creating a variable:

```bash
NAME="Amritesh"
```

Using a variable:

```bash
echo $NAME
```

Output:

```text
Amritesh
```

Variable expansion:

```bash
echo $NAME
```

becomes:

```bash
echo Amritesh
```

before execution.

Linux replaces the variable with its value.

---

# Understanding The find Command

General Syntax:

```bash
find <directory> <filters>
```

Example:

```bash
find /var/log
```

The command recursively searches:

```text
Directory
 ├── File
 ├── File
 └── Subdirectory
       ├── File
       └── File
```

This makes `find` one of the most powerful Linux administration commands.

---

# Understanding Every Filter

## Filter 1

```bash
-name "*.log"
```

Meaning:

Only match files ending with:

```text
.log
```

Examples:

Matches:

```text
auth.log
access.log
error.log
```

Does Not Match:

```text
notes.txt
report.pdf
image.png
```

---

## Filter 2

```bash
-mtime +7
```

Meaning:

Modification Time greater than 7 days.

Examples:

| File Age | Match |
| -------- | ----- |
| 2 Days   | No    |
| 5 Days   | No    |
| 8 Days   | Yes   |
| 30 Days  | Yes   |

---

## Filter 3

```bash
-type f
```

Meaning:

Return files only.

Other useful types:

```bash
-type d
```

Directories only.

```bash
-type l
```

Symbolic links only.

---

# Why Quotation Marks Matter

Correct:

```bash
find "$TARGET_DIR"
```

Suppose:

```bash
TARGET_DIR="/home/kali/My Documents"
```

With quotes:

```text
One argument
```

Without quotes:

```text
Two separate arguments
```

which breaks the command.

Professional Bash scripts almost always quote path variables.

---

# Common Beginner Mistakes

## Wrong

```bash
TARGET_DIR=#{1:-"/var/log"}
```

Correct:

```bash
TARGET_DIR=${1:-"/var/log"}
```

---

## Wrong

```bash
echo"Hello"
```

Correct:

```bash
echo "Hello"
```

---

## Risky

```bash
find $TARGET_DIR
```

Preferred:

```bash
find "$TARGET_DIR"
```

---

# Cybersecurity Applications

The exact same concepts are used for:

Finding recently modified files:

```bash
find / -mtime -1
```

Finding world-writable files:

```bash
find / -perm -002
```

Finding backup files:

```bash
find /backup -mtime +30
```

Finding PHP files:

```bash
find /var/www -name "*.php"
```

Finding suspicious files during incident response:

```bash
find / -type f -mtime -1
```

---

# Key Takeaways

After this lab, you should understand:

* What a Bash script is
* How Linux executes scripts
* What a Shebang does
* What positional parameters are
* How `$1` works
* How default values work
* How variables are expanded
* How the `find` command works
* How file filtering works
* Why quotation marks matter
* How Bash syntax errors occur
* Basic Linux automation principles

---

# Outcome

Successfully created, debugged, executed, and understood a reusable Bash script capable of identifying `.log` files older than seven days.

Status:

✅ Completed

Gate Progress:

✅ Script 1 of 4 Complete
