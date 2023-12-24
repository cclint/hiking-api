# this pythons script uses flask to create an api for GETTING AND POSTING hiking trails
# use postman or a curl command to post new trails
from flask import Flask, jsonify, request

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

@app.route('/trails',methods=['POST'])
def add_trail():
    new_trail = request.json
    if not new_trail or 'name' not in new_trail or 'City' not in new_trail:
        return jsonify({'error': 'Invalid trail data'}), 400
    
    # Create a new trail id
    new_trail_id = max(trail['id'] for trail in trails) + 1
    new_trail['id'] = new_trail_id
    trails.append(new_trail)

    return jsonify({'message': 'New Trail Added Successfully', 'trail': new_trail}), 201

if __name__ == '__main__':
    app.run(debug=True)

    
