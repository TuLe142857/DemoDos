from flask import Flask, render_template


app = Flask(__name__)

count = 0
@app.route("/")
def home():
    global count
    count += 1
    return render_template("home.html", count=count)
if __name__ =='__main__':
    print("hello world")
    app.run(host="0.0.0.0", port=8080, debug=True)