from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

# Create a Flask app instance
app = Flask(__name__)
# Configure MongoDB URI
app.config['MONGO_URI'] = 'mongodb://localhost:27017/web_app_db'
# Initialize PyMongo with the app
mongo = PyMongo(app)


@app.route('/submit', methods=['POST'])
def submit_data():
    # Get JSON data from the request
    data = request.get_json()

    if data:
        # Extract 'name' and 'email' from the JSON data
        name = data.get('name')
        email = data.get('email')

        # Check if 'name' and 'email' are provided
        if name and email:
            # Insert data into MongoDB
            db = mongo.db.users
            db.insert_one({'name': name, 'email': email})
            return jsonify({'message': 'Data submitted successfully!'}), 200
        else:
            return jsonify({'error': 'Name and email fields are required.'}), 400
    else:
        return jsonify({'error': 'Invalid request format.'}), 400


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
