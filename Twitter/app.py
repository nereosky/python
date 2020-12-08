from flask import Flask, render_template, url_for, request
import joblib

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    #load model 
    model_filename = "./model/hatespeech.joblib.z"
    clf = joblib.load(model_filename)
    # Receives the input query from form
    if request.method == 'POST':
	    namequery = request.form['namequery']
	    data = [namequery]
	    probas = clf.predict_proba([str(data)])[0]
    return render_template('result.html', probas=probas)


if __name__ == '__main__':
    app.run(debug=True)





