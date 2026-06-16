# Pipes and Redirection Lab

**Date:** 2026-06-16

## Objective

Create three original Linux pipe commands using tools available in Kali Linux and explain their security relevance.

---

## Command 1

```bash
history | tail -20 | wc -l
```

### What it does

* Displays command history
* Shows the last 20 commands
* Counts the resulting lines

### Why it matters

Security professionals spend most of their time in the terminal. Understanding command history helps with auditing activity, troubleshooting mistakes, and reviewing recent actions performed on a system.

### Concepts Used

* Pipe (`|`)
* history
* tail
* wc

---

## Command 2

```bash
ps aux | grep ssh | wc -l
```

### What it does

* Lists all running processes
* Searches for SSH-related processes
* Counts matching entries

### Why it matters

SSH is the primary method used to administer Linux servers remotely. Being able to identify SSH-related processes helps verify remote access activity and forms part of basic system monitoring.

### Concepts Used

* Pipe (`|`)
* ps
* grep
* wc

---

## Command 3

```bash
ls -la ~/ | grep "^d" | wc -l
```

### What it does

* Lists all files and directories in the home folder
* Filters only directories
* Counts how many directories exist

### Why it matters

Security analysts frequently need to understand filesystem structure quickly. Counting directories can help identify unexpected folders, suspicious locations, or changes to a user's environment.

### Concepts Used

* Pipe (`|`)
* ls
* grep
* wc

---

## Skills Practiced

* Pipes
* Command chaining
* Output filtering
* Counting results
* Security-focused Linux analysis

---

## Reflection

This exercise reinforced the concept that Linux commands become significantly more powerful when combined using pipes. Rather than running commands individually, output from one command can be transformed, filtered, and analyzed by another command to answer specific operational and security questions.

This approach is fundamental for Linux administration, cloud engineering, incident response, and security operations.
