from flask import Flask

import configs

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!1112'


if __name__ == '__main__':
    print(app.config)

    app.run()


