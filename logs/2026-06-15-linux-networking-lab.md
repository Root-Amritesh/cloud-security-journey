# Linux & Network Reconnaissance Lab Report

**Date:** 15 June 2026

## Objective

Gain hands-on experience with Linux command-line operations, Bash scripting, text processing, file permissions, network host discovery, and introductory network reconnaissance using Kali Linux.

---

## Activities Performed

### 1. Network Connectivity Testing

Used the `ping` command to verify communication with devices on the local network.

Commands practiced:

```bash
ping <target> -c 1
```

Concepts learned:

* ICMP echo requests and replies
* Packet transmission statistics
* Response time analysis
* Basic network reachability testing

---

### 2. Output Redirection

Saved command output into files using output redirection.

Commands practiced:

```bash
ping <target> -c 1 > ip.txt
```

Concepts learned:

* Standard output (stdout)
* File redirection using `>`
* Capturing command results for later processing

---

### 3. Text Processing and Data Extraction

Processed command output using Linux text-manipulation utilities.

Commands practiced:

```bash
grep
cut
tr
```

Pipeline used:

```bash
cat ip.txt | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"
```

Concepts learned:

* Pattern matching
* Field extraction
* Character removal
* Command chaining with pipes

---

### 4. Bash Scripting

Created a Bash script to automate network host discovery.

Script functionality:

* Accept subnet input from the user
* Perform host discovery across the subnet
* Display responsive hosts

Concepts learned:

* Script execution
* Script arguments
* Loops
* Conditional statements
* Automation fundamentals

---

### 5. Linux Permissions Management

Encountered and resolved execution permission issues.

Commands used:

```bash
chmod +x ipsweep.sh
```

Concepts learned:

* File permissions
* Execute bit
* Script execution requirements

---

### 6. Script Debugging

Resolved several scripting and command-line errors.

Issues encountered:

* Incorrect interpreter declaration
* Syntax errors involving conditional blocks
* Command typos
* Case-sensitive command mistakes

Concepts learned:

* Bash troubleshooting
* Error interpretation
* Debugging workflow
* Importance of syntax accuracy

---

### 7. Host Discovery Automation

Executed the completed Bash script to identify active hosts on the local network.

Concepts learned:

* Network enumeration
* Automated scanning
* Data collection for reconnaissance activities

---

### 8. Nmap Installation and Verification

Updated and verified the Nmap installation.

Commands used:

```bash
sudo apt update
sudo apt install nmap
nmap --version
```

Concepts learned:

* Package management
* Tool verification
* Security tool installation

---

### 9. Automated Network Scanning

Performed automated Nmap scans against discovered hosts.

Commands practiced:

```bash
for ip in $(cat ip.txt); do nmap $ip; done
```

Concepts learned:

* Bash loops
* Automation of repetitive tasks
* Network reconnaissance workflows

---

### 10. Service Enumeration

Identified open ports and services running on discovered devices.

Services observed included:

* HTTP
* HTTPS
* Microsoft RPC
* NetBIOS
* SMB
* Remote management services

Concepts learned:

* Port scanning fundamentals
* Service identification
* Attack surface awareness
* Reconnaissance methodology

---

## Skills Practiced

### Linux

* File management
* Permissions management
* Command pipelines
* Output redirection
* Package management

### Bash

* Script creation
* Variables
* Arguments
* Loops
* Conditionals
* Troubleshooting

### Networking

* ICMP
* Host discovery
* Port scanning
* Service enumeration
* Network reconnaissance

---

## Key Takeaways

* Linux commands become significantly more powerful when combined through pipes.
* Small syntax mistakes can completely break a script.
* File permissions are critical for executable scripts.
* Automation reduces repetitive manual work.
* Reconnaissance is a structured process involving discovery, validation, and enumeration.
* Troubleshooting and debugging are essential parts of cybersecurity work.

---

## Outcome

Successfully completed a hands-on Linux and networking lab involving command-line operations, Bash scripting, host discovery, automated scanning, service enumeration, and troubleshooting. Demonstrated the ability to build, debug, and execute scripts while collecting and analyzing network information using Kali Linux and Nmap.
