from flask import Flask, render_template
from board import board

app = Flask(__name__)

@app.route('/')
def checkerboard():
    result = board(8, 8)
    return render_template("checker.html", result = result)

@app.route('/<int:y>')
def checkerboard_2(y):
    result = board(8, y)
    return render_template("checker.html", result = result)

@app.route('/<int:x>/<int:y>')
def checkerboard_3(x, y):
    result = board(x, y)
    return render_template("checker.html", result = result)


if __name__=="__main__":
    app.run(debug=True)

