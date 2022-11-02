# RU202 Redis Streams

This repository contains the source code for the [RU202 Redis Streams Course](https://university.redis.com/courses/ru202/) at [Redis University](https://university.redis.com/).  These materials can be accessed by installing them locally on your machine, or through a self-contained lab in a Docker container.

## Reporting Errata

Spotted an error in a text segment, image or video transcript?  Please report an issue here on GitHub, we also welcome pull requests with your suggestions.  The files for each text segment, image and video transcript can be found in the `courseware` folder in this repository.

## Optional Docker Environment

You access these materials through a self-contained Docker lab environment including an IDE and Redis install that we have setup for you:

```bash
$ docker run --rm --name redis-lab -p:8888:8888 redisuniversity/ru202-lab
```

Once the container is up and running, simply point your browser at `http://localhost:8888/entry.html` to access the IDE, terminal sessions and Redis.  The source code is pre-installed, and the Python environment is setup for you.

## Local Installation

You may prefer to setup an environment for this course on your local machine.

### Prerequisites

(If you are using our Docker container, skip this section).

In order to run the sample code, you will need:

* [Python 3](https://www.python.org/downloads/).
* Ability to run the `pip` command for Python 3.
* Access to a local or remote installation of [Redis](https://redis.io/download) version 5 or newer (local preferred).  We've provided a Docker Compose file to make this easy. 

If you're using Windows, check out the following resources for help with running Redis:

* [Video - Installing Redis on Windows 10](https://www.youtube.com/watch?v=_nFwPTHOMIY)
* [Redis Blog - Running Redis on Windows 10](https://redis.com/blog/redis-on-windows-10/)
* [Microsoft - Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

### Setup

(If you are using our self-contained Docker lab container that contains Redis, an IDE and the code then you can skip this section).

Execute these commands in your shell to clone the repository then create a Python virtual environment and install depdendencies:

```bash
$ git clone https://github.com/redislabs-training/ru202.git
$ cd ru202
$ python3 -m venv env
$ . env/bin/activate
$ pip install -r requirements.txt
```

**Note:** Ensure you activate your virtual environment before running any of the sample code.

If you need a local copy of Redis and have Docker installed you can start one like this:

```bash
$ docker-compose up  -d
```

You can now run `redis-cli` to connect to Redis as follows:

```bash
$ docker exec -it redis_ru202 redis-cli
```

Type `quit` to exit `redis-cli` back to your shell.

When you are done with the container, you can shut it down like this:

```bash
$ docker-compose down
```

Redis will persist your data to an append only file in the `redisdata` folder, so it will be there the next time you start the container.  To erase it, use `rm -rf redisdata`.

### Configuration

(If you are using our self-contained Docker lab container or Docker Compose then you can skip this section).

By default, the code will assume that Redis is available on `localhost` at port `6379`.  If your Redis instance is running elsewhere, you will need to set the `REDIS_HOST` and/or `REDIS_PORT` environment variables.  For example, here's how to configure these to connect to Redis on `myredishostname` port `6380`:

```bash
$ export REDIS_HOST=myredishostname
$ export REDIS_PORT=6380
```

If your Redis instance requires a password to connect, also set the `REDIS_PASSWORD` environment variable:

```bash
$ export REDIS_PASSWORD=secret123
```

If you are using Redis 6 or 7 and need to supply a user name when connecting, you should set the `REDIS_USER` environment variable:

```bash
$ export REDIS_USER=student
```

### Test Your Connection to Redis

To test your Redis connection and Python environment, run:

```bash
$ python test_connection.py
```

If this command outputs `True`, then you are setup and ready to run the example code as described in the course materials.

### Optional (but recommended!): RedisInsight

RedisInsight is a graphical management tool for Redis.  It allows you to view and edit data in Redis, and contains specialized views for looking at the contents of Redis Streams.

You don't need to install or use RedisInsight to be successful with this course, but we'd recommend you give it a try.

[Download RedisInsight here](https://redis.com/redis-enterprise/redis-insight/) (it's free!).  Once installed, add a new Redis database and supply the hostname, port and optionally password for the Redis instance that you're using for this course (this will usually be `localhost`, `6379` and no password).

## Questions?

If you have questions about this repository, you can chat with our teaching assistants on the [Redis University Discord Server](https://discord.gg/3wseBzw).

## Subscribe to our YouTube Channel / Follow us on Twitch

We'd love for you to [check out our YouTube channel](https://youtube.com/redisinc), and subscribe if you want to see more Redis videos!  We also stream regularly on our [Twitch.tv channel](https://www.twitch.tv/redisinc) - follow us to be notified when we're live and [check out our events schedule on the Redis Developer site](https://developer.redis.com/redis-live/).
