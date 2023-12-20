from flask import Flask, request, render_template
app = Flask(__name__)

def get_openai_response(query):
    print(f"Forwarding to OpenAI: {query}")
    return "I'm sorry, but I can't assist with that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = chatbot_response(user_input)
    if "I'm sorry, but I can't assist with that." in bot_response:
        get_openai_response(user_input)
    return render_template('index.html', user_input=user_input, bot_response=bot_response)

#just some prompts for testing
def chatbot_response(user_input):
    if "how are you" in user_input.lower():
        return "I'm just a computer program, but I'm doing well. How can I assist you today?"
    elif "your name" in user_input.lower():
        return "I'm a chatbot. You can call me ChatGPT."
    elif "python" in user_input.lower():
        return "I love Python! It's a powerful and versatile programming language."
    elif "openai" in user_input.lower():
        return "OpenAI is an amazing organization that develops artificial intelligence technologies."
    elif "flask" in user_input.lower():
        return "Flask is a lightweight and powerful web framework for Python."
    return f"I'm sorry, but I can't assist with that. Let me try OpenAI."


if __name__ == "__main__":
    app.run(debug=True)