import requests
from flask import Flask, request, jsonify , url_for

app = Flask(__name__)


API_URL = "https://api-inference.huggingface.co/models/jamm55/autotrain-improved-pidgin-model-2837583188"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

@app.route('/')
def home():
    # payloads = {"inputs": "how are you doing today?"}
    # output = requests.post("http://localhost:5000/predict",json=payloads)
    return "Hello, World"



@app.route('/predict', methods=["POST"])
def predict():
    # Get the input data from the request body
    data = request.json
    print(data)
    output = query(data)
    # Return the prediction as a JSON response
    return jsonify({'prediction': output})

if __name__ == '__main__':
    app.run(debug=True)
