# flask --app server run (used to run)
from flask import Flask, render_template, url_for, request, redirect, jsonify
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/login")
def my_login():
    return render_template('login.html')


@app.route("/verification-success")
def html_page2():
    return render_template('verification-success.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    try:
        return render_template(page_name)
    except:
        return render_template('404.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Could not save to database'
    else:
        return 'Error Try Again'


@app.route('/send-verification-email', methods=['POST'])
def send_verification_email():
    # Retrieve the email from the request
    email = request.form.get('email')

    # Implement your email sending logic here
    # ...

    # Redirect the user to a success page or display a success message
    return redirect('/verification-success')
