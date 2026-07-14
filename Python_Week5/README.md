# Gate 2 – Log Parser

## Overview

This project is a Python-based log parser that scans a directory for `.log` files, searches each file for security-related keywords, and generates a JSON summary of the results.

The parser checks every line in every log file for the keywords **FAILED** and **ERROR**, counts how many matching lines appear in each file, and writes the results to a `results.json` file.

---

# Why Log Parsing Matters

Modern operating systems, applications, firewalls, web servers, and cloud platforms continuously generate log files. These logs record normal activity, warnings, errors, authentication attempts, and system failures.

Security analysts rarely read thousands of log lines manually. Instead, they build automated tools that search logs for indicators of suspicious activity.

This project demonstrates that exact workflow.

The keywords **FAILED** and **ERROR** are commonly associated with events such as:

- Failed login attempts
- Authentication failures
- Database connection problems
- Application crashes
- Service failures
- System errors

Although this script searches only two keywords, the same technique scales to thousands of detection rules inside enterprise security platforms.

---

# How Security Teams Use This

Real Security Operations Centers (SOCs) use Security Information and Event Management (SIEM) platforms such as:

- Splunk
- Microsoft Sentinel
- IBM QRadar
- Google Chronicle
- Elastic Security

These systems continuously parse millions of log entries using logic very similar to this project.

The output helps analysts:

- Detect suspicious authentication failures
- Identify systems generating repeated errors
- Prioritize incident investigations
- Detect attack trends over time
- Reduce manual log analysis

This project demonstrates the fundamental concept behind automated log analysis.

---

# Why Count Per File Instead of One Total?

Imagine the parser only produced:

```
12 flagged events
```

That number alone is not useful.

Which system generated them?

Which application is failing?

Which server should be investigated first?

Instead, this parser counts each log file individually.

Example:

```json
{
    "app.log": 4,
    "auth.log": 7,
    "system.log": 0
}
```

From this report an analyst can immediately see that **auth.log** requires attention, while **system.log** currently has no detected issues.

Per-file visibility makes the results actionable.

---

# Features

- Recursively scans directories using `os.walk()`
- Reads every `.log` file
- Detects **FAILED** and **ERROR** entries
- Counts flagged lines per file
- Includes files with zero matches
- Exports results as formatted JSON
- Uses safe file handling with `with open()`

---

# Project Workflow

```
Directory
    │
    ▼
Find every .log file
    │
    ▼
Open each file
    │
    ▼
Read every line
    │
    ▼
Search for FAILED / ERROR
    │
    ▼
Count matches
    │
    ▼
Store results in dictionary
    │
    ▼
Write results.json
```

---

# Usage

Run the script:

```bash
python3 script5_gate2_logparser.py
```

When prompted:

```
Enter directory to scan:
```

Example:

```
sample_logs
```

---

# Example Output

Terminal:

```
{
    "app.log": 2,
    "auth.log": 2,
    "system.log": 0
}
```

Generated `results.json`

```json
{
    "app.log": 2,
    "auth.log": 2,
    "system.log": 0
}
```

---

# Skills Demonstrated

This project demonstrates practical use of:

- Python functions
- Dictionaries
- Loops
- Conditional statements
- File handling
- `with open()`
- `os.walk()`
- `os.path.join()`
- `json.dump()`
- JSON data serialization
- Directory traversal
- Basic log analysis

---

# Learning Outcome

This project serves as a foundation for future cybersecurity automation.

The same workflow can later be extended to:

- Parse Apache logs
- Parse Nginx logs
- Analyze Windows Event Logs
- Detect brute-force login attempts
- Build SIEM detection rules
- Create SOC automation scripts
- Build threat detection pipelines

Although simple, this project mirrors the core process used in professional log analysis tools and Security Operations Centers.
