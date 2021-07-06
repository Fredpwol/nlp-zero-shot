from flask import Flask, request, jsonify

from transformers import pipeline

app = Flask(__name__)

task = "zero-shot-classification"
model = "typeform/distilbert-base-uncased-mnli"
classifier = pipeline(task, model)

@app.route("/predict-text", methods=["POST"])
def predict_text():
    """
    This is a API route that accepts POST requests with a json payload of two attributes
    1. text
    2. categories
    Trys to label the text based on the categories passed in and responds with a score for each category in JSON.
    """

    try:
        data = request.get_json()
        if not all([field in ["text", "categories"] for field in data]): #we check for all required parameters to be in the JSON payload
            return jsonify(status="error", message="Please valid json parameters are 'text' and 'categories'"), 400

        if type(data["text"]) != str: return jsonify(status="error", message="text must be a text string"), 400 #CHECK to see if the type of the text is string
        
        predict = classifier(data["text"], data["categories"])
        res = {}
        for i in range(len(predict["labels"])):
            res[predict["labels"][i]] = predict["scores"][i] #unpack labels and their corresponding score into a dictionary res

        return jsonify(res), 200
    except Exception as e:
        print("ERROR: ", e)
        return jsonify(status="error", message=str(e)), 400


if __name__ == "__main__":
    app.run(debug=True)