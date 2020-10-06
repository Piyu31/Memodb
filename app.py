from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json
# requests
import database_memo

#This is how you tell python that this is a flask app
app = Flask(__name__)

#GCD (Good Coding Practice)
app.secret_key="563782639628026"




#Python is an indented language
#Python uses indentation to indicate a block of code belonging to a certain func, or for,i, etc.

#Its the entry point to the browser
@app.route("/")
def index():
	#get all data from db
#getting  install_companies data
	install_comapanies = database_memo.get_installation_companies()
	# list[list[key:value pair]]
	userinstalllist = []
	for i in install_comapanies:
		userinstalllist.append(i)

#getting  memo data
	memo_data = database_memo.get_memo()
	usermemolist = []
	for m in memo_data:
		usermemolist.append(m)

#getting  token_map data
	token_map = database_memo.get_token_map()
	tokenmaplist =[]
	for t in token_map:
		tokenmaplist.append(t)

	return render_template('base.html', userlist = userinstalllist, memolist = usermemolist, tokenlist = tokenmaplist)



@app.route("/", methods=['POST'])
def update_installcompaniesdb():
	#for installation companies collection data	
	newdata = {}
	phone_number = request.form['phone_number']
	account_number = request.form['account_number']
	account_name = request.form['account_name']
	#send data to db
	newdata["phone_number"] = phone_number
	newdata["account_number"] = account_number
	newdata["account_name"] = account_name
	print (newdata)
	database_memo.save_installation_companies(newdata)
	return redirect(url_for('index'))


#for memo collection data
@app.route("/", methods=['POST'])	
def update_memodb():
	fewdata = {}
	memo_url = request.form['memo_url']
	memo_id = request.form['memo_id']
	datetime_creation = request.form['datetime_creation']
	#send data to db
	fewdata["memo_url"] = memo_url
	fewdata["memo_id"] = memo_id
	fewdata["datetime_creation"] = datetime_creation
	print(fewdata)
	database_memo.save_memo(fewdata)
	return redirect(url_for('index'))

#for token collection data
@app.route("/", methods=['POST'])
def update_tokenmapdb():
	dewdata = {}
	token_id = request.form['token_id']
	memo_id = request.form['memo_id']
	user_id = request.form['user_id']
	seen = request.form['seen']
	#send data to db
	dewdata["token_id"] = token_id
	dewdata["memo_id"] = memo_id
	dewdata["user_id"] = user_id
	dewdata["seen"]  = seen
	print(dewdata)
	database_memo.save_token_map(dewdata)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)