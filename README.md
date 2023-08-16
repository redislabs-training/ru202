# RU202 Redis Streams

This repository contains the source code for the [RU202 Redis Streams Course](https://university.redis.com/courses/ru202/) at [Redis University](https://university.redis.com/). 

## Reporting Errata

Spotted an error in a text segment, image or video transcript?  Please [report an issue](https://github.com/redislabs-training/ru202/issues). We also welcome [pull requests](https://github.com/redislabs-training/ru202/pulls) with your suggestions.  The files for each text segment, image, non-graded quiz question and video transcript can be found in the `courseware` folder in this repository.

## Environment Setup

To get the most from this course and follow along with the sample code, you'll need to have access to a Redis 7 server and have Python 3 installed.

### Prerequisites

In order to run the sample code, you will need:

* [Python 3](https://www.python.org/downloads/).
* Ability to run the `pip` command for Python 3.
* Access to a local or remote installation of [Redis](https://redis.io/download) version 6.2 or newer (local preferred).  We've provided a Docker Compose file to make this easy for you.  If you don't want to use Docker, [follow the instructions here](https://redis.io/docs/getting-started/) to install Redis using a package manager.

If you're using Windows, check out the following resources for help with running Redis:

* [Video - Installing Redis on Windows 10](https://www.youtube.com/watch?v=_nFwPTHOMIY)
* [Redis Blog - Running Redis on Windows 10](https://redis.com/blog/redis-on-windows-10/)
* [Microsoft - Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

### Setup

Execute these commands in your shell to clone the repository, create a Python virtual environment and install the depdendencies:

```bash
git clone https://github.com/redislabs-training/ru202.git
cd ru202
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

**Note:** Ensure you activate your virtual environment in each new shell/terminal session before running any of the sample code.

#### Starting Redis (Docker)

If you're using Docker to Run Redis, start it like this:

```bash
docker-compose up  -d
```

You can now run `redis-cli` to connect to Redis as follows:

```bash
docker exec -it redis_ru202 redis-cli
```

Type `quit` to exit `redis-cli` back to your shell.

When you are done with the container, you can shut it down like this:

```bash
docker-compose down
```

Redis will persist your data to an append only file in the `redisdata` folder, so it will be there the next time you start the container.  To erase it, use `rm -rf redisdata`.

#### Starting Redis (when installed by a Package Manager)

If you installed Redis using a package manager, start the Redis server if it isn't already running.  For example, if you installed Redis with the Homebrew package manager for macOS you'd start it like this:

```bash
brew services start redis
```

You can now run `redis-cli` to connect to Redis as follows:

```bash
docker exec -it redis_ru202 redis-cli
```

Type `quit` to exit `redis-cli` back to your shell.

When you are done with Redis, you can optionally turn off the server.  For example if Redis was installed with the Homebrew package manager for macOS you'd stop the server like this:

```bash
brew services stop redis
```

### Configuration

By default, the code will assume that Redis is available on `localhost` at port `6379`.  If your Redis instance is running elsewhere, you will need to set the `REDIS_HOST` and/or `REDIS_PORT` environment variables.  For example, here's how to configure these to connect to Redis on `myredishostname` port `6380`:

```bash
export REDIS_HOST=myredishostname
export REDIS_PORT=6380
```

If your Redis instance requires a password to connect, also set the `REDIS_PASSWORD` environment variable:

```bash
export REDIS_PASSWORD=secret123
```

If you are using Redis 6 or 7 and need to supply a user name when connecting, you should set the `REDIS_USER` environment variable:

```bash
export REDIS_USER=student
```

### Test Your Connection to Redis

To test your Redis connection and Python environment, run:

```bash
python test_connection.py
```

If this command outputs `True`, then you are setup and ready to run the example code as described in the course materials.

### Running the Example Code

Throughout the course, you will be asked to run the example code for the various exercises.  Some of these require you to open multiple shell/terminal sessions.  Don't forget to start your Python virtual environment in each new shell session.  You'll also need to set the environment variables `REDIS_HOST`, `REDIS_PORT` and optionally `REDIS_USER` and `REDIS_PASSWORD` if your Redis instance is not running on `localhost:6379`.

### Optional (but recommended!): RedisInsight

RedisInsight is a graphical management tool for Redis.  It allows you to view and edit data in Redis, and contains specialized views for looking at the contents of Redis Streams.

You don't need to install or use RedisInsight to be successful with this course, but we'd recommend you give it a try.

[Download RedisInsight here](https://redis.com/redis-enterprise/redis-insight/) (it's free!).  Once installed, add a new Redis database and supply the hostname, port and optionally password for the Redis instance that you're using for this course (this will usually be `localhost`, `6379` and no password).

## Questions?

If you have questions about this repository, you can chat with our teaching assistants on the [Redis University Discord Server](https://discord.gg/3wseBzw).

## Subscribe to our YouTube Channel / Follow us on Twitch

We'd love for you to [check out our YouTube channel](https://youtube.com/redisinc), and subscribe if you want to see more Redis videos!  We also stream regularly on our [Twitch.tv channel](https://www.twitch.tv/redisinc) - follow us to be notified when we're live and [check out our events schedule on the Redis Developer site](https://developer.redis.com/redis-live/).
