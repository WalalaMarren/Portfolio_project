from flask import Flask, render_template, url_for, flash, redirect, request
from pets import app
from pets.forms import Register, Login

@app.route('/')
@app.route('/Home')
def home():
    return render_template('index.html')

@app.route('/Sign Up', methods=['POST', 'GET'])
def register():
    form = Register()
    if request.method == 'POST' and form.validate():
        user = User(form.first_name.data, form.last_name, form.email.data,
                    form.password.data)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
    
@app.route('/Log In', methods=['POST', 'GET'])
def login():
    form = Login()
    return render_template('login.html', form=form)

@app.route('/Breeds')
def breed():
    return render_template('breeds.html')

@app.route('/Contact Us')
def contact():
    return render_template('contact.html')




