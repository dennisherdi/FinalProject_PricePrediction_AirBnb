# Air BnB Boston Price Prediction

This project is made to pass the Job Connector program in the Purwadhika Data Science course. The scope of this project is to create a local web page to predict the recommended rental price to the user. 

<hr>

<h3>Goals</h3>
The goals of this project are: 
1. 1. Helping users to predict their rental prices before becoming hosted on AIRBNB

<hr>


# Data Understanding

I am selecting Boston AirBnB listings as my dataset for the study. It is available on Kaggle https://www.kaggle.com/airbnb/boston. Listings dataset has various features/columns such as neighborhood, property_type, bedrooms, bathrooms, beds, price, reviews, ratings, etc.

## Features Use

|Feature|Description|
|--------------|--------------------------------------------------------------------|
|neighbourhood_cleansed|lokasi listing tersebut berada / distrik|
|property_type|tipe properti dari listing. exp: House/ Apartment/ ...|
|room_type|tipe ruangan dari listing (Entire home/apt, Private room, or Shared room)|
|accommodates|jumlah orang yang listing dapat akomodasikan|
|bathrooms|jumlah bathrooms|
|bedrooms|jumlah bedrooms|
|beds|jumlah tempat tidur|
|amenities|perlengkapan yang ditawarkan host untuk pengunjungnya. exp: Air Conditioning, Refrigerator, Wifi, ....|
|cleaning_fee|biaya yang ditentukan host untuk bersih-bersih|
|minimum_nights|minimum malam untuk menginap|
|availability_365| jumlah ketersediaan listing per hari dalam setahun|
|guests_included|jumlah perkiraan dapat menampung tamu. ada denda bila melebihi yang ditentukan|
|cancellation_policy|kebijakan pembatalan, biasanya ada maksimum hari untuk pembatalan apabila ingin refund. 7 hari sebelum tanggal menginap. bila lebih dari itu maka uang tidak bisa dikembalikan|
|price(TARGET)|harga listing|
|instant_bookable| apakah cara pemesanan property kepada hostnya dapat secara langsung atau membutuhkan persetujuan terlebih dahulu sebelum melakukan pemesanan
|extra_people|harga per tamu tambahan di atas harga yang termasuk tamu|




## Insights developed
- Daftar harga yang paling umum berada dalam kisaran 50-200 USD dengan harga tertinggi 4000 dolar.

-kota yang populer belum tentu menjadikan harga yang tertinggi, dapa di lihat perpopuler adalah Jamaica Plan tetapi kota yang termahal Bay Village.

-Seluruh Rumah adalah tipe kamar yang sangat padat diikuti oleh kamar Pribadi dan Bersama.

-Bay Village dan Leather District adalah yang paling mahal. Daftar Back Bay memiliki kisaran harga rata-rata 270 dolar, sedangkan Leather District memiliki 250 dolar.

-Back Bay memiliki jumlah listing Seluruh Rumah dan Kamar Bersama yang tinggi. Brooklyn memiliki pemesanan kamar pribadi yang tinggi.

-minimum night tertinggi terlihat pada kota yang terpoper yaitu Jamaica Plan 75% dari harga listing di bawah 300 dolar.

-data menunjukkan tren umum ketika tipe kamar adalah Seluruh rumah / apartemen, harga umumnya lebih tinggi sementara lebih sedikit untuk kamar bersama.

-jumlah akomodasi yang sering mencantumkan pada listings sebanyak 12 orang.

-minimum night terbanyak menempatkan pada room tipe jenis entire house/apt.

-cancel fee terbesar terdapat pada lokasi Bay village dengan Rata-rata 100 dolar.

-High end electronics , tv, dan heating menempati fasilitas yang menunjukan perbedaan harga yg jauh di banding kna tidak memakai fasilitas tersebut.

- extra people fee terbesar terlihat di kota Leather District,dengan rata-rata di atas kota lain dengan yg di bawah 20 dolar.

 
## Results Analysis
<hr>
<h3>Model Interfaces</h3>

__Home Page__
![home](/img/visual.png)

__Predictions__
![predictions](/img/prediction.png)

__dataset__
![dataset](/img/dataset.png)


