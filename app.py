from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def helloworld():
    return render_template("home.html")

@app.route("/dict/")
def good():
    return render_template("dict.html")

if(__name__ == "__main__"):
    app.run(host="0.0.0.0" ,debug=True)