import requests



def get_data(api_key, lat, lon):
    #api url with geo data and api key
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    #get the response with requests
    response = requests.get(url, verify=True)
    #convert to json
    dict_response = response.json()

    return dict_response

def get_temp(lat,lon):
    data = get_data('42bb1537c35ff2de934a7f9a7f6dfaa1',lat, lon)
    #temperature in celsius
    temp = data['main']['temp'] # temp from API is stored in kelvin
    celsius = round(temp - 273.15,2)  #calculate to celsius
    return celsius 


def get_wind_dir(lat,lon):

    data = get_data('42bb1537c35ff2de934a7f9a7f6dfaa1',lat, lon)
    #wind speed and degree
    wind = data['wind']
    wind_speed = wind['speed']
    wind_degree = wind['deg']
    

    return wind_degree

def get_wind_speed(lat,lon):
    data = get_data('42bb1537c35ff2de934a7f9a7f6dfaa1',lat, lon)
    #wind speed 
    wind = data['wind']
    wind_speed = wind['speed'] # in meter pro sekunde
    return wind_speed

def get_wind_bft(lat,lon):
    wind_speed = get_wind_speed(lat,lon) # in meter pro sekunde
    if wind_speed <= 0.2:
        bft = 0 #Windstille, Flaute
    elif wind_speed <=1.5:
        bft = 1 #leiser Zug
    elif wind_speed <= 3.3:
        bft = 2 #leichte Brise
    elif wind_speed <= 5.4:
        bft = 3 #schwache Brise
    elif wind_speed <= 7.9:
        bft = 4 # mäßige Brise
    elif wind_speed <= 10.7:
        bft= 5 #frische Brise, friscer Wind
    elif wind_speed <= 13.8:
        bft = 6 #starker Wind
    elif wind_speed <= 17.1:
        bft = 7 #steifer Wind
    elif wind_speed <= 20.7:
        bft = 8 #stürmischer Wind
    elif wind_speed <= 24.4:
        bft = 9 #Sturm
    else:
        bft = 10 #schwerer Sturm
    

    return bft

#geo data of loerrach
loe_lat = 47.6169
loe_lon = 7.6709

# replace XXX with your personal API key
api_key = '42bb1537c35ff2de934a7f9a7f6dfaa1'
