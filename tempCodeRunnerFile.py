pp.route("/predict", methods=["POST"])
# def predict():
#     # float_features = [str(x) for x in request.form.values()]
#     float_features = [str(request.form.values)]
#     # features = [np.array(float_features)]
#     prediction = model.predict(float_featurescls)
#     # prediction = model.predict("awesome")
#     return render_template("index.html",prediction_text = 