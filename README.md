# Tracking system Using Flask

### Features

REST API by Flask , Tracking system implementation

# How to install

Use powershell or cmd and type by order, please see below.

- `git clone https://gitlab.com/kantinanm/imagency.git`
- `cd imagency`
  If you are running Python version below 3.4, You must execute command below:
- `pip install virtualenv`
  If you are running Python 3.4+, you can use the venv module baked into Python:
- `python -m venv env` for create [env] in root project directory
- `source env/bin/activate` for activate environment  
  or Window using
- `.\env\Scripts\activate` for activate environment
- `pip install -r requirements.txt`

# Ext. pip install (Windows)

for python-ldap. please download .whl from https://github.com/cgohlke/python-ldap-build/releases

- `py.exe -3.10 -m pip install python_ldap-3.4.4-cp310-cp310-win_amd64.whl`
  or
- `pip install python_ldap-3.4.4-cp310-cp310-win_amd64.whl`

# Change requirements.txt for deployment

Linux or Mac

- `python-ldap==3.4.4`

Windows

- `python-ldap @ file:///{path}taskmgnt/python_ldap-3.4.4-cp310-cp310-win_amd64.whl#sha256=58f45fc4fd0eee441d36bf868dc89b84c183cfb527179bf72b40ed9cfd50db6b`

# How to run

- `python -m flask run --port 5000 ` execute command in root directory
- `python -m flask run --port 5000 --debug ` execute command (debug mode)

# How to generate secret key

- `python -c "import secrets; print(secrets.token_hex())"`

# db migration init command {Project folder}

- `flask db init`
- `flask db migrate -m "initial migration"`
- `flask db upgrade`

# migration executor command

- `flask db upgrade`

# step of create or alter table , in development mode

- `flask db stamp head`
- Edit model file, corresponding tables that you want to change.
- `flask db migrate -m "alter column, change in users table"`
- `flask db upgrade`
- `flask db stamp head`

# Other

- `flask db heads`
- `flask db show`

# Sample run

- `flask run`

# How to test

- http://localhost:5000/
- http://localhost:5000/tab
- http://localhost:5000/qr
- http://localhost:5000/home
- http://localhost:5000/about
- http://localhost:5000/api/v1/generate
- http://localhost:5000/api/v1/info

# How to deactivate venv

- `deactivate` execute command in root directory

# .ENV

- `MY_APP="Imagency"`
- `FILL_COLOR="black" `
- `BACK_COLOR="GreenYellow"`
- `BOX_SIZE=8`
- `BORDER=4`
- `QR_VERSION=3`
- `SECRET_KEY="xxx"`
- `JWT_SECRET_KEY="xxx"`

# How to run gunicorn

- `gunicorn --bind 0.0.0.0:5000 wsgi:app` execute command in root directory gunicorn (UNIX)
- `waitress-serve --listen=0.0.0.0:5000 wsgi:app` execute command for WINDOWS
