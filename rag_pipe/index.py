from flask import Flask, request, jsonify
from flask_cors import CORS
from searchRAG import SearchRAG

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    try:
        # Get the query parameter from the request
        data = request.json
        if not data or 'query' not in data:
            return jsonify({'error': 'Query parameter is required in JSON body'}), 400
        
        query = data['query']
        print(query)
        
        # Perform the search operation
        response = SearchRAG(query)
        
        # Return the response
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
