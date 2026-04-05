from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "secret123"

data = {
    "manick123@gmail.com": "manick123",
    "arun123@gmail.com": "arun123",
    "justinmala@gmail.com": "JK123"
}

#sign in
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in data and data[email] == password:
            session['user'] = email
            flash("Login Successful")
            return redirect('/home')
        else:
            flash("Invalid Email or Password")

    return render_template("login.html")

#sign up
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if email in data:
            flash("User already exists")
        elif password != confirm:
            flash("Passwords not match")
        else:
            data[email] = password
            flash("Signup Successful Please login")
            return redirect('/')

    return render_template("signup.html")

#Home
@app.route('/home')
def home():
    if 'user' in session:
        return render_template("home.html", user=session['user'])
    else:
        return redirect('/')

#logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Log out successful")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    