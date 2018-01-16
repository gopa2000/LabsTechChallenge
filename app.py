from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/do2324', methods=['GET'])
def homepage():
	return render_template('do2324.html')

if __name__ == '__main__':
    app.run()
