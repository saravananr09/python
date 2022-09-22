from distutils.log import debug
from flask import Flask,send_from_directory

app = Flask(__name__)


@app.route("/main")
def mainPage():
    return {"appDetais": ["Flask", "React"]}
     

@app.route('/dashboard')
def send_report(path):
    return send_from_directory('dashboard', path)

send_report('/Users/saravanan/python/misc-app-test/app/ui/dashboard/index.html')
if __name__ == "__main__":
    app.run(port=3001)
