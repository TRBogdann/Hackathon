import requests
import json

lat = 44.4309909
lng = 26.1097773
message_w = ""
############################################
def wheather_check():

    api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
    api_key = "40aed1c3553094108ea8f9c83af1bdad"
    latit = str(lat)
    longi = str(lng)

    parameters = {
        "lat": latit,
        "lon": longi,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }

    request = requests.get(url=api_endpoint, params=parameters)
    request.raise_for_status()
    data = request.json()
    need_umbrella = False
    for hours in range(0, 5):
        id = data["hourly"][hours]["weather"][0]["id"]
        if int(id) < 700:
            need_umbrella = True

    if need_umbrella:
        print("take an umbrella with you!")
        message_w = "Vor urma precipitatii!"
    else:
        print("leave the umbrella home!")
        message_w = "Plimbare placuta!Vremea va fi super!"


##############################################

def air_q(lat, lng):
    url = 'https://airquality.googleapis.com/v1/currentConditions:lookup?key=AIzaSyAbIP7DzmjSr0vta5i4dcDA9_8deC9ruXk'
    headers = {'Content-Type': 'application/json'}
    data = {
        "location": {
            "latitude": lat,
            "longitude": lng
        },
        "languageCode": "ro"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    json_response = response.json()

    category = json_response['indexes'][0]['category']
    print(category)
    print(json_response)
    return(category)




##########################################################################
def mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    URL_ADP = "https://www.pmb.ro/subordonate/administratii/menu-page/2"
    # message = f"Subject:GreenPath!\n\nMultumim pentru ca ati contribuit la siguranta si aspectul orasului!\nPentru mai multe infomatii va rugam sa accesati site-ul institutiei locale  {URL_ADP}".encode(
    #             "utf-8")
    port = 587
    password = "kndvhremlmvewufj"
    my_mail = "zoicatrade@gmail.com"

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = my_mail
    msg['To'] = "eduardmusic12@gmail.com"
    msg['Subject'] = "GreenPath!"

    # Attach the text part
    msg.attach(
        MIMEText(
            f"Subject:GreenPath!\n\nMultumim pentru ca ati contribuit la siguranta si aspectul orasului!\n\nPentru mai multe infomatii va rugam sa accesati site-ul institutiei locale  {URL_ADP}",
            'plain'))

    # Attach the image part
    image_paths = ['v_emag.png', 'v_guess.png', 'v_penny.png']
    for path in image_paths:
        with open(path, 'rb') as file:
            img = MIMEImage(file.read())
            msg.attach(img)

    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.send_message(msg)


########################################################################
def wheather_check():
    global message_w

    api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
    api_key = "40aed1c3553094108ea8f9c83af1bdad"
    latit = str(lat)
    longi = str(lng)

    parameters = {
        "lat": latit,
        "lon": longi,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }


    request = requests.get(url=api_endpoint, params=parameters)
    request.raise_for_status()
    data = request.json()
    need_umbrella = False
    for hours in range(0, 5):
        id = data["hourly"][hours]["weather"][0]["id"]
        if int(id) < 700:
            need_umbrella = True

    if need_umbrella:
        print("take an umbrella with you!")
        message_w = "Vor urma precipitatii!"
        return message_w
    else:
        print("leave the umbrella home!")
        message_w = f"Plimbare placuta!Vremea va fi super!\nStare aer:{air_q(lat, lng)}!"
        return message_w


####################################################################
def sms(location,message_w):
    from twilio.rest import Client
    message = f"Constatarea dvs ce se afla :{location}, a ajuns la  noi,\nin cel ma scurt timp ne vom ocupa de problema!\n\nPentru ca faptele bune sunt rasplatite ,\nintra pe mail si vezi ce cadouri ti-am pregatit!\n\n{message_w}"
    account_sid = 'ACbf1fe13d076ad16a26389696e4ab2cbc'
    auth_token = '7b2138c4c89cf3964ca5dc3b37473802'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12292672147',
        body=message,
        to='+40726608693')
    print(message.sid)


##############################################

#################################################################
def garbage_alert(location):
    wheather_check()
    sms(location,wheather_check())
    mail()


def dangerus_alert(location):
    wheather_check()
    sms(location, wheather_check())
    mail()


def damaged_sidewalk(location):
    wheather_check()
    sms(location, wheather_check())
    mail()

garbage_alert("bucuresti")
