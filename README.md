# Air BnB Boston Price Prediction


# Business Understanding

Airbnb adalah perusahaan pasar online persewaan liburan Amerika yang berbasis di San Francisco, California. Airbnb mengelola dan menyelenggarakan pasar, yang dapat diakses oleh konsumen di situs web atau aplikasinya. Pengguna dapat mengatur penginapan, terutama homestay, dan pengalaman pariwisata atau membuat daftar kamar cadangan, properti, atau bagian darinya untuk disewa. Di sisi lain, pengguna yang sedang bepergian mencari properti pencarian penginapan dan kamar berdasarkan lingkungan atau lokasi. Airbnb merekomendasikan harga terbaik di lingkungan tersebut dan pengguna memesan harga terbaik.Saya mendapat kesempatan untuk menganalisis daftar kota <b>`BOSTON`</b> di Airbnb. Dataset listing <b>`BOSTON`</b> Airbnb memiliki berbagai fitur seperti lneighborhood, property_type, bedrooms, bathrooms, beds, price, reviews, ratings, etc. Akan menarik untuk melihat fitur apa yang mempengaruhi harga di kota <b>`BOSTON`</b> dan menarik kesimpulan yang menarik. Saya akan lebih tertarik untuk melatih dan mengevaluasi model dan melihat performa model saat memprediksi harga di kota <b>`BOSTON`</b> di Airbnb. Tujuan utama saya adalah sebagai berikut  

* Menetukan prediksi harga sewa untuk host yang ingin menyewakan property di Air Bnb di kota <b>`BOSTON`</b>
* Bagaimana algoritme pembelajaran mesin digunakan dalam memprediksi harga sewa?


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
|security_deposit|biaya deposit yang ditentukan host untuk keamanan. Apabila ada terjadi sesuatu, uang tersebut digunakan untuk membayarnya. exp: setrika dirusak pengunjung, maka biaya ganti rugi ditanggung deposit ini. Apabila tidak ada apa-apa, uang akan dikembalikan saat selesai menginap|
|minimum_nights|minimum malam untuk menginap|
|availability_365| jumlah ketersediaan listing per hari dalam setahun|
|guests_included|jumlah perkiraan dapat menampung tamu. ada denda bila melebihi yang ditentukan|
|cancellation_policy|kebijakan pembatalan, biasanya ada maksimum hari untuk pembatalan apabila ingin refund. 7 hari sebelum tanggal menginap. bila lebih dari itu maka uang tidak bisa dikembalikan|
|price(TARGET)|harga listing|
|instant_bookable| apakah cara pemesanan property kepada hostnya dapat secara langsung atau membutuhkan persetujuan terlebih dahulu sebelum melakukan pemesanan
|extra_people|harga per tamu tambahan di atas harga yang termasuk tamu|



# Machine Learning Model


##  Models used*

The models used in this analysis can be grouped in three different types: (1) **linear models**, (2) **tree-based models** and (3) **clustering-like models**. There is a total of **6 models** used. 

##### **1. Linear models**

- ``LinearRegression`` Analisis Regresi Linear Sederhana – Regresi Linear Sederhana adalah Metode Statistik yang berfungsi untuk menguji sejauh mana hubungan sebab akibat antara Variabel Faktor Penyebab (X) terhadap Variabel Akibatnya. Faktor Penyebab pada umumnya dilambangkan dengan X atau disebut juga dengan Predictor sedangkan Variabel Akibat dilambangkan dengan Y atau disebut juga dengan Response. Regresi Linear Sederhana atau sering disingkat dengan SLR (Simple Linear Regression) juga merupakan salah satu Metode Statistik yang dipergunakan dalam produksi untuk melakukan peramalan ataupun prediksi tentang karakteristik kualitas maupun Kuantitas.


##### **2. Tree-based models**

- ``DecisionTreeRegressor`` Pohon keputusan membangun model regresi atau klasifikasi dalam bentuk struktur pohon. Ini memecah kumpulan data menjadi himpunan bagian yang lebih kecil dan lebih kecil sementara pada saat yang sama pohon keputusan terkait dikembangkan secara bertahap. Hasil akhirnya adalah pohon dengan simpul keputusan dan simpul daun [2]. Dalam konteks regresi, maka decision tree adalah regresi yang bersifat non-linear dan non-kontinu (diskret). maka ia adalah teknik pengambilan keputusan dengan analogi sebuah pohon memiliki banyak cabang/ akar. Di mana satu cabang akan bercabang lagi, kemudian bercabang lagi, dan seterusnya.

- ``GradientBoostingRegressor`` "Meningkatkan" dalam pembelajaran mesin adalah cara menggabungkan beberapa model sederhana ke dalam satu model komposit. Ini juga mengapa penguat dikenal sebagai model aditif, karena model sederhana (juga dikenal sebagai pembelajar lemah) ditambahkan satu per satu, sambil mempertahankan struktur yang ada dalam model tidak berubah. Saat kami menggabungkan semakin banyak model sederhana, model akhir yang lengkap menjadi prediktor yang lebih kuat. Istilah "gradien" dalam "peningkatan gradien" berasal dari fakta bahwa algoritme menggunakan penurunan gradien untuk meminimalkan kerugian.

- ``RandomForestRegressor`` Random forests or random decision forests are metode pembelajaran ansambel untuk klasifikasi, regresi, dan tugas lain yang beroperasi dengan membangun banyak pohon keputusan pada waktu pelatihan dan mengeluarkan kelas yang merupakan mode kelas (klasifikasi) atau prediksi rata-rata / rata-rata ( regresi) dari masing-masing pohon.

- ``XGBRegressor`` XGBoost adalah singkatan dari "Extreme Gradient Boosting", di mana istilah "Gradient Boosting" berasal dari kertas Pendekatan Fungsi Greedy: A Gradient Boosting Machine, oleh Friedman. XGBoost digunakan untuk masalah pembelajaran yang diawasi, di mana kami menggunakan data pelatihan (dengan beberapa fitur) $ x_i $ untuk memprediksi variabel target $ y_i $ [4].

##### **3. Clustering-like models**

- ``KNeighborsRegressor`` Regression based on *k-nearest neighbors*. Target diprediksi dengan interpolasi lokal dari target yang terkait dengan tetangga terdekat dalam set pelatihan.

## Metrics choosed to validate the models*
metrik yang digunakan untuk mengevaluasi model regresi adalah:

- **$R^2$** - Proporsi varian dalam variabel dependen yang dapat diprediksi dari variabel independen. Skor terbaik adalah 1.0 dan bisa negatif (karena model bisa menjadi lebih buruk secara sewenang-wenang). Model konstan yang selalu memprediksi nilai yang diharapkan dari y, dengan mengabaikan fitur masukan, akan mendapatkan skor R ^ 2 sebesar 0,0 
**$R^2$** Merupakan koefisien determinasi berganda dan metode untuk menemukan subset variabel independen yang paling baik memprediksi variabel dependen dengan regresi linier. Metode selalu mengidentifikasi model terbaik sebagai model dengan yang terbesar untuk setiap jumlah variabel yang dipertimbangkan.


# Summary
The goal of the project is to find out which feature mostly affects the candidate decision of staying or leaving the company. 


