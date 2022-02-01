from flask import Flask, render_template, request,url_for
import datetime

app = Flask(__name__)
global database,l,amount,x
database={"Hari":["1010","12345",[5000]]}##{username:["pin","account number","amount"}
l=[]

@app.route("/",methods=["GET","POST"])
def index():

	username = request.form.get('username')
	password = request.form.get('password')

	for i,j in database.items():
		if username == i and password == j[0]:
			return render_template('options.html',username=username)
		#return render_template('loginfail.html', username=username)
	return render_template("login.html")

@app.route("/withdraw",methods=["GET","POST"])
def withdraw():
	dt= datetime.datetime.now()
	x = dt.strftime("%Y-%m-%d %H:%M:%S")
	withdraw = request.form.get('withdraw')
	password1 = request.form.get('password')
	for password, acnumber, amount in database.values():
		if password1 == password:
			if amount[-1]>=int(withdraw):
				an = amount[-1] - int(withdraw)
				amount.append(an)
				b = "Debit", "-"+f"{(withdraw)}",f"{x}"
				l.append(b)
				return render_template("msg.html",database=database,l=l,x=x,msg = "Amount {} is debited successfully".format(withdraw))
			return render_template("withdrawfail.html", database=database, l=l,x=x)
	return render_template("withdraw.html",database=database,l=l)

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
	dt = datetime.datetime.now()
	x = dt.strftime("%Y-%m-%d %H:%M:%S")
	deposit = request.form.get('deposit')
	acnumber1 = request.form.get('acnumber')
	for password, acnumber, amount in database.values():
		if acnumber1 == acnumber:
			an = amount[-1] + int(deposit)
			amount.append(an)
			b = "Credit", "+"+f"{int(deposit)}",f"{x}"
			l.append(b)
			return render_template("msg.html",database=database,l=l,x=x,msg = "Amount {} is credited successfully".format(deposit))
	return render_template("deposit.html", database=database,l=l,x=x)


@app.route("/ministat", methods=["GET", "POST"])
def ministat():
	dt = datetime.datetime.now()
	x = dt.strftime("%Y-%m-%d %H:%M:%S")
	for password, acnumber, amount in database.values():
		return render_template("ministat.html",database=database,l=l,amount=amount,x=x)
	return render_template("ministat.html", database=database, l=l,amount=amount)

@app.route("/exit", methods=["GET", "POST"])
def exit():
	for username in database.keys():
		pass
	return render_template("options.html",username=username)

if __name__ == '__main__':
	app.run(debug=True)
