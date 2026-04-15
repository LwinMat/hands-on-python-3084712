from flask import Flask

app = Flask(__name__)

# using decoratings to create routes
@app.route("/")
def hello():
  return "Hello, World"

app.run(debug=True)