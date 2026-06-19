# Linux Permissions and Redirection Lab

**Date:** 2026-06-18

## Objective

Develop practical understanding of Linux file permissions, ownership, standard streams, and output redirection.

---

# Chapter 5 — Permissions

## Commands Executed

```bash
ls -la /etc/passwd
ls -la ~/hello.txt
chmod 755 hello.txt
chmod u+x,o-r hello.txt
chmod 644 hello.txt
sudo chown root:root hello.txt
find / -perm -4000 2>/dev/null
find / -perm -2000 2>/dev/null
```

## Observations

- Document actual outputs.
- Explain what rwx means.
- Explain difference between 755 and 644.
- Record examples of discovered SUID and SGID binaries.

## Key Learning

File permissions determine which users may read, write, or execute files and directories.

---

# Chapter 6 — Redirection

## Commands Executed

```bash
ls /etc > /tmp/list.txt
ls /var >> /tmp/list.txt
ls /nonexistent 2> /tmp/error.txt
ls /etc /nonexistent > /tmp/output.txt 2>&1
ls /nonexistent 2>/dev/null
```

## Observations

- Explain difference between > and >>.
- Explain purpose of stderr.
- Explain why /dev/null is useful.

## Key Learning

Linux treats standard output and standard error as independent data streams which can be redirected separately.

---

# Mandatory Kali Connection

## Nmap Service Scan

Command:

```bash
nmap -sV 127.0.0.1 > scan.txt
```

## Result

(Document actual findings)

## Why It Matters

Introduced practical use of output redirection while performing a real security-related task.

---

# Challenges Encountered

- Record mistakes made.
- Record corrections.
- Record troubleshooting steps.

---

# Summary

Today focused on Linux access control mechanisms and output stream management. These concepts form the foundation for future Bash automation and the upcoming Gate 1 audit script.
