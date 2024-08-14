from flask import Flask

# Insitalizing the flask app
# WSGI App
app = Flask(__name__)

## create route
@app.route("/")
def welcome():
    return "Welcome to this Flask World."


@app.route("/index")
def index():
    return "Welcome to index page."




if __name__=="__main__":
    # app.run()
    # restart server automatically
    app.run(debug=True)






