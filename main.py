from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/submitform', methods = ['POST'])
def submitform():
    email = request.form['email']
    name = request.form['name']
    tel = request.form['tel']
    msg = request.form['message']
    fileName = "Forms.txt"
    file = open(fileName,'a+',encoding="utf-8")
    file.write("Name:" + name + '\n')
    file.write("Telephone:" + tel + '\n')
    file.write("Email:" + email + '\n')
    file.write("Message:" + msg + '\n')
    file.write("----------------------------------------" + '\n')
    file.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
