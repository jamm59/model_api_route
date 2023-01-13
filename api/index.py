from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# # initialize the tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(
#     "jamm55/autotrain-improved-pidgin-model-2837583189"
# )
# model = AutoModelForSeq2SeqLM.from_pretrained(
#     "jamm55/autotrain-improved-pidgin-model-2837583189"
# )

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# @app.route('/predict', methods=["POST"])
# def predict():
#     # Get the input data from the request body
#     data = request.json
#     input_text = data['input_text']
#     # tokenize the input
#     input_ids = tokenizer.encode(input_text, return_tensors='pt')
#     # Generate translations
#     output = model.generate(input_ids)
#     # Decode the generated translations
#     predicted_text = tokenizer.decode(output[0], skip_special_tokens=True)
#     # Return the prediction as a JSON response
#     return jsonify({'prediction': predicted_text})

# if __name__ == '__main__':
#     app.run()
