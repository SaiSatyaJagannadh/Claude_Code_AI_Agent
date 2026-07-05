from flask import Flask, render_template, request
from local_ai_agent import run_agent

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        if user_input:
            try:
                result = run_agent(user_input)
            except Exception as e:
                result = f"Error: {str(e)}"
    return render_template('index.html', user_input=user_input, result=result)

if __name__ == '__main__':
    # For development only. Use a production server for deployment.
    app.run(debug=True, host='0.0.0.0', port=5000)