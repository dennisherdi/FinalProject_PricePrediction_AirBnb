from flask import Flask, render_template, request
import plotly.graph_objs as go 
import pandas as pd
import plotly
import joblib
import numpy as np
import json


listings = pd.read_csv('/Users/dennisherdi/data_science/FinalProject_PricePrediction_AirBnb/listings_visual.csv')
app = Flask(__name__)




# 1 home index
@app.route('/')
def index():
    plot = category_plot()
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('neighbourhood_cleansed', 'Neighbourhood'),('bed_type','Bed Type'), ('property_type', 'Property Type'),
            ('room_type','Room Type'),('instant_bookable','Instant_bookable'),('cancellation_policy','Cancellation Policy')]
    list_y = [('price', 'Price'), ('bathrooms', 'Bathroom'), ('accommodates','Accommodates'),
                ('bedrooms','Bedroom'),('cleaning_fee','Cleaning Fee'),('availability_365','Available'),('guests_included','Guests Included'),
                ('extra_people','Extra People'),('minimum_nights','Minimum Nights'),('high_end_electronics','Electronics'),
                ('smoke_detector','Smoke Detector'), ('washing_machine','Washing Machine'),('heating', 'Heating'),('hair_dryer','Hair Dryer'), 
                ('hangers','Hangers'),('free_parking','Free_Parking'), ('gym','Gym'), ('tv','Tv'), ('kitchen','Kitchen'),
                ('workspace','Workspace'),('internet','Internet')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('neighbourhood_cleansed', 'Neighbourhood'),('bed_type','Bed Type'), ('property_type', 'Property Type'),
            ('room_type','Room Type'),('instant_bookable','Instant_bookable'),('cancellation_policy','Cancellation Policy')]

    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot='histplot',
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x='bed_type',

        # untuk sumbu Y tidak ada, nantinya menu dropdown Y akan di disable
        # karena pada histogram, sumbu Y akan menunjukkan kuantitas data

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator='count',
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue='neighbourhood_cleansed',
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue
        )
def category_plot(
    cat_plot = 'histplot',
    cat_x = 'bed_type', cat_y = 'price',
    estimator = 'count', hue = 'bed_type'):

    # jika menu yang dipilih adalah histogram
    if cat_plot == 'histplot':
        # siapkan list kosong untuk menampung konfigurasi hist
        data = []
        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in listings[hue].unique():
            hist = go.Histogram(
                x=listings[listings[hue]==val][cat_x],
                y=listings[listings[hue]==val][cat_y],
                histfunc=estimator,
                name=str(val)
                )
            #masukkan ke dalam array
            data.append(hist)
        #tentukan title dari plot yang akan ditampilkan
        title='Histogram'
    elif cat_plot == 'boxplot':
        data = []

        for val in listings[hue].unique():
            box = go.Box(
                x=listings[listings[hue] == val][cat_x], #series
                y=listings[listings[hue] == val][cat_y],
                name=str(val)
            )
            data.append(box)
        title='Box'
    if cat_plot == 'histplot' and estimator == 'count':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='person'),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    #simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/cat_fn/<nav>')
def cat_fn(nav):

    # saat klik menu navigasi
    if nav == 'True':
        cat_plot = 'histplot'
        cat_x = 'bed_type'
        cat_y = 'price'
        estimator = 'count'
        hue = 'bed_type'
    
    # saat memilih value dari form
    else:
        cat_plot = request.args.get('cat_plot')
        cat_x = request.args.get('cat_x')
        cat_y = request.args.get('cat_y')
        estimator = request.args.get('estimator')
        hue = request.args.get('hue')

    # Dari boxplot ke histogram akan None
    if estimator == None:
        estimator = 'count'
    
    # Saat estimator == 'count', dropdown menu sumbu Y menjadi disabled dan memberikan nilai None
    if cat_y == None:
        cat_y = 'price'

    # Dropdown menu
    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('neighbourhood_cleansed', 'Neighbourhood'),('bed_type','Bed Type'), ('property_type', 'Property Type'),
            ('room_type','Room Type'),('instant_bookable','Instant_bookable'),('cancellation_policy','Cancellation Policy')]
    list_y = [('price', 'Price'), ('bathrooms', 'Bathroom'), ('accommodates','Accommodates'),
                ('bedrooms','Bedroom'),('cleaning_fee','Cleaning Fee'),('availability_365','Available'),('guests_included','Guests Included'),
                ('extra_people','Extra People'),('minimum_nights','Minimum Nights'),('high_end_electronics','Electronics'),
                ('smoke_detector','Smoke Detector'), ('washing_machine','Washing Machine'),('heating', 'Heating'),('hair_dryer','Hair Dryer'), 
                ('hangers','Hangers'),('free_parking','Free_Parking'), ('gym','Gym'), ('tv','Tv'), ('kitchen','Kitchen'),
                ('workspace','Workspace'),('internet','Internet')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('neighbourhood_cleansed', 'Neighbourhood'),('bed_type','Bed Type'), ('property_type', 'Property Type'),
            ('room_type','Room Type'),('instant_bookable','Instant_bookable'),('cancellation_policy','Cancellation Policy')]

    plot = category_plot(cat_plot, cat_x, cat_y, estimator, hue)
    return render_template(
        # file yang akan menjadi response dari API
        'category.html',
        # plot yang akan ditampilkan
        plot=plot,
        # menu yang akan tampil di dropdown 'Jenis Plot'
        focus_plot=cat_plot,
        # menu yang akan muncul di dropdown 'sumbu X'
        focus_x=cat_x,
        focus_y=cat_y,

        # menu yang akan muncul di dropdown 'Estimator'
        focus_estimator=estimator,
        # menu yang akan tampil di dropdown 'Hue'
        focus_hue=hue,
        # list yang akan digunakan looping untuk membuat dropdown 'Jenis Plot'
        drop_plot= list_plot,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu X'
        drop_x= list_x,
        # list yang akan digunakan looping untuk membuat dropdown 'Sumbu Y'
        drop_y= list_y,
        # list yang akan digunakan looping untuk membuat dropdown 'Estimator'
        drop_estimator= list_est,
        # list yang akan digunakan looping untuk membuat dropdown 'Hue'
        drop_hue= list_hue
    )
def scatter_plot(cat_x, cat_y, hue):

    data = []

    for val in listings[hue].unique():
        scatt = go.Scatter(
            x = listings[listings[hue] == val][cat_x],
            y = listings[listings[hue] == val][cat_y],
            mode = 'markers',
            name = str(val)
        )
        data.append(scatt)

    layout = go.Layout(
        title= 'Scatter',
        title_x= 0.5,
        xaxis=dict(title=cat_x),
        yaxis=dict(title=cat_y)
    )

    result = {"data": data, "layout": layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/scatt_fn')
def scatt_fn():
    cat_x = request.args.get('cat_x')
    cat_y = request.args.get('cat_y')
    hue = request.args.get('hue')

    # WAJIB! default value ketika scatter pertama kali dipanggil
    if cat_x == None and cat_y == None and hue == None:
        cat_x = 'price'
        cat_y = 'cleaning_fee'
        hue = 'bed_type'

    # Dropdown menu
    list_x = [('price', 'Price'), ('bathrooms', 'Bathroom'), ('accommodates','Accommodates'),
                ('bedrooms','Bedroom'),('cleaning_fee','Cleaning Fee'),('availability_365','Available'),('guests_included','Guests Included'),
                ('extra_people','Extra People'),('minimum_nights','Minimum Nights'),('high_end_electronics','Electronics'),
                ('smoke_detector','Smoke Detector'), ('washing_machine','Washing Machine'),('heating', 'Heating'),('hair_dryer','Hair Dryer'), 
                ('hangers','Hangers'),('free_parking','Free_Parking'), ('gym','Gym'), ('tv','Tv'), ('kitchen','Kitchen'),
                ('workspace','Workspace'),('internet','Internet')]
    list_y = [('price', 'Price'), ('bathrooms', 'Bathroom'), ('accommodates','Accommodates'),
                ('bedrooms','Bedroom'),('cleaning_fee','Cleaning Fee'),('availability_365','Available'),('guests_included','Guests Included'),
                ('extra_people','Extra People'),('minimum_nights','Minimum Nights'),('high_end_electronics','Electronics'),
                ('smoke_detector','Smoke Detector'), ('washing_machine','Washing Machine'),('heating', 'Heating'),('hair_dryer','Hair Dryer'), 
                ('hangers','Hangers'),('free_parking','Free_Parking'), ('gym','Gym'), ('tv','Tv'), ('kitchen','Kitchen'),
                ('workspace','Workspace'),('internet','Internet')]
    list_hue = [('neighbourhood_cleansed', 'Neighbourhood'),('bed_type','Bed Type'), ('property_type', 'Property Type'),
            ('room_type','Room Type'),('instant_bookable','Instant_bookable'),('cancellation_policy','Cancellation Policy')]

    plot = scatter_plot(cat_x, cat_y, hue)

    return render_template(
        'scatter.html',
        plot=plot,
        focus_x=cat_x,
        focus_y=cat_y,
        focus_hue=hue,
        drop_x= list_x,
        drop_y= list_y,
        drop_hue= list_hue
    )
def pie_plot(hue = 'neighbourhood_cleansed'):
    
    vcounts = listings[hue].value_counts()

    labels = []
    values = []

    for item in vcounts.iteritems():
        labels.append(item[0])
        values.append(item[1])
    
    data = [
        go.Pie(
            labels=labels,
            values=values
        )
    ]

    layout = go.Layout(title='Pie', title_x= 0.48)

    result = {'data': data, 'layout': layout}

    graphJSON = json.dumps(result,cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/pie_fn')
def pie_fn():
    hue = request.args.get('hue')

    if hue == None:
        hue = 'neighbourhood_cleansed'

    list_hue = [('neighbourhood_cleansed', 'Neighbourhood'),('bed_type','Bed Type'), ('property_type', 'Property Type'),
            ('room_type','Room Type'),('instant_bookable','Instant_bookable'),('cancellation_policy','Cancellation Policy')]

    plot = pie_plot(hue)
    return render_template('pie.html', plot=plot, focus_hue=hue, drop_hue= list_hue)


#3 DATASET + PREDICTING
@app.route('/predict')
def prediction():
    listings= pd.read_csv("/Users/dennisherdi/data_science/FinalProject_PricePrediction_AirBnb/listings_cleaned.csv").head(100)
    listings.index.name = None
    titles = " "
    
    # data.to_html()
    return render_template('prediction.html', tables = [listings.to_html(classes = 'data', header = 'true')], titles = titles)

#4 Result
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form
        neighbourhood_cleansed = input['neighbourhood_cleansed']
        property_type=input['property_type']
        room_type=input['room_type']
        accommodates =int(input['accommodates'])
        bathrooms = float(input['bathrooms'])
        instant_bookable= input['instant_bookable']
        bedrooms = float(input['bedrooms'])
        bed_type=input['bed_type']
        beds = float(input['beds'])
        cleaning_fee = int(input['cleaning_fee'])
        availability_365 = int(input['availability_365'])
        guests_included = int(input['guests_included'])
        extra_people = int(input['extra_people'])
        minimum_nights = int(input['minimum_nights'])
        cancellation_policy=input['cancellation_policy']
        high_end_electronics = float(input['high_end_electronics'])    
        smoke_detector = float(input['smoke_detector'])
        washing_machine = float(input['washing_machine'])
        heating = float(input['heating'])
        hair_dryer = float(input['hair_dryer'])
        hangers = float(input['hangers'])
        tv = float(input['tv'])
        kitchen = float(input['kitchen'])
        workspace = float(input['workspace'])
        internet = float(input['internet'])
        df_predicts = pd.DataFrame({ neighbourhood_cleansed :input['neighbourhood_cleansed'],
            property_type:input['property_type'],
            room_type:input['room_type'],
            accommodates :int(input['accommodates']),
            bathrooms : float(input['bathrooms']),
            instant_bookable:input['instant_bookable'],
            bedrooms : float(input['bedrooms']),
            bed_type:input['bed_type'],
            beds : float(input['beds']),
            cleaning_fee : int(input['cleaning_fee']),
            availability_365 : int(input['availability_365']),
            guests_included : int(input['guests_included']),
            extra_people : int(input['extra_people']),
            minimum_nights : int(input['minimum_nights']),
            cancellation_policy:input['cancellation_policy'],
            high_end_electronics : float(input['high_end_electronics']) ,   
            smoke_detector : float(input['smoke_detector']),
            washing_machine : float(input['washing_machine']),
            heating : float(input['heating']),
            hair_dryer : float(input['hair_dryer']),
            hangers : float(input['hangers']),
            tv : float(input['tv']),
            kitchen : float(input['kitchen']),
            workspace : float(input['workspace']),
            internet : float(input['internet'])},index=[0])
                
        model = joblib.load('/Users/dennisherdi/data_science/FinalProject_PricePrediction_AirBnb/GBR_TUNED')

        data_pred = pd.DataFrame(data =[[neighbourhood_cleansed, property_type, room_type, accommodates,
        bathrooms,instant_bookable, bedrooms, bed_type, beds,
        cleaning_fee,availability_365,guests_included,extra_people,
        minimum_nights,cancellation_policy,high_end_electronics,smoke_detector,
        washing_machine,heating,hair_dryer,hangers,tv,kitchen,workspace,internet]],
		columns = ['neighbourhood_cleansed', 'property_type', 'room_type', 'accommodates',
       'bathrooms', 'instant_bookable', 'bedrooms', 'bed_type', 'beds',
       'cleaning_fee', 'availability_365', 'guests_included', 'extra_people',
       'minimum_nights', 'cancellation_policy','high_end_electronics', 'smoke_detector','washing_machine', 'heating','hair_dryer',
       'hangers','tv','kitchen', 'workspace', 'internet', ])
       
        prediksi = model.predict(data_pred)
        pred = prediksi[0]


        return render_template('result.html', 
        neighbourhood_cleansed= neighbourhood_cleansed,
        property_type= property_type,
        room_type= room_type,
        accommodates = accommodates,
        bathrooms = bathrooms,
        instant_bookable= instant_bookable,
        bedrooms = bedrooms,
        bed_type= bed_type,
        beds = beds,
        cleaning_fee =  cleaning_fee,
        availability_365 = availability_365,
        guests_included = guests_included,
        extra_people = extra_people,
        minimum_nights = minimum_nights,
        cancellation_policy= cancellation_policy,
        high_end_electronics = high_end_electronics,    
        smoke_detector = smoke_detector,
        washing_machine = washing_machine,
        heating = heating,
        hair_dryer = hair_dryer,
        hangers = hangers,
        tv = tv,
        kitchen = kitchen,
        workspace = workspace,
        internet = internet,
        pred = (np.expm1(pred).round(2))
        )

if __name__ == '__main__':
    model = joblib.load('/Users/dennisherdi/data_science/FinalProject_PricePrediction_AirBnb/GBR_TUNED')
    app.run(debug=True,port=1500)


