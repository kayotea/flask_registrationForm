from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*\d)(?=.*[A-Z]).+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def validate():
    email = request.form['email']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    pw = request.form['password']
    pwConfirm = request.form['confirm_pw']
    # email check
    if len(email) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
    # first name check
    if len(firstName) < 1:
        flash("First name cannot be blank!")
    # last name check
    if len(lastName) < 1:
        flash("Last name cannot be blank!")
    # check that first and last name contain no numbers
    elif hasNumbers(firstName) or hasNumbers(lastName):
        flash("Name must not contain numbers!")
    # password check
    if len(pw) < 1:
        flash("Please input your password!")
    # make sure password is at least 8 characters
    elif len(pw) < 8:
        flash("Please use a password longer than 8 characters!")
    # make sure password has at least 1 uppercase and 1 lowercase letter
    if not PW_REGEX.match(pw):
        flash("Please use at least 1 number and 1 uppercase letter in your password!")
    # confirm password check
    if len(pwConfirm) < 1:
        flash("Please confirm your password!")
    # check that password matches password confirmation
    if pw != pwConfirm:
        flash("Your password do not match! Please double check!")
    else:
        flash("Success!")
    return redirect('/')

#returns true if the given string contains a number
def hasNumbers(string):
    return bool(re.search(r'\d', string))

app.run(debug=True)