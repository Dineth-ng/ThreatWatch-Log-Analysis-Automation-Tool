:::writing{variant="document" id="48291"}
### ThreatWatch - Log Analysis & Security Monitoring Tool

## Overview

ThreatWatch is a lightweight Python-based log analysis tool designed for SOC (Security Operations Center) practice and cybersecurity learning.

It parses Apache, Nginx, and firewall logs to detect common attack patterns such as:

🔐 Brute Force Login Attempts
📂 Directory Traversal Attacks
🌐 Port Scanning Activity

The tool generates structured JSON security alerts with severity levels for easier monitoring and automation.

For example, raw logs might look like this:
```text
192.168.1.10 - - [30/May/2026:13:45:00] "POST /login HTTP/1.1" 401 - (Repeated multiple times)
192.168.1.20 - - [30/May/2026:13:46:12] "GET /../../etc/passwd HTTP/1.1" 400 -
192.168.1.30 - - [30/May/2026:13:47:05] "CONNECT 192.168.1.30:22" 200 -