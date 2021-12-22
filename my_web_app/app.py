import requests
from flask import Flask, render_template, request, redirect, flash
import psycopg2
import time

app = Flask(__name__)


app.config['SECRET_KEY'] = '?~RdA:a("cPE<7O*3gwIb(n6Q'


conn = psycopg2.connect(database="service_db",
						user="postgres",
						password="1234",
						host="localhost",
						port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
	return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
	if request.method == 'POST':
		if request.form.get("login"):
			username = request.form.get('username')   
			password = request.form.get('password')
			if str(username) == '' and str(password)== '':
				flash(message='Username and password not entered')
			elif str(username) != '' and str(password)== '':
				flash(message='Password not entered')
			elif str(username) == '' and str(password) != '':
				flash(message='Username not entered')
			else:
				cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
				records = list(cursor.fetchall())
				return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
		elif request.form.get("registration"):
			return redirect("/registration/")
	return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        if str(name) == '':
        	flash('Name not entered')
        if str(login) == '':
        	flash('Login not entered')
        if str(password) == '':
        	flash('Password not entered')
        if str(name) != '' and str(login) != '' and str(password) != '':
        	if len(password) < 3:
        		flash('The password must contain at least 3 characters')
        	else:
        		cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',(str(name), str(login), str(password)))
        		conn.commit()
        		flash('You have successfully registered')
        		time.sleep(2)
        		return redirect('/login/')
    return render_template('registration.html')



if __name__ == "__main__":
	app.run(debug=True)