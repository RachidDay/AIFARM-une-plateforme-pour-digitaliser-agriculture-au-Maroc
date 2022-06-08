import pandas as pd
from utils.fertilizer import fertilizer_dic
import re
import numpy as np
from flask import Flask, render_template, request, Markup
import requests
import sklearn
import pickle
# --------- 

crop_translator = {
    'rice' : 'riz',
    'maize' : 'maïs',
    'chickpea' : 'pois chiche',
    'kidneybeans' : 'haricots rénaux',
    'pigeonpeas' : "pois d'Angole",
    'mothbeans' : 'haricots papillon',
    'mungbean' : 'haricot mungo',
    'blackgram' : 'mâle',
    'lentil' : 'lentille',
    'pomegranate' : 'grenade',
    'banana' : 'banane',
    'mango' : 'mangue',
    'grapes' : 'les raisins',
    'watermelon' : 'pastèque',
    'muskmelon' : 'cantaloup',
    'apple' : 'pomme',
    'orange' : 'orange',
    'papaya' : 'papaye',
    'coconut' : 'noix de coco',
    'cotton' : 'coton',
    'jute' : 'jute',
    'coffee' : 'café'
}
inv_crop_translator = {v : k for k, v in crop_translator.items()}
# ---------
def city_name_separater(city_name):
        x = city_name.split(' ')
        print(x, len(x))
        if len(x) != 1:
            result = ""
            for i in range(len(x)):
                result += x[i] + "+"
            return result[:-1]
        else :
            return city_name

def weather_fetch(city_name):
    city = city_name_separater(city_name)
    print(f"city in params : {city_name}, city after separtaion : {city}, nbre de characteres : {len(city)}")
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = "9d7cde1f6d07ec55650544be1631307e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()


    if x["cod"] != "404":
        y = x["main"]
        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None



crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


# ---------
app = Flask(__name__)

#render Accueil page
@ app.route('/')
def Accueil():
    title = 'AIfarm - Accueil'
    return render_template('index.html', title=title)

#render Recommandation de culture form page
@ app.route('/culture-recommandation')
def crop_recommendation():
    title = 'AIfarm - Recommandation de culture'
    return render_template('crops.html', title=title)

#render Recommandation de culture result page
@ app.route('/culture-predire', methods=['POST'])
def crop_prediction():
    title = 'AIfarm - Recommandation de culture'
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potassium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        city = request.form['city']
        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            print(1)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = crop_translator[my_prediction[0]]
            

            return render_template('crop_prediction.html', prediction=final_prediction, title=title)
        
        else:
            print(city, weather_fetch(city))
            # return render_template('try_again.html', title=title)

# --------

#render fertilizer recommendation form page
@app.route('/engrais-recommandation')
def fertilizer_recommendation():
    title = 'AIfarm - Engrais recommandatoin'
    return render_template('fertilizer.html', title=title)

#render fertilizer results page
@app.route('/engrais-predire', methods=['POST'])
def fert_recommend():
    title = 'AIfarm - Engrais recommandation'

    crop_name_fr = str(request.form['cropname'])
    crop_name = inv_crop_translator[crop_name_fr]
    print(crop_name)
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorous'])
    K = int(request.form['potassium'])
    # ph = float(request.form['ph'])

    df = pd.read_csv('data/fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]
    
    print(nr, pr, kr)
    
    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = Markup(str(fertilizer_dic[key]))

    return render_template('fertilizer_prediction.html', recommendation=response, title=title)

# --------

#render services page
@app.route('/services')
def services():
    title = 'AIfarm - Services'
    return render_template('service-page.html', title=title)

# --------

#render contact-us page
@app.route('/contact-us')
def contact_us():
    title = 'AIfarm - contact-us'
    return render_template('contact-us.html', title=title)

# --------
if __name__ == '__main__':
    app.run(debug=False)
