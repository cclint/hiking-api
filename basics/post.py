# this pythons script uses flask to create an api for getting hiking trails
from flask import Flask, jsonify 

app = Flask(__name__)

trails = [
    {'id': 1, 'name': 'Verstovia Trail', 'City': 'Sitka'},
    {'id': 2, 'name': 'Starrigavan Trail', 'City': 'Sitka'}
]

# Route to get all hiking trails 
@app.route('/trails', methods=['GET'])
def get_trails():
    return jsonify({'trails': trails
    })


if __name__ == '__main__':
    app.run(debug=True)