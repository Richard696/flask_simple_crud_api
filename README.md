# Simple CRUD API Using Flask

This repo is the backend API that serve simple CRUD for user.
The API is written in Python language with Flask framework and using Mongodb
as the database.

## Setup

### Python

Make sure you have install python in your local machine.
Else please go to [python official website](https://www.python.org/)
to download the installer (for Windows and Mac user), while for Linux user
python is installed by default in the system. Then check is the python package manager `pip`
is available in your or not by running `pip -v` in commandline (for Windows User)
or terminal (for Mac and Linux user). Then, open the commandline or terminal and change the directory to the root folfer of the project. Look for `requirtement.txt` then run `pip install` to install neccessary dependency.

### Database

Create an account in [Mongodb Atlas](https://www.mongodb.com/), then create a free
database in the website. The detail guide to set up the mongodb on cloud can be
found in [How to Create a Database for Free](https://www.mongodb.com/database/free)
and [Get started with Atlas](https://docs.atlas.mongodb.com/getting-started/). The reason
of using the cloud hosted mongodb is because it save out the trouble of setup
the mongodb in the local.

### Notes

The URI in the `config/conf.py` is just an example, do change it to the database that you are using currently.
