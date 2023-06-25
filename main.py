from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return 'Hello, welcome to my exercise deployment'

@app.route('/cow')
def cow():
    return 'MOoooOo!'


if __name__ == '__main__':
    
   app.run(port=8080)


    
   

