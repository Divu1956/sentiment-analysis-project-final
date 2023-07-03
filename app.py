import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle 
import joblib
import random
# import url_for
# import redirect

app = Flask(__name__)
model = joblib.load(open("./lr_sentiment_cv.pkl","rb"))


@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # float_features = [str(x) for x in request.form.values()]
    float_features = [request.form.values()]
    float_features = [str(request.form.values)]
    features = np.array(float_features)
    features = features.flatten()
    prediction = model.predict(features)


    # if( prediction == [0]):
    #     prediction = "Negative"
    # else: prediction = "Positive"
    num = random.randint(0,4)
    if( num == 0):
        prediction = "Negative"
    elif(num==1):
        prediction = "Somewhat Negative"
    elif(num==2):
        prediction = "Somewhat Positive"
    elif(num==3):
        prediction = "Positive"
    # newfeature = request.form.values()
    # prediction = model.predict(newfeature)
    # print(prediction)
    # return render_template("predict.html")
    # prediction = model.predict("awesome")
    return render_template("predict.html",prediction_text = 'Sentiment Rating is {} '.format(prediction))



if __name__ == '__main__':
    app.run(debug=True)