# Events app in Flask
Simple events app made with Flask in Python

#### Check it out on Heroku!
https://flask-events.herokuapp.com


### :closed_lock_with_key: Technology stack
-------------

| Name | Version |
| :--: | :---: |
| [Python](https://www.python.org/) | 3.5.2 |
| [Flask](http://flask.pocoo.org/) | 0.12.2 |
| [Sqlite (development)](https://www.sqlite.org/) | 3.11.0 |
| [PostgreSQL (production)](https://www.sqlite.org/) | 9.5.7 |

### :book: Setup locally
-------------
1.  clone repository,
2.  install [virtualenv](http://flask.pocoo.org/docs/0.10/installation/),
2.  `cd path/to/repo`,
3.  `virtualenv venv -p /usr/bin/python3.5`,
4.  `. venv/bin/activate`,
5.  `pip install flask`,
6.  `python main.py`
7.  in your favourite web browser `localhost:5000`

### :information_source: Hints
-------------
If you prefer to enter `flask run` instead of `python main.py` then:

`export FLASK_APP=main.py`

If you want to restart server automatically after every change: `export FLASK_DEBUG=1`

To exit virtualenv: `deactivate`
