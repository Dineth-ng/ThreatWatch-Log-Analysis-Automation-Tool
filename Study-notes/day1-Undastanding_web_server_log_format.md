# Day 1: Phase 1 – Foundations

## Understand Web Server Log Formats

### What is a Web Server Log File?

A web server log is a text document that contains a record of all activity related to a specific web server over a defined period.

The web server gathers data automatically and constantly to provide administrators with insight into how and when a server is used.

Most web servers generate a log file in the **Common Log Format (CLF)** for every HTTP request.

---

# Common Log Format

A typical configuration for the access log might look as follows:

```apache
LogFormat "%h %l %u %t \"%r\" %>s %b" common
CustomLog logs/access_log common
```

Example log entry:

```text
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
```

## Log Entry Breakdown

### 1. Client IP Address (%h)

```text
127.0.0.1
```

**(%h)** – This is the IP address of the client (remote host) that made the request to the server.

---

### 2. Remote Log Name (%l)

```text
-
```

**(%l)** – The hyphen (`-`) indicates that the requested information is not available.

In this case, the unavailable information is the RFC 1413 identity of the client determined by **ident** on the client’s machine.

---

### 3. Authenticated User (%u)

```text
frank
```

**(%u)** – This is the user ID of the person requesting the document, as determined by HTTP authentication.

The same value is typically provided to CGI scripts in the `REMOTE_USER` environment variable.

> If the status code for the request is **401**, this value should not be trusted because the user is not yet authenticated.

---

### 4. Timestamp (%t)

```text
[10/Oct/2000:13:55:36 -0700]
```

**(%t)** – The time the request was received.

Format:

```text
day/month/year:hour:minute:second zone
```

Components:

```text
day    = 2 digits
month  = 3 letters
year   = 4 digits
hour   = 2 digits
minute = 2 digits
second = 2 digits
zone   = (+ or -) 4 digits
```

---

### 5. Request Line (%r)

```text
"GET /apache_pb.gif HTTP/1.0"
```

The request line from the client is enclosed in double quotes.

Information included:

- **Method:** GET
- **Resource Requested:** `/apache_pb.gif`
- **Protocol:** HTTP/1.0

It is also possible to log parts of the request line separately.

Example:

```apache
"%m %U%q %H"
```

This logs:

- Method
- Path
- Query String
- Protocol

---

### 6. Status Code (%>s)

```text
200
```

This is the status code returned by the server.

Status code categories:

| Code Range | Meaning |
|------------|----------|
| 2xx | Successful response |
| 3xx | Redirection |
| 4xx | Client error |
| 5xx | Server error |

Examples:

- **200** → OK
- **301** → Moved Permanently
- **404** → Not Found
- **500** → Internal Server Error

---

### 7. Response Size (%b)

```text
2326
```

This indicates the size of the object returned to the client, excluding response headers.

If no content was returned, the value will be:

```text
-
```

To log `0` instead of `-`, use:

```apache
%B
```

---

# Combined Log Format

Another commonly used format is the **Combined Log Format**.

Configuration:

```apache
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"" combined
CustomLog logs/access_log combined
```

Example:

```text
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"
```

The Combined Log Format is identical to the Common Log Format but includes two additional fields.

---

## Additional Field 1: Referer (%{Referer}i)

```text
"http://www.example.com/start.html"
```

**(%{Referer}i)** – The HTTP Referer header.

This indicates the page from which the client was referred.

Example:

If the image `/apache_pb.gif` was requested from a webpage, the Referer shows that webpage.

---

## Additional Field 2: User-Agent (%{User-agent}i)

```text
"Mozilla/4.08 [en] (Win98; I ;Nav)"
```

**(%{User-agent}i)** – The HTTP User-Agent header.

This provides identifying information about the client browser or application making the request.

Examples:

- Mozilla Firefox
- Google Chrome
- Microsoft Edge
- Curl
- Python Requests

---

# Summary

| Field | Description |
|---------|------------|
| %h | Client IP Address |
| %l | Remote Log Name |
| %u | Authenticated User |
| %t | Timestamp |
| %r | Request Line |
| %>s | HTTP Status Code |
| %b | Response Size |
| %{Referer}i | Referring Page |
| %{User-agent}i | Client Browser/Application |

### Example Combined Log Entry

```text
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"
```

This single line tells us:

- Who made the request
- When the request occurred
- What resource was requested
- Which protocol was used
- Whether the request succeeded
- How much data was returned
- Which page referred the user
- Which browser/application made the request