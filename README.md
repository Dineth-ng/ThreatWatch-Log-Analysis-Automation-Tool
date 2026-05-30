# ThreatWatch - Log Analysis Automation Tool

---

##  Project Overview

In a production environment, a company website or server receives thousands of requests every day. Manually sorting through these logs to find malicious activity is incredibly time-consuming and inefficient. 

For example, raw logs might look like this:
```text
192.168.1.10 - - [30/May/2026:13:45:00] "POST /login HTTP/1.1" 401 - (Repeated multiple times)
192.168.1.20 - - [30/May/2026:13:46:12] "GET /../../etc/passwd HTTP/1.1" 400 -
192.168.1.30 - - [30/May/2026:13:47:05] "CONNECT 192.168.1.30:22" 200 -