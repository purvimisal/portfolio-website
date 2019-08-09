from flask import Flask, render_template, request, redirect

app = Flask(__name__)
myEmail = "" //Email ID where forms must be sent
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/submitform', methods = ['POST'])
def submitform():
    email = request.form['email']
    name = request.form['name']
    tel = request.form['tel']
    msg = request.form['message']
    if not email or not name or not msg:
        return redirect('/')
    import sendemail
    sendmail.mainSendMail(myEmail, name, str('Email: ' +email + '\nPhone number: ' + tel + '\nMessage: ' + msg))
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)