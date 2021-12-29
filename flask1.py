#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!!</h1>"

