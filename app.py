from flask import Flask, render_template, request
from data import locations, property_type, room_type, bed_type, cancellation_policy , instant_bookable
from prediction import prediction
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=["GET","POST"])
def index_predict():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
         
        data['accommodates'] = float(data['accommodates'])
        data['bathrooms'] = float(data['bathrooms'])
        data['bedrooms'] = float(data['bedrooms'])
        data['cleaning_fee'] = float(data['cleaning_fee'])
        data['security_deposit'] = float(data['security_deposit'])
        data['extra_people'] = float(data['extra_people'])
        data['guests_included'] = float(data['guests_included'])
        data['minimum_nights'] = float(data['minimum_nights'])
        data['availability_365'] = float(data['availability_365'])
        data['beds'] = float(data['beds'])
        data['smoke_detector'] = float(data['smoke_detector'])
        data['pets_allowed'] = float(data['pets_allowed'])
        data['tv'] = float(data['tv'])
        data['high_end_electronics'] = float(data['high_end_electronics'])
        data['secure'] = float(data['secure'])
        data['breakfast'] = float(data['breakfast'])
        data['elevator'] = float(data['elevator'])
        data['washing_machine'] = float(data['washing_machine'])
        data['heating'] = float(data['heating'])
        data['internet'] = float(data['internet'])
        data['wheelchair_access'] = float(data['wheelchair_access'])
        data['pool'] = float(data['pool'])
        data['room_key'] = float(data['room_key'])
        data['Hot_Tub'] = float(data['Hot_Tub'])
        data['hair_dryer'] = float(data['hair_dryer'])
        data['hangers'] = float(data['hangers'])
        data['fire_extinguisher'] = float(data['fire_extinguisher'])
        data['free_parking'] = float(data['free_parking'])
        data['gym'] = float(data['gym'])
        data['tv'] = float(data['tv'])
        data['tv'] = float(data['tv'])
        data['kitchen'] = float(data['kitchen'])
        data['workspace'] = float(data['workspace'])
        data['firstAid_kit'] = float(data['firstAid_kit'])


        hasil = prediction(data)
        return render_template('prediction.html', hasil_prediction = hasil)
    return render_template('prediction.html', data_location= sorted(locations),
    data_property=sorted(property_type), data_room_type=sorted(room_type), data_bed_type=sorted(bed_type),
    data_instant_bookable=sorted(instant_bookable), data_cancellation_policy=sorted(cancellation_policy))


@app.route('/visualization')
def visual():
    return render_template('visualization.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/data')
def dataset():
    data = pd.read_csv('listings_cleaned')
    return render_template('dataset.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=1212)