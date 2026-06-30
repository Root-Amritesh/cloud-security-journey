# Linux Find Command

## Overview

The `find` command is one of the most powerful Linux utilities for locating files and directories based on different search conditions.

Unlike `ls`, which simply lists a directory, `find` recursively searches an entire directory tree and allows filtering based on:

- Name
- Type
- Owner
- Permissions
- Size
- Modification time
- Access time
- Executable status
- Empty files/directories

The `find` command is widely used in:

- Linux Administration
- Cloud Engineering
- DevOps
- Cybersecurity
- Digital Forensics
- Incident Response

---

# Learning Objective

After completing this lab I can:

- Search recursively
- Filter by permissions
- Filter by owner
- Search using modification time
- Identify SUID binaries
- Detect world-writable files
- Suppress permission errors
- Combine multiple search conditions

---

# Files

| File | Purpose |
|------|---------|
| README.md | Overview |
| NOTES.md | Detailed explanations |
| cheatsheet.sh | Quick command reference |

---

# Commands Practiced

```bash
find /tmp -perm -o+w -type f

find / -user root -type f 2>/dev/null

find / -perm -4000 -type f 2>/dev/null

find /var/log -mtime -1 -type f

find /etc -perm -o+w -type d 2>/dev/null
```

---

# Why This Matters

These commands are commonly used during:

- Security Audits
- System Hardening
- Privilege Escalation Assessments
- Incident Response
- Linux Administration

They are also directly applicable to the upcoming Gate 1 audit scripts.
