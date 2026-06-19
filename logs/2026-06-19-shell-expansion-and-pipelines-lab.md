# 2026-06-19 Shell Expansion and Pipelines Lab

## Objective

Practice shell expansion, environment variables, command substitution, variables, file creation, and Linux pipelines using common text-processing utilities.

---

## Commands Executed

### Shell Expansion

```bash
echo ~
```

Output:

```text
/home/kali
```

Observation:

* `~` expands to the current user's home directory.
* The shell performs this expansion before executing the command.

---

### Environment Variables

```bash
echo $HOME
```

Output:

```text
/home/kali
```

Observation:

* `$HOME` stores the path to the current user's home directory.
* The `$` symbol retrieves the value of a variable.

---

### Command Substitution

```bash
echo $(date)
```

Output:

```text
Fri Jun 19 03:45:24 PM EDT 2026
```

Observation:

* `$(command)` executes a command and substitutes its output into the current command.

---

### Variable Assignment

```bash
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
echo $TIMESTAMP
```

Output:

```text
20260619_154652
```

Observation:

* Stored the current date and time inside a variable.
* Useful for generating unique filenames and log entries.

---

### Dynamic File Creation

```bash
mkdir -p ~/audit-output
echo "test" > ~/audit-output/run_$TIMESTAMP.txt
```

Observation:

* Created a directory if it did not already exist.
* Generated a timestamped output file using variable expansion.

---

## Pipeline Exercises

### Extract Usernames from /etc/passwd

```bash
cat /etc/passwd | cut -d: -f1
```

Observation:

* `cut` split each line using `:` as the delimiter.
* `-f1` extracted the first field.
* Result was a list of system usernames.

---

### Sort Usernames

```bash
cat /etc/passwd | cut -d: -f1 | sort
```

Observation:

* Sorted all usernames alphabetically.

---

### Count Usernames

```bash
cat /etc/passwd | cut -d: -f1 | sort | wc -l
```

Output:

```text
57
```

Observation:

* Counted the total number of user accounts present on the system.

---

### Count Unique Executables in /bin

```bash
ls /bin | sort | uniq | wc -l
```

Output:

```text
3661
```

Observation:

* Listed binaries in `/bin`.
* Removed duplicates.
* Counted total unique entries.

---

### Process Ownership Analysis

```bash
ps aux | awk '{print $1}' | sort | uniq -c | sort -rn
```

Output (Top Results):

```text
190 root
62 kali
```

Observation:

* `ps aux` listed running processes.
* `awk '{print $1}'` extracted the owner column.
* `uniq -c` counted occurrences.
* `sort -rn` displayed results from highest to lowest.
* Most running processes were owned by the `root` user.

---

## Key Concepts Learned

### Shell Expansion

```bash
~
```

Expands to the user's home directory.

---

### Environment Variables

```bash
$VARIABLE
```

Retrieves stored variable values.

---

### Command Substitution

```bash
$(command)
```

Executes a command and inserts its output.

---

### Pipelines

```bash
command1 | command2
```

Passes the output of one command as input to another.

---

### Text Processing Utilities

| Command | Purpose                                 |
| ------- | --------------------------------------- |
| cut     | Extract specific fields                 |
| sort    | Sort data alphabetically or numerically |
| uniq    | Remove or count duplicates              |
| wc      | Count lines, words, or characters       |
| awk     | Process and extract columns of text     |

---

## Summary

This lab focused on shell expansion and Linux pipelines. I practiced variable expansion, command substitution, dynamic file creation, and chaining commands together using pipes. The exercises demonstrated how small Linux utilities can be combined to filter, transform, sort, count, and analyze system information efficiently from the command line.

