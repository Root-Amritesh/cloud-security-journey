# Linux Command Line Foundations — Chapters 1–4 Completion Report

**Date:** 2026-06-16
**Repository:** cloud-security-journey
**Phase:** Week 1 — Linux Foundations
**Status:** Completed

---

# Objective

Complete the foundational Linux command-line material required for Week 1 of the Cloud Security roadmap through hands-on practice in Kali Linux using SSH.

Resources used:

* Linux Command Line Book (linuxcommand.org) — Chapters 1–4
* TCM Security — Linux for Ethical Hackers (First Hour)
* freeCodeCamp Linux Command Line Course (Supplemental)
* Kali Linux
* SSH Terminal Sessions

---

# Environment

Operating System:

* Kali Linux

Access Method:

* SSH

Reason:

All exercises and labs were completed through SSH to build familiarity with remote Linux administration, terminal-only workflows, and real-world Linux server interaction.

---

# Linux Command Line Book Progress

## Chapter 1 — Introduction

Completed:

* Linux terminal basics
* Shell concepts
* Running commands from the command line
* Understanding command execution

Commands Practiced:

```bash
pwd
ls
```

Outcome:

Successfully interacted with the Linux terminal and understood the role of the shell.

---

## Chapter 2 — Navigation

Completed:

* Filesystem hierarchy
* Current working directory
* Absolute paths
* Relative paths
* Directory navigation

Commands Practiced:

```bash
cd /
ls

cd /etc
ls

cd /etc/ssh
pwd
```

Outcome:

Successfully navigated the Linux filesystem manually and reached system directories without relying on graphical tools.

---

## Chapter 3 — Files and Directories

Completed:

* Creating directories
* Creating files
* Copying files
* Moving files
* Renaming files
* Deleting files

Commands Practiced:

```bash
mkdir ~/test-folder

touch ~/test-folder/file1.txt

cp ~/test-folder/file1.txt \
~/test-folder/file2.txt

mv ~/test-folder/file2.txt \
~/test-folder/file2-moved.txt

rm ~/test-folder/file1.txt
```

Outcome:

Successfully managed files and directories entirely through terminal commands.

---

## Chapter 4 — Help and Documentation

Completed:

* Using manual pages
* Command help systems
* Understanding command options

Commands Practiced:

```bash
man ls

man cp

ls --help

cp --help
```

Outcome:

Able to locate command documentation and understand command usage directly from the terminal.

---

# Blueprint Deliverables

## Deliverable 1

Create, copy, move, and delete files using terminal commands only.

Status:

✅ Completed

Commands Used:

```bash
touch
cp
mv
rm
```

---

## Deliverable 2

Run the following command without looking up syntax:

```bash
ls /etc | grep ssh > ~/day4.txt
```

Verification:

```bash
cat ~/day4.txt
```

Status:

✅ Completed

Concepts Practiced:

* Pipes
* grep
* Output redirection
* File creation through redirection

---

# TCM Security Linux Course Progress

Course:

Linux for Ethical Hackers (First Hour)

Status:

✅ Completed

Topics Covered:

* Linux filesystem navigation
* Directory traversal
* ls command family
* File creation
* File deletion
* File movement
* File copying
* Linux help systems
* Basic terminal workflow

Learning Method:

Every command demonstrated during the course was reproduced manually in Kali Linux through SSH.

Outcome:

Practical experience was prioritized over passive video consumption.

---

# Supplemental Learning

Resource:

freeCodeCamp Linux Command Line Full Course

Purpose:

Used as a secondary explanation source and reference when additional clarification was required.

Status:

Referenced as supporting material.

---

# Evidence of Commands Executed

Filesystem Navigation:

```bash
cd /
ls

cd /etc
ls

cd ssh

pwd
```

File Operations:

```bash
mkdir ~/test-folder

touch ~/test-folder/file1.txt

cp ~/test-folder/file1.txt \
~/test-folder/file2.txt

mv ~/test-folder/file2.txt \
~/test-folder/file2-moved.txt

rm ~/test-folder/file1.txt
```

Help and Documentation:

```bash
man ls

man cp

ls --help

cp --help
```

Pipes and Redirection:

```bash
ls /etc | grep ssh > ~/day4.txt

cat ~/day4.txt
```

---

# Skills Gained

By the completion of this phase I can:

* Navigate Linux filesystems confidently
* Understand absolute and relative paths
* Create directories from the terminal
* Create files from the terminal
* Copy files
* Move files
* Rename files
* Delete files safely
* Read Linux manual pages
* Use built-in help systems
* Use pipes and output redirection
* Work effectively inside a remote Linux environment using SSH

---

# Reflection

This phase focused on practical Linux command-line usage rather than memorization.

All exercises were completed through SSH on a Kali Linux environment. Commands from both the Linux Command Line book and the TCM Security course were executed manually to reinforce understanding through repetition and experimentation.

Key outcomes:

* Improved terminal confidence
* Better understanding of Linux filesystem structure
* Practical experience managing files and directories
* Familiarity with Linux documentation tools
* First exposure to command chaining, filtering, and output redirection
* Increased comfort operating in a remote Linux environment

These skills establish the foundation for future work involving:

* AWS EC2
* Linux administration
* Cloud engineering
* Cloud security
* Security operations
* Incident response
* Penetration testing

---

# Next Steps

Week 2 Focus:

* Linux permissions
* Users and groups
* grep
* find
* Process management
* Networking fundamentals
* Continued Git and GitHub workflow development

---

**Phase Status:** Completed ✅

**Repository Updated:** Yes

**Ready for Week 2:** Yes
