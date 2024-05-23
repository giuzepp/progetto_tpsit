from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/json')
def json():
    data = {
    "lista": [
        {
            "Country": "Italy",
            "Mfr_CommonName": "Fiat",
            "Mfr_Name": "Fiat Automobiles S.p.A.",
            "Year_Founded": 1899,
            "Founder": "Giovanni Agnelli",
            "Headquarters": "Turin, Italy",
            "Popular_Model": "Fiat 500"
        },
        {
            "Country": "Germany",
            "Mfr_CommonName": "BMW",
            "Mfr_Name": "Bayerische Motoren Werke AG",
            "Year_Founded": 1916,
            "Founder": "Franz Josef Popp",
            "Headquarters": "Munich, Germany",
            "Popular_Model": "BMW 3 Series"
        },
        {
            "Country": "Japan",
            "Mfr_CommonName": "Toyota",
            "Mfr_Name": "Toyota Motor Corporation",
            "Year_Founded": 1937,
            "Founder": "Kiichiro Toyoda",
            "Headquarters": "Toyota City, Japan",
            "Popular_Model": "Toyota Corolla"
        },
        {
            "Country": "USA",
            "Mfr_CommonName": "Ford",
            "Mfr_Name": "Ford Motor Company",
            "Year_Founded": 1903,
            "Founder": "Henry Ford",
            "Headquarters": "Dearborn, Michigan, USA",
            "Popular_Model": "Ford Mustang"
        },
        {
            "Country": "France",
            "Mfr_CommonName": "Renault",
            "Mfr_Name": "Renault S.A.",
            "Year_Founded": 1899,
            "Founder": "Louis Renault",
            "Headquarters": "Boulogne-Billancourt, France",
            "Popular_Model": "Renault Clio"
        },
        {
            "Country": "South Korea",
            "Mfr_CommonName": "Hyundai",
            "Mfr_Name": "Hyundai Motor Company",
            "Year_Founded": 1967,
            "Founder": "Chung Ju-Yung",
            "Headquarters": "Seoul, South Korea",
            "Popular_Model": "Hyundai Elantra"
        },
        {
            "Country": "United Kingdom",
            "Mfr_CommonName": "Jaguar",
            "Mfr_Name": "Jaguar Land Rover Automotive PLC",
            "Year_Founded": 1922,
            "Founder": "William Lyons",
            "Headquarters": "Coventry, England, UK",
            "Popular_Model": "Jaguar XF"
        },
        {
            "Country": "Sweden",
            "Mfr_CommonName": "Volvo",
            "Mfr_Name": "Volvo Car Corporation",
            "Year_Founded": 1927,
            "Founder": "Assar Gabrielsson and Gustav Larson",
            "Headquarters": "Gothenburg, Sweden",
            "Popular_Model": "Volvo XC90"
        },
        {
            "Country": "Italy",
            "Mfr_CommonName": "Ferrari",
            "Mfr_Name": "Ferrari N.V.",
            "Year_Founded": 1939,
            "Founder": "Enzo Ferrari",
            "Headquarters": "Maranello, Italy",
            "Popular_Model": "Ferrari 488"
        },
        {
            "Country": "Japan",
            "Mfr_CommonName": "Honda",
            "Mfr_Name": "Honda Motor Co., Ltd.",
            "Year_Founded": 1948,
            "Founder": "Soichiro Honda",
            "Headquarters": "Tokyo, Japan",
            "Popular_Model": "Honda Civic"
        },
        {
            "Country": "Germany",
            "Mfr_CommonName": "Mercedes-Benz",
            "Mfr_Name": "Mercedes-Benz Group AG",
            "Year_Founded": 1926,
            "Founder": "Karl Benz and Gottlieb Daimler",
            "Headquarters": "Stuttgart, Germany",
            "Popular_Model": "Mercedes-Benz C-Class"
        },
        {
            "Country": "USA",
            "Mfr_CommonName": "Tesla",
            "Mfr_Name": "Tesla, Inc.",
            "Year_Founded": 2003,
            "Founder": "Elon Musk, JB Straubel, Martin Eberhard, Marc Tarpenning, Ian Wright",
            "Headquarters": "Palo Alto, California, USA",
            "Popular_Model": "Tesla Model S"
        },
        {
            "Country": "France",
            "Mfr_CommonName": "Peugeot",
            "Mfr_Name": "Peugeot S.A.",
            "Year_Founded": 1810,
            "Founder": "Armand Peugeot",
            "Headquarters": "Paris, France",
            "Popular_Model": "Peugeot 208"
        },
        {
            "Country": "Germany",
            "Mfr_CommonName": "Volkswagen",
            "Mfr_Name": "Volkswagen AG",
            "Year_Founded": 1937,
            "Founder": "German Labour Front",
            "Headquarters": "Wolfsburg, Germany",
            "Popular_Model": "Volkswagen Golf"
        }
    ]
}

    #print(json)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)