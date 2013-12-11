# Django real-time chat example


This example demonstrates real-time chat with Django. It uses the django_socketio app and gevent and greenlets for long-polling.

### Installation

    git clone git@github.com:ailling/chatapp.git
    cd chatapp
    virtualenv venv
    pip install - requirements.txt

### Starting the server

This solution uses the long polling technique. You must start two servers to vend the app: one is to vend synchronous request/reply communication as in a typical web app; the other is to handle asynchronous communication through socket-io.

    ./manage.py runserver localhost:8000 # start the web server
    ./manage.py runserver_socketio localhost:9000 # start the async server for socketio

### Version

v0.1

This is a demo app, not intended for production use.
