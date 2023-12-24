import requests

# Define the data to be sent as JSON
new_trail_data = {
    'name': 'Verstovia',
    'city': 'Sitka, Alaska'
}

# Send a POST request to add a new trail
response = requests.post('http://127.0.0.1:5000/trails', json=new_trail_data)

# Check the response status code and content
if response.status_code == 201:
    print('New trail added successfully:')
    print(response.json())
else:
    print('Failed to add a new trail:')
    print(response.json())
