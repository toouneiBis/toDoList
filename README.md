# Bibliothèque Python

La version de python utilisé est : 3.8.10

## Authors 

    Louis Lemoine
    Laurent Guyraud
    Célia Giotti
    Guillaume Piol

#### Link Github

    https://github.com/toouneiBis/toDoList


### Install dependencies

Create a venv :

```sh
python -m pip install --user virtualenv # If you don't already have venv
python -m venv venv
```

Once the venv created :


```sh
docker-compose up --build -d
```

```sh
source venv/bin/activate
pip install -r requirements.txt
```

### Run tests

```sh
python -m pytest
```

### Run API

```sh
python -m flask run
```

### Use CLI

Run the API before use the CLI

```sh
python cli/main.py create "Task Title" "Task Description"
python cli/main.py list
python cli/main.py complete "Task Title"
python cli/main.py delete "Task Title"
```

### Use GUI 

Run on http://127.0.0.1:5000
