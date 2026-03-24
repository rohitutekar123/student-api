## Overview

## Tech Stack

Python (Flask), Docker, Makefile

---

## Project Structure

```
student-api/
app.py
requirements.txt
Dockerfile
Makefile
README.md
```

---

## Assignment 1 – REST API

Endpoints:

* GET /health
* POST /students
* GET /students
* GET /students/<id>
* PUT /students/<id>
* DELETE /students/<id>

Example:

```
curl -X POST http://localhost:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "Rohit"}'
```

---

## Assignment 2 – Docker

Build image:

```
docker build -t rohitutekar123/student-api:latest .
```

Run container:

```
docker run -p 5000:5000 rohitutekar123/student-api:latest
```

Test:

```
curl http://localhost:5000/health
```

---

## Assignment 3 – One-Click Setup

Run:

```
make run
```

Stop:

```
make stop
```

Restart:

```
make restart
```

Logs:

```
make logs
```

---

## Notes

* Uses in-memory storage
* No database required
* Data resets after restart

---

## Docker Image

rohitutekar123/student-api:latest
