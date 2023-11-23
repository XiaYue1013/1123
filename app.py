from flask import Flask, render_template, request, jsonify
import random
from flask_frozen import Freezer
import sys

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    choices = ['剪刀', '石頭', '布']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "平手!"
    elif (user_choice == "剪刀" and computer_choice == "布") or \
         (user_choice == "石頭" and computer_choice == "剪刀") or \
         (user_choice == "布" and computer_choice == "石頭"):
        result = "你贏了!"
    else:
        result = "你輸了!"

    return jsonify(user_choice=user_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("Building website...")
        freezer.freeze()
    else:
        app.run(debug=True)
