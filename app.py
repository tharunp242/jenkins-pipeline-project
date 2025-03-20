from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is running inside Docker container!!!"

@app.route("/about")
def about():
    return "This is about page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)
