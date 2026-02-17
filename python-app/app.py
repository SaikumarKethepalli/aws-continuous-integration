from flask import Flask

app = Flask(__name__)

@app.route('/')
def howdy():
    return 'Howdy Aggies!'

if __name__ == '__main__':
    app.run()
