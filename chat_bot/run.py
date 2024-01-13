from flask import Flask
from flask import render_template, request, jsonify
from run import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['user_message']
    # Process user_message and generate chatbot_response using NLP
    chatbot_response = "This is a placeholder response."
    return jsonify({'bot_response': chatbot_response})
app = Flask(__name__)

from run import routes


if __name__ == '__main__':
    app.run(debug=True)