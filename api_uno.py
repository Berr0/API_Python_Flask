from flask import Flask
from flask import render_template
from flask import request


api_uno = Flask(__name__)

#Create diccionary 
todo_list = {}

@api_uno.post('/create_todo')
def create_todo():
    data = request.get_json(force=True)
    pass


@api_uno.route('/get_todos')
def get_todos():
    pass

@api_uno.put('/create_todo')
def complete_todo():
    pass