from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    # For development only. Use a production server for deployment.
    app.run(debug=True, host='0.0.0.0', port=5000)
