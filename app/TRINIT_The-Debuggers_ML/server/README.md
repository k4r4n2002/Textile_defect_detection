# Tri-NIT - The Debuggers - ML01 - Server

## Setup

- Set up a virtual environment

```bash
virtualenv -p python3 env
source ./venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Copy .env.example to .env and set the variables in environment.

```bash
cp .env.example .env
```

- Start the server

```bash
python main.py
```

Server will be started at [http://0.0.0.0:5000](http://0.0.0.0:5000)
