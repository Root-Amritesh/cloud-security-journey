# 2026-06-26 — Gate 1: Linux Security Audit Script

## Objective

Complete Gate 1 by building a Bash script (`audit.sh`) capable of performing a basic Linux security audit.

The script must:

* Create an output directory if it does not already exist.
* Generate a timestamped report.
* Identify world-writable files inside `/tmp`.
* List every running process owned by `root`.
* Save all results into a report.
* Print the report location after execution.

---

# Files

```
scripts/
└── audit.sh

audit-output/
└── audit_YYYY-MM-DD_HH-MM-SS.txt
```

---

# Commands Executed

```bash
cd ~/cloud-security-journey/scripts

nano audit.sh

chmod +x audit.sh

./audit.sh

bash -n audit.sh

cat -n audit.sh

mousepad audit.sh

ls -lh ~/audit-output

cat ~/audit-output/audit_*.txt
```

---

# Problems Encountered

## Problem 1

```
No such file or directory
```

appeared on every output redirection line.

### Cause

The output filename variable was incorrectly written as:

```bash
OUTPUT=$~/audit-output/...
```

Two issues existed:

* Wrong variable name (`OUTPUT` vs `OUTFILE`)
* Invalid path construction using `$~`

---

## Problem 2

Timestamp format contained:

```bash
%M%- %S
```

instead of

```bash
%M-%S
```

This produced an invalid timestamp format.

---

## Debugging Process

Instead of guessing, the script was inspected step-by-step.

Validation commands:

```bash
bash -n audit.sh
```

Checked for Bash syntax errors.

```bash
cat -n audit.sh
```

Displayed numbered source code to locate mistakes quickly.

Both techniques significantly reduced debugging time.

---

# Fixes Applied

Corrected timestamp:

```bash
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
```

Corrected output filename:

```bash
OUTFILE=~/audit-output/audit_${TIMESTAMP}.txt
```

Re-ran the script.

Successfully generated the audit report.

---

# Final Result

Successfully created:

```
~/audit-output/audit_YYYY-MM-DD_HH-MM-SS.txt
```

Report contained:

* World-writable files inside `/tmp`
* Active root processes

Terminal displayed the report location after completion.

---

# Learning Outcomes

This gate combined every major Bash concept learned so far.

Concepts reinforced:

* Variables
* Command substitution
* Dynamic filenames
* mkdir -p
* Output redirection
* File searching with find
* Permission filtering
* Error redirection
* Pipes
* awk
* Process enumeration
* Report generation

---

# Practical Security Value

## World-Writable Files

Files writable by everyone can become privilege-escalation opportunities.

Example:

A cron script accidentally marked world-writable could be modified by a low-privilege attacker, resulting in code execution as root.

---

## Root Processes

Processes owned by root execute with unrestricted privileges.

If any vulnerable service runs as root and is exploited, the attacker immediately gains full system control.

Auditing these processes helps identify unnecessary attack surface.

---

-----------NOTES-----------

## Mental Model

```
Create Folder
      ↓
Generate Timestamp
      ↓
Build Filename
      ↓
Write Report Header
      ↓
Find World-Writable Files
      ↓
List Root Processes
      ↓
Save Report
      ↓
Print Report Location
```

Remember this flow rather than memorizing commands.

---

## Commands to Never Forget

### mkdir -p

Creates directories safely.

If the directory already exists, no error is produced.

---

### $(command)

Runs a command and stores its output.

Example:

```bash
TODAY=$(date)
```

---

### >

Creates or overwrites a file.

---

### >>

Appends to an existing file.

---

### 2>/dev/null

Redirects error messages into Linux's "black hole".

Keeps output clean.

---

### find

Searches the filesystem.

Common pattern:

```bash
find <location> <conditions>
```

---

### -perm -o+w

Find files writable by "others".

These are world-writable files.

---

### ps aux

Lists every running process.

---

### awk '$1=="root"'

Filters only processes where the USER column equals root.

---

## Biggest Lesson From Today

The script initially failed because of a **variable assignment mistake**, not because of Bash syntax.

Incorrect:

```bash
OUTFILE=$~/audit-output/...
```

Correct:

```bash
OUTFILE=~/audit-output/...
```

Never place `$` before `~`.

---

## Debugging Workflow

Whenever a Bash script fails:

1. Read the error carefully.
2. Validate syntax using:

```bash
bash -n script.sh
```

3. Display numbered source code:

```bash
cat -n script.sh
```

4. Inspect variables before assuming command failure.

Most Bash bugs are caused by variables—not commands.
