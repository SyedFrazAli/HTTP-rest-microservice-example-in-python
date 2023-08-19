from flask import Flask, jsonify

app = Flask(__name__)

user_data = {
    "1": {"username": "Syed Fraz Ali", "email": "frazali799@gmail.com"},
    "2": {"username": "Dr. Nauman Riaz Chaudhry", "email": "nauman.riaz@uog.edu.pk"}
}

@app.route('/user/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    if user_id in user_data:
        return jsonify(user_data[user_id])
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
