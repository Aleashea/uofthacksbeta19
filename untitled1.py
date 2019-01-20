from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Landing Page!'

@app.route('/complicated')
def complicated_life():
    pass

@app.route('/process_image')
def process_image():
    pass

@app.route('choose-object')
def choose_object():
    pass

if __name__ == '__main__':
    app.run()


## Need to process image from POST request
##
## Send image to Azure API -> Separate module: Sai
##
## Filter objects using another module -> Separate module: Cynthia
##
## Pick top three objects and see where they are supposed to go?
##
## Alex figures out HTML / CSS template so we know how to route back?
##
##
##

action="{{ url_for('handle_data') }}