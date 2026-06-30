# Find Command Lab

## Objective

Learn how to locate files and directories efficiently in Linux and understand how `find` is used during system administration and security auditing.

---

## Command Syntax

```bash
find <starting_path> <conditions> <actions>
```

Example:

```bash
find /home -name "*.txt"
```

Searches for all `.txt` files inside `/home`.

---

# Commands Practiced

## Find by Name

```bash
find . -name "*.txt"
```

Finds all text files.

---

## Find Directories

```bash
find . -type d
```

Lists directories only.

---

## Find Files

```bash
find . -type f
```

Lists regular files only.

---

## Find Empty Files

```bash
find . -empty
```

Useful for cleanup.

---

## Find Large Files

```bash
find / -size +100M
```

Shows files larger than 100 MB.

---

## Find Recently Modified Files

```bash
find . -mtime -7
```

Files modified within the last 7 days.

---

## Find SUID Files

```bash
find / -perm -4000 -type f 2>/dev/null
```

Purpose:

- Locate files running with root privileges.
- Used during privilege-escalation audits.

Examples found:

- /usr/bin/passwd
- /usr/bin/su
- /usr/bin/mount

These are normally expected.

Unexpected SUID files may indicate security risks.

---

## Find World Writable Files

```bash
find / -perm -0002 -type f 2>/dev/null
```

Purpose:

Identify files that every user can modify.

Can lead to privilege escalation if sensitive files are writable.

---

## Suppress Permission Errors

```bash
2>/dev/null
```

Redirects error messages to `/dev/null`.

Keeps command output clean.

---

# Security Relevance

The `find` command is widely used by:

- System Administrators
- SOC Analysts
- Penetration Testers
- Cloud Security Engineers

Typical use cases:

- Locate misconfigured files
- Find sensitive data
- Detect privilege escalation paths
- Audit permissions
- Search log files
- Incident response

---

# Key Learnings

- `find` recursively searches directories.
- Filters can be combined.
- Permissions can be audited.
- SUID files require verification.
- World-writable files may be dangerous.
- `find` is one of the most important Linux security commands.
