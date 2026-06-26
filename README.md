# Cloud Security Journey

June 2026. Zero certs. Zero projects. Zero network.
Cloud Security Architect. Germany by 2032.


# Gate 1 — Linux Security Audit Script

## Overview

This project is the first security automation milestone in my Linux and Cybersecurity learning journey.

The goal of this project is to build a Bash script (`audit.sh`) capable of performing a basic Linux security audit by identifying potentially dangerous files and privileged processes. The generated report is automatically saved inside the `audit-output/` directory with a unique timestamp, allowing every audit to be preserved.

---

# Project Objectives

The script performs the following tasks:

* Creates an output directory if it does not already exist.
* Generates a timestamped audit report.
* Searches `/tmp` for world-writable files.
* Lists every active process running as the `root` user.
* Saves all findings into a structured report.
* Prints the report location after execution.

---

# Why World-Writable Files Matter

A **world-writable file** is any file that every user on the system can modify.

This permission is granted using:

```bash
chmod o+w filename
```

or detected using:

```bash
find /tmp -perm -o+w -type f
```

The `o` represents **Others** (everyone except the owner and group).

## Security Risk

World-writable files are dangerous because an attacker with low-level access can modify their contents.

### Example Attack Scenario

Imagine a scheduled backup script executed every hour by the root user.

If that script accidentally becomes world-writable, an attacker could replace its contents with malicious commands.

When the scheduled task runs again, the malicious code executes with **root privileges**, resulting in a complete privilege escalation.

For this reason, identifying world-writable files is a common task during Linux security audits.

---

# Why Root Processes Matter

Processes owned by **root** execute with unrestricted system privileges.

Unlike normal users, root bypasses Linux permission restrictions and has full control over:

* Files
* Services
* Network configuration
* User accounts
* System configuration

The audit script identifies these processes using:

```bash
ps aux | awk '$1=="root"'
```

## Security Risk

If any process running as root contains a vulnerability (such as command injection, buffer overflow, or remote code execution), an attacker who successfully exploits it gains **root-level access** to the operating system.

Auditing privileged processes helps identify unnecessary services and reduces the attack surface.

---

# Script Workflow

```
Create Output Directory
            │
            ▼
Generate Timestamp
            │
            ▼
Create Audit Report
            │
            ▼
Find World-Writable Files
            │
            ▼
List Root Processes
            │
            ▼
Save Results
            │
            ▼
Display Report Location
```

---

# Technologies Used

* Bash
* Linux File Permissions
* `find`
* `mkdir`
* `date`
* `ps`
* `awk`
* Output Redirection (`>`, `>>`)
* Error Redirection (`2>/dev/null`)

---

# Usage

Make the script executable:

```bash
chmod +x scripts/audit.sh
```

Run the script:

```bash
./scripts/audit.sh
```

Example output:

```text
Audit complete. Report saved to:
/home/kali/audit-output/audit_2026-06-26_14-18-41.txt
```

View the generated report:

```bash
cat ~/audit-output/audit_*.txt
```

---

# Example Report

```text
===================================
 Linux Security Audit Report
 Generated: 2026-06-26_14-18-41
===================================

[WORLD-WRITABLE FILES IN /tmp]

/tmp/example.txt

[ACTIVE ROOT PROCESSES]

root      1     systemd
root    523     NetworkManager

========== END OF REPORT ==========
```

---

# Skills Demonstrated

* Bash Scripting
* Linux File Permissions
* Security Auditing
* Process Enumeration
* Command Substitution
* Dynamic File Generation
* Output Redirection
* Text Processing
* Linux Automation

---

# Lessons Learned

This project combined every concept learned throughout the first four Bash scripting exercises into one practical security automation task.

Key concepts reinforced include:

* Variables
* Command substitution (`$(...)`)
* Dynamic filenames
* Safe directory creation (`mkdir -p`)
* File discovery using `find`
* Permission analysis
* Process enumeration (`ps`)
* Pipelines (`|`)
* Text filtering with `awk`
* Report generation using output redirection

This project represents the successful completion of **Gate 1** in my Linux and Cloud Security learning roadmap.
