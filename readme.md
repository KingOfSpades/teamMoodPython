---
author: "Christian Benstein"
title: "Setup and use this repo"
---

This repository contains code and documentation to get a flask instance with bootstrap running. This can be first run locally and the be packaged in to a dockercontainer.

# Running locally

This is easy:

1. Clone the repo
2. Before entering the folder, create a virutal env with python:
    ```bash
    $ python3 -m venv FOLDER
    ```
3. Activate the `venv` and install the dependancys:
    ```bash
    $ cd FOLDER
    $ source bin/activate
    $ pip install -r requirements.txt
    ```
3. Finally, start the application:
    ```bash
    $ flask run
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```

## Starting flask with auto-reload

To run `flask` with the automatic reload on file change, use:

```bash
$ flask run --debugger --reload
```

# Building a docker image

This is done by using `docker build`:

1. Run `docker build` to build the image:
    ```bash
    $ docker build -t teammood
    ```
2. Run the image:
    ```bash
    $ docker run -d --name teamMoodApp -p 5001:5000 teammood
    ```
3. Visit the instance on http://127.0.0.1:5001

## Stopping and deleting the image

To stop and remove the docker container, run:

```bash
docker stop teamMoodApp && docker rm teamMoodApp
teamMoodApp
teamMoodApp
```