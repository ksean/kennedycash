KennedyCash
---

Digitize, organize, and analyze your money.


## Requirements

Python >= 3.4.8

PyEnv >= 1.2.2

Django >= 2.0.3

React >= 16.2.0


## Installation and Usage

One time database setup:

```
cd backend
python manage.py makemigrations kennedycash
python manage.py migrate kennedycash
```

### API

Install the `pyenv` dependency. Then `cd` into the `backend` directory and run the local server.

```
cd backend
pip install -r requirements.txt
python manage.py runserver
```

API available at [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api).

### UI

Make sure React is already installed globally. If not `npm install -g create-react-app`.

```
cd frontend
$ npm install
$ npm start
```

Navigate to [http://localhost:3000/](http://localhost:3000/).

## License

[The Unlicense](http://unlicense.org/)