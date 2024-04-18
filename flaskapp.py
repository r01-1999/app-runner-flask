from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get-header')
def get_header():
	host = request.headers['Host']
	response = make_response(
		jsonify({
			"host" : host
		}), 200)
	return response

if __name__ == '__main__':
	app.run(debug=True, threaded=True)
