# 2026-06-23 — Service Health Status Checker

## Objective

Build a Bash script capable of checking whether a Linux service is currently running and displaying a clean, human-readable status message.

This task serves as Script 2 of 4 for Gate 1 preparation and introduces the concept of conditional execution using the Bash `if` statement.

---

## Deliverable

### service_check.sh

```bash
#!/bin/bash

# Script 2: Check if a service is running
# Usage: ./service_check.sh sshd

SERVICE=${1:-"sshd"}

if systemctl is-active --quiet "$SERVICE"; then
    echo "[✓ UP]   $SERVICE is RUNNING"
else
    echo "[✗ DOWN] $SERVICE is NOT running"
fi
```

---

## Commands Executed

### Create Script

```bash
nano service_check.sh
```

### Make Script Executable

```bash
chmod +x service_check.sh
```

### Verify Permissions

```bash
ls -l service_check.sh
```

### Execute Script Using Default Service

```bash
./service_check.sh
```

### Execute Script With Explicit Service Name

```bash
./service_check.sh sshd
```

```bash
./service_check.sh apache2
```

### Verify Exit Code Behaviour

```bash
echo $?
```

### Investigate Service State

```bash
systemctl is-active sshd
```

```bash
systemctl status sshd
```

### Enumerate Running Services

```bash
systemctl list-units --type=service --state=running
```

---

-----------NOTES-----------

# What Was Actually Learned

At first glance this task appears to be about checking whether a Linux service is running.

In reality, the service checker is only the vehicle used to introduce several core Bash scripting concepts that will be reused throughout future automation projects.

---

## Concept 1 — Variables

The script stores information inside a variable.

```bash
SERVICE=${1:-"sshd"}
```

The variable name is:

```bash
SERVICE
```

The value stored inside the variable changes depending on the argument supplied by the user.

Example:

```bash
./service_check.sh nginx
```

Results in:

```bash
SERVICE=nginx
```

Variables allow scripts to reuse values without repeatedly typing them.

---

## Concept 2 — Command-Line Arguments

Arguments are values passed to a script when it is executed.

Example:

```bash
./service_check.sh nginx
```

Bash automatically stores:

```bash
$1 = nginx
```

Argument positions:

```bash
$1 = first argument
$2 = second argument
$3 = third argument
```

This allows a single script to work with different services.

---

## Concept 3 — Default Values

The expression:

```bash
${1:-"sshd"}
```

means:

Use the first argument if one exists.

Otherwise use:

```bash
sshd
```

Example:

```bash
./service_check.sh
```

Results in:

```bash
SERVICE=sshd
```

This prevents empty variables and allows the script to operate even when no argument is supplied.

---

## Concept 4 — Conditional Logic

The core of the script is:

```bash
if systemctl is-active --quiet "$SERVICE"; then
```

This introduces decision making.

The script can follow different execution paths depending on whether a condition succeeds or fails.

Logic:

```text
IF service is active
    print success message
ELSE
    print failure message
```

This is known as branching.

---

## Concept 5 — Exit Codes

Every Linux command returns an exit code.

Success:

```bash
0
```

Failure:

```bash
non-zero
```

Examples:

```bash
1
2
3
127
```

The Bash `if` statement checks the exit code of a command.

It does not check the visible text output.

Example:

```bash
if command; then
```

means:

```text
Did the command succeed?
```

not:

```text
What text did the command print?
```

This concept is fundamental to Bash scripting.

---

## Concept 6 — systemctl

The command:

```bash
systemctl
```

is used to interact with Linux services.

Examples:

```bash
systemctl status sshd
```

```bash
systemctl start sshd
```

```bash
systemctl stop sshd
```

```bash
systemctl restart sshd
```

For this task we specifically used:

```bash
systemctl is-active
```

which checks whether a service is currently active.

---

## Concept 7 — The --quiet Flag

Without:

```bash
systemctl is-active sshd
```

Output:

```bash
active
```

With:

```bash
systemctl is-active --quiet sshd
```

Output:

```text
nothing
```

The command becomes silent.

Only the exit code remains.

This allows the script to generate its own custom output.

---

## Concept 8 — Script Permissions

A Bash script cannot be executed simply because it exists.

Linux requires execute permissions.

Before:

```bash
-rw-r--r--
```

After:

```bash
chmod +x service_check.sh
```

Permissions become:

```bash
-rwxr-xr-x
```

The execute bit allows Linux to run the file as a program.

---

## Concept 9 — IF / THEN / ELSE / FI Structure

General syntax:

```bash
if condition; then
    commands
else
    commands
fi
```

Components:

```bash
if
```

Starts the conditional block.

```bash
then
```

Runs when the condition succeeds.

```bash
else
```

Runs when the condition fails.

```bash
fi
```

Ends the conditional block.

A simple way to remember:

```text
if = start
fi = finish
```

---

## Execution Flow

User executes:

```bash
./service_check.sh sshd
```

Bash stores:

```bash
$1 = sshd
```

Variable becomes:

```bash
SERVICE=sshd
```

The command executes:

```bash
systemctl is-active --quiet sshd
```

Bash reads the exit code.

If the exit code equals:

```bash
0
```

Output:

```bash
[✓ UP] sshd is RUNNING
```

Otherwise:

```bash
[✗ DOWN] sshd is NOT running
```

---

## Learning Outcome

Successfully created and tested a Bash script that checks service status using conditional logic.

Concepts mastered:

* Variables
* Command-line arguments
* Default values
* Conditional statements
* Exit codes
* systemctl
* Script permissions
* User-friendly output formatting

This is the first Bash script in the roadmap that introduces true decision-making logic and serves as the foundation for future automation tasks.

-----------END NOTES-----------

---

## Result

The service health checker was successfully created, executed, and tested against multiple services.

The script correctly evaluates service state and displays customized output based on command success or failure.

This task completed Script 2 of 4 for Gate 1 preparation.

---

## Git Commands

```bash
git add .
git commit -m "feat: service_check.sh - health status"
git push
```
