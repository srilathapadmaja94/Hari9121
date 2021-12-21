from flask import Flask, render_template, request, redirect
app = Flask(__name__)
global database
database={}
@app.route("/", methods=['GET','POST'])
def login():
	Access = {'ram':'1234','hari':'1010','krishna':'4567'}
	Username = request.form.get('Username')
	Password = request.form.get('Password')
	if Username in Access.keys():
		if Access[Username]==Password:
			return render_template('add.html')
	return render_template("login.html")
@app.route("/display", methods=['GET','POST'])
def display():
	Name = request.form.get('Name')
	Mobile_Number = request.form.get('Mobile_number')
	database[Name]=Mobile_Number
	return render_template("display.html",Name = Name, Mobile_Number = Mobile_Number, database = database)
	

@app.route("/add", methods=['GET','POST'])
def add():
    Name = request.form.get('Name')
    Mobile_Number = request.form.get('Mobile_number')
    database[Name]=Mobile_Number
    return render_template('add.html', Name = Name, Mobile_Number = Mobile_Number, database = database)
    return redirect('display')

@app.route("/search", methods=['GET','POST'])
def search():
	 Search_Name = request.form.get('Name')
	 return render_template('search.html', Search_Name = Search_Name, database = database)
	 return redirect('index')

if __name__ == '__main__':
	app.run(debug=True,port='5002')