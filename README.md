# RU202 Redis Streams

This repository contains the source code for the [RU202 Redis Streams Course](https://university.redislabs.com/courses/ru202/) at [Redis University](https://university.redislabs.com/).

## Prerequisites

In order to run the sample code, you will need:

* [Python 3](https://www.python.org/downloads/)
* Ability to run the `pip` command for Python 3
* Access to a local or remote installation of [Redis](https://redis.io/download) version 5 or newer (local preferred)

## Setup

Execute these commands in your shell to clone the repository then create a Python virtual environment and install depdendencies:

```bash
$ git clone https://github.com/redislabs-training/ru202.git
$ cd ru202
$ python3 -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt
```

**Note:** Ensure you activate your virtual environment before running any of the sample code.

## Configuration

By default, the code will assume that Redis is available on `localhost` at port `6379`.  If your Redis instance is running elsewhere, you will need to set the `REDIS_HOST` and/or `REDIS_PORT` environment variables.  For example, here's how to configure these to connect to Redis on `myredishostname` port `6380`:

```bash
$ export REDIS_HOST=myredishostname
$ export REDIS_PORT=6380
```

If your Redis instance requires a password to connect, also set the `REDIS_PASSWORD` environment variable:

```bash
$ export REDIS_PASSWORD=secret123
```

If you are using Redis 6 and need to supply a user name when connecting, you should set the `REDIS_USER` environment variable:

```bash
$ export REDIS_USER=student
```

## Test Your Connection to Redis

To test your Redis connection and Python environment, run:

```bash
$ python test_connection.py
```

If this command outputs `True`, then you are setup and ready to run the example code as described in the course materials.

## Questions?

If you have questions about this repository, you can chat with our teaching assistants on the [Redis University Discord Server](https://discord.gg/3wseBzw).
