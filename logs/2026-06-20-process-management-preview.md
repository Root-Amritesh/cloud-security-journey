# 2026-06-20 Process Management Preview

## Objective

Practice basic Linux process monitoring and job control commands.

---

## Process Inspection

Command:

```bash
ps aux | grep root
```

Observation:

Displayed active processes owned by the root user. Most system services and kernel-related processes were running under root.

---

## Real-Time Monitoring

Command:

```bash
top
```

Observation:

Displayed CPU, memory, running tasks, and system load in real time. Xorg was among the highest memory-consuming processes.

---

## Background Process

Command:

```bash
sleep 100 &
```

Observation:

Started a background job and returned a job number and PID.

Example:

```text
[1] 42856
```

---

## View Active Jobs

Command:

```bash
jobs
```

Observation:

Displayed currently running background jobs.

---

## Foreground Job

Command:

```bash
fg %1
```

Observation:

Returned the background sleep process to the foreground.

The process was terminated using Ctrl+C.

---

## Job Termination

Command:

```bash
kill %1
```

Observation:

The command returned:

```text
kill: %1: no such job
```

because the process had already been terminated using Ctrl+C.

---

## CPU Usage Analysis

Command:

```bash
ps aux | sort -k3 -rn | head -10
```

Observation:

Displayed the processes with the highest CPU utilization. Xorg appeared at the top of the list.

---

## Concepts Reinforced

* Process monitoring
* Foreground and background jobs
* Job control
* Process termination
* CPU utilization analysis
* Linux multitasking

## Summary

This lab introduced Linux process management fundamentals. Commands such as `ps`, `top`, `jobs`, `fg`, and `kill` were used to inspect, control, and terminate running processes.
