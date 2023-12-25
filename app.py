from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'API KEY' 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def process_message():
        # Get the message from the request
        user_message = request.json.get('message', '')

        # Use OpenAI API to generate a response
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user","content": message}
        ]
        )

        return completion.choices[0].message.content
if __name__=='__main__':
    app.run()