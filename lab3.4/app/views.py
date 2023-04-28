from flask import render_template, redirect
from app import app
from app.forms import FileForm
from app.repository import Repository

repo = Repository()

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index(): 
    form = FileForm()     
    if form.validate_on_submit():         
        repo.save(form)             
        return redirect('/result')     
 
    return render_template(
        'index.html',
        form = form
    ) 
     
@app.route('/result', methods=['get'])
def result():          
    return render_template(
        'result.html',
        files = repo.files_dict
    )   