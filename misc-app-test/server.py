from distutils.log import debug
import Flask

app = Flask(__name__)

@app.route("/main")
def mainPage():
    return {"appDetais": ["Flask", "React"]}




if __name__ == "__main__":
    app.run(debug=True)
