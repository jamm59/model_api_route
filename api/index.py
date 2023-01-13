# from flask import Flask, request, jsonify
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# tokenizer = AutoTokenizer.from_pretrained(
#     "jamm55/autotrain-pidgintranslationmix-2798982563"
#     )
# model = AutoModelForSeq2SeqLM.from_pretrained(
#     "jamm55/autotrain-pidgintranslationmix-2798982563"
#     )
# app = Flask(__name__)

# @app.route('/predict', methods=["GET","POST"])
# def predict():
#     # Get the input data from the request body
#     #data = request.json

#     input_text = "When are we going to the zoo?"

#     input_ids = tokenizer.encode(input_text, return_tensors='pt')

#     # Generate translations
#     output = model.generate(input_ids)

#     # Decode the generated translations
#     predicted_text = tokenizer.decode(output[0], skip_special_tokens=True)

#     print(predicted_text)

#     # Return the prediction as a JSON response
#     return jsonify({'prediction': predicted_text})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

