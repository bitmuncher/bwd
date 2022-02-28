from flask import Flask, render_template, redirect, request, abort

app = Flask(__name__)

@app.route('/')
def bwd():
  """ 
  GET - redirect to default index page
  """
  return redirect('/index', code=302)

@app.route('/index')
def index():
  """
  GET - show dashboard
  """
  return render_template('index.html')

@app.route('/about')
def about():
  """
  GET - show infos
  """
  return render_template('about.html')
