# nlp-zero-shot

Get category score for a text from a list of categories.

## Getting Started

first install dependencies for the application using
```
pip install -r requirements.txt
```
After that if you have python installed on your pc run this command on your terminal
```
python app.py
```
This will spawn up a server on your localhost at port 5000. send a POST request to the endpoint `/predict-text` with the JSON payload structured
```
{
  "text": string,
  "categories": [string]
}
```
