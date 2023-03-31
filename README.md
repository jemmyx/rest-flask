542 ls -ls
543 which python
544 python --version
545 pip install --upgrade pip
546 pip freeze
547 pip freeze > requirements.txt
548 ls -ls
549 less requirements.txt
550 pip uninstall -r requirements.txt -y
551 pip freeze
552 which python
553 ls -ls /c/Python310/python
554 ls -ls /c/Python310/python/
555 ls -ls /c/Python310/
556 ls -ls /c/Python310/Lib

Dans C:\Users\meyer\Documents\ephemeral\dev\python :
python -m venv rest-flask
source rest-flask/Scripts/activate
pip install flask
pip freeze

Exécuter le serveur
Dans C:\Users\meyer\Documents\ephemeral\dev\python :
export FLASK_APP=~/Documents/ephemeral/dev/rest-flask/app.py
printenv
flask run

En mode watch
flask run --reload
