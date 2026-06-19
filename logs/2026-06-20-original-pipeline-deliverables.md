# 2026-06-20 Original Pipeline Deliverables

## Objective

Create and analyze three original Linux pipelines.

---

## Pipeline 1

```bash
ls -la | grep ".md"
```

Purpose:

Display only Markdown files from the current directory.

Observation:

The pipeline filtered the output of `ls -la` and returned files ending with `.md`.

---

## Pipeline 2

```bash
ps aux | grep kali
```

Purpose:

Display running processes associated with the user `kali`.

Observation:

The pipeline filtered process listings and displayed processes owned by the user.

---

## Pipeline 3

```bash
cat /etc/passwd | wc -l
```

Purpose:

Count the number of lines in `/etc/passwd`.

Observation:

The pipeline passed file contents into `wc` and returned the total line count.

---

## Concepts Reinforced

* Pipes (`|`)
* Command chaining
* Text filtering
* Process inspection
* Output counting

## Summary

This exercise demonstrated how multiple Linux commands can be chained together using pipelines to filter, analyze, and transform data efficiently from the command line.
