from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/mars")
def hello_mars():
    return "<p>Hello, planet Mars!</p>"

@app.route("/mars2")
def hello_mars2():
    return render_template("hello_mars.html")

if __name__=="__main__":
    app.run(debug=True)
