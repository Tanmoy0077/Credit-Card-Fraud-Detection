from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("./model_development/models/RF.pkl", "rb"))

def get_prediction(data):
    x = [np.float64(data[f'V{i}']) for i in range(1, 29)]
    x.append(np.float64(data["Amount"]))
    x = np.expand_dims(np.array(x), axis=0)
    return model.predict(x)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    return render_template("data.html", features=[f"V{i}" for i in range(1, 29)])


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    prediction = get_prediction(data)
    message = "Fraudulent Transaction" if prediction[0] > 0 else "Non-Fraudulent Transaction"
    return render_template("results.html", prediction=message)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)