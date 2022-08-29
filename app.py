from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('Regression_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html',
                           data1=[{'GeN': 'Gender'}, {'GeN': 0}, {'GeN': 1}],
                           data2=[{'MN': 'Month'}, {'MN': 1}, {'MN': 2}, {'MN': 3}, {'MN': 4}, {'MN': 5}, {'MN': 6},
                                  {'MN': 7}, {'MN': 8},
                                  {'MN': 9}, {'MN': 10}, {'MN': 11}, {'MN': 12}],
                           data3=[{'CO': 'Company'}, {'CO': 0}, {'CO': 1}],
                           data4=[{'CY': 'City'}, {'CY': 1}, {'CY': 2}, {'CY': 3}, {'CY': 4}, {'CY': 5}, {'CY': 6},
                                  {'CY': 7}, {'CY': 8},
                                  {'CY': 9}, {'CY': 10}, {'CY': 11}, {'CY': 12}, {'CY': 13}, {'CY': 14}, {'CY': 15},
                                  {'CY': 16},
                                  {'CY': 17}, {'CY': 18}])

@app.route('/predict', methods = ['POST'])
def predict():
    input_features = [int(x) for x in request.form.values()]
    final_features = [np.array(input_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Investment should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(port=5000, debug=True)


