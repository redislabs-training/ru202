# RU202 Redis Streams

This repository contains the source code for the [RU202 Redis Streams Course](https://university.redis.com/courses/ru202/) at [Redis University](https://university.redis.com/). 

## Reporting Errata

Spotted an error in a text segment, image or video transcript?  Please [report an issue](https://github.com/redislabs-training/ru202/issues). We also welcome [pull requests](https://github.com/redislabs-training/ru202/pulls) with your suggestions.  The files for each text segment, image, non-graded quiz question and video transcript can be found in the `courseware` folder in this repository.

## Environment Setup

To get the most from this course and follow along with the sample code, you'll need to have access to a Redis Stack 7 server and have Python 3 installed.

### Prerequisites

In order to run the sample code, you will need:

* [Python 3](https://www.python.org/downloads/).
* Ability to run the `pip` command for Python 3.
* Access to a local or remote installation of [Redis Stack](https://redis.io/docs/getting-started/install-stack/). (local preferred).  We've provided a Docker Compose file to make this easy for you.  If you don't want to use Docker, [follow the instructions here](https://redis.io/docs/getting-started/install-stack/) to install Redis Stack using a package manager.

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

#### Starting Redis Stack (Docker)

If you're using Docker to Run Redis Stack, start it like this:

```bash
docker-compose up -d
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

Redis Stack will persist your data to an append only file in the `redisdata` folder, so it will be there the next time you start the container.  To erase it, use `rm -rf redisdata`.

### Configuration

By default, the code will assume that Redis Stack is available on `localhost` at port `6379`.  If your Redis Stack instance is running elsewhere, you will need to set the `REDIS_HOST` and/or `REDIS_PORT` environment variables.  For example, here's how to configure these to connect to Redis Stack on `myredishostname` port `6380`:

```bash
export REDIS_HOST=myredishostname
export REDIS_PORT=6380
```

If your Redis Stack instance requires a password to connect, also set the `REDIS_PASSWORD` environment variable:

```bash
export REDIS_PASSWORD=secret123
```

If you need to supply a user name when connecting, you should set the `REDIS_USER` environment variable:

```bash
export REDIS_USER=student
```

### Test Your Connection to Redis Stack

To test your Redis Stack connection and Python environment, run:

```bash
python test_connection.py
```

If this command outputs `True`, then you are setup and ready to run the example code as described in the course materials.

### Running the Example Code

Throughout the course, you will be asked to run the example code for the various exercises.  Some of these require you to open multiple shell/terminal sessions.  Don't forget to start your Python virtual environment in each new shell session.  If your Redis Stack instance is not running on `localhost:6379` then you'll also need to set the environment variables `REDIS_HOST`, `REDIS_PORT` and optionally `REDIS_USER` and `REDIS_PASSWORD`.

### Optional (but recommended!): RedisInsight

RedisInsight is a graphical management tool for Redis.  It allows you to view and edit data in Redis, and contains specialized views for looking at the contents of Redis Streams.

You don't need to install or use RedisInsight to be successful with this course, but we'd recommend you give it a try.

[Download RedisInsight here](https://redis.com/redis-enterprise/redis-insight/) (it's free!).  Once installed, add a new Redis database and supply the hostname, port and optionally username and password for the Redis instance that you're using for this course (this will usually be `localhost`, `6379` and no username or password).

If you're using the Docker Compose file provided with this course, you can also try out a limited version of RedisInsight in your browser by visiting `http://localhost:8081` - this version can only connect to the Redis Stack instance in the Docker container.  Use the Desktop version of RedisInsight to manage connections to multiple remote and/or local Redis instances.  

## Questions?

If you have questions about this repository, you can chat with our teaching assistants on the [Redis University Discord Server](https://discord.gg/3wseBzw).

## Subscribe to our YouTube Channel / Follow us on Twitch

We'd love for you to [check out our YouTube channel](https://youtube.com/redisinc), and subscribe if you want to see more Redis videos!  We also stream regularly on our [Twitch.tv channel](https://www.twitch.tv/redisinc) - follow us to be notified when we're live and [check out our events schedule on the Redis Developer site](https://developer.redis.com/redis-live/).
