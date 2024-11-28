import flask


app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><H1> hello world </H!></html>'

@app.route('/about')
def about_us():
    return '<html><H1> my name is momen </H1></html>'


if __name__ == '__main__':
    app.run(debug=True)