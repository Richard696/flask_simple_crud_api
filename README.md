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
or terminal (for Mac and Linux user). Then, open the commandline or terminal and change
the directory to the root folder of this project then run `pip install` to install
neccessary dependency as stated in `requirements.txt`.

### Database

Create an account in [Mongodb Atlas](https://www.mongodb.com/), then create a free
database in the website. The landing page of the Mongo Atlas is shown as below.
![Mongo Atlas landing page](./assets/mongo-atlas-landing-page.png)

## Unit Testing

The test case are locate in `test` folder. The command to run the test is `python -m unittest --buffer`.
Sample output:

```bash
user@host:~$ python -m unittest --buffer
...
----------------------------------------------------------------------
Ran 3 tests in 1.209s

OK
```

## API Documentation

The documentation for this api can be found on https://documenter.getpostman.com/view/9794957/TzJoDfYs.

## Notes

The URI in the `config/conf.py` is just an example, do change it to the database that you are using currently.
