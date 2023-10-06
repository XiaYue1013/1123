from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['剪刀', '石頭', '布']
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    return jsonify({'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result})

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平局"
    elif (
        (user_choice == '剪刀' and computer_choice == '布') or
        (user_choice == '石頭' and computer_choice == '剪刀') or
        (user_choice == '布' and computer_choice == '石頭')
    ):
        return "你赢了！"
    else:
        return "電腦赢了！"

if __name__ == '__main__':
    app.run(debug=True)
