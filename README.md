# Betao AB Backend Interview

## Contents

1. [Service Architecture](#service-architecture)
2. [Prerequisites](#prerequisites)
3. [Running The Service](#running-the-service)
4. [Cleaning Up](#cleaning-up)
5. [Cases Tested](#cases-tested)
6. [Built With](#built-with)

## Service Architecture

![Service Architecture](https://github.com/MitraThakker/betaoab-back-end-interview/blob/main/assets/ServiceArchitecture.jpg)

## Prerequisites

Prerequisites needed to run this project locally:
1. Docker and Docker Compose (can be downloaded from the [official site](https://hub.docker.com/))
2. A clone (or zip) of this repository
3. A stable internet connection for a hassle-free build :)

## Running The Service

1. Start Docker (if not already running).

2. Open Terminal and go to the root directory of the project.

```bash
cd /path/to/betaoab-back-end-interview
```

3. Build and run the service.

```bash
docker-compose up -d
```

4. Check the logs to verify if the server is running.

```bash
docker-compose logs -f
```

5. The endpoints should be accessible on `0.0.0.0:5005/` locally.  Test it using an HTTP client like `curl` command on the terminal or by using a tool like Postman.

## Cleaning Up

1. Stop the Docker container.

```bash
docker-compose down
```

2. Remove all stopped containers.

```bash
docker system prune
```

OR

2. Remove a specific container.

```bash
docker container rm CONTAINER_ID
```

3. Remove the docker image.
```bash
docker image rm IMAGE_ID
```

## Cases Tested

1. Create link - success

```
URL: 0.0.0.0:5005/api/links
METHOD: POST

Request:
{
  "url": "https://yahoo.com"
}

Response: 200 - Ok
{
    "link_id": 1
}
```

2. Create link - failure

```
URL: 0.0.0.0:5005/api/links
METHOD: POST

Request:
{
  "url": "https://yahoo"
}

Response: 400 - Bad Request
{
    "error": "invalid URL"
}
```

3. List all links

```
URL: 0.0.0.0:5005/api/links
METHOD: GET

Request: NA

Response: 200 - Ok
[
    {
        "created_at": "2024-02-05 01:24:38.246443",
        "downvotes": 0,
        "id": 1,
        "score": 0,
        "upvotes": 0,
        "url": "https://yahoo.com"
    }
]
```

4. Get link details by ID - success

```
URL: 0.0.0.0:5005/api/links/1
METHOD: GET

Request: NA

Response: 200 - Ok
{
    "created_at": "2024-02-05 01:24:38.246443",
    "downvotes": 0,
    "id": 1,
    "score": 0,
    "upvotes": 0,
    "url": "https://yahoo.com"
}
```

5. Get link details by ID - failure

```
URL: 0.0.0.0:5005/api/links/2
METHOD: GET

Request: NA

Response: 404 - Not Found
{
    "error": "link with id 2 not found"
}
```

6. Upvote link - success

```
URL: 0.0.0.0:5005/api/links/1/upvote
METHOD: POST

Request: NA

Response: 200 - Ok
{
    "created_at": "2024-02-05 01:24:38.246443",
    "downvotes": 0,
    "id": 1,
    "score": 1,
    "upvotes": 1,
    "url": "https://yahoo.com"
}
```

7. Upvote link - failure

```
URL: 0.0.0.0:5005/api/links/2/upvote
METHOD: POST

Request: NA

Response: 404 - Not Found
{
    "error": "link with id 2 not found"
}
```

8. Downvote link - success

```
URL: 0.0.0.0:5005/api/links/1/downvote
METHOD: POST

Request: NA

Response: 200 - Ok
{
    "created_at": "2024-02-05 01:24:38.246443",
    "downvotes": 1,
    "id": 1,
    "score": 0,
    "upvotes": 1,
    "url": "https://yahoo.com"
}
```

9. Downvote link - failure

```
URL: 0.0.0.0:5005/api/links/2/downvote
METHOD: POST

Request: NA

Response: 404 - Not Found
{
    "error": "link with id 2 not found"
}
```

## Built With

* Language: Python 3.11
* Web Framework: Flask
* Deployment: Docker
* And... Lots of love! :)
