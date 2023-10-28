import requests
import json


message_w = ""



############################################
##############################################

def air_q(lat, lng):
    url = 'https://airquality.googleapis.com/v1/currentConditions:lookup?key=API_KEY'
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
    return (category)


##########################################################################
def mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    URL_ADP = "https://www.pmb.ro/subordonate/administratii/menu-page/2"

    port = 587
    password = PASSWORD
    my_mail = EMAIL

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = my_mail
    msg['To'] = EMAIL2
    msg['Subject'] = "GreenPath!"

    # Attach the text part
    msg.attach(
        MIMEText(
            f"Subject:GreenPath!\n\nMultumim pentru ca ati contribuit la siguranta si aspectul orasului!\n\nPentru "
            f"mai multe infomatii va rugam sa accesati site-ul institutiei locale  {URL_ADP}",
            'plain'))

    # Attach the image part
    image_paths = ['/home/X/Documents/Projects2/Hackathon/hackathon-app/server/raport/v_emag.png', '/home/X/Documents/Projects2/Hackathon/hackathon-app/server/raport/v_guess.png', '/home/X/Documents/Projects2/Hackathon/hackathon-app/server/raport/v_penny.png']
    for path in image_paths:
        with open(path, 'rb') as file:
            img = MIMEImage(file.read())
            msg.attach(img)

    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.send_message(msg)


########################################################################
def wheather_check(lat,lng):
    global message_w

    api_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
    api_key = KEY
    latit = lat
    longi = lng

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
def sms(location, message_w):
    from twilio.rest import Client
    message = f"Constatarea dvs ce se afla :{location}, a ajuns la  noi,\nin cel ma scurt timp ne vom ocupa de problema!\n\nPentru ca faptele bune sunt rasplatite ,\nintra pe mail si vezi ce cadouri ti-am pregatit!\n\n{message_w}"
    account_sid = SID
    auth_token = TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12292672147',
        body=message,
        to=PHONE_NR)
    print(message.sid)


##############################################

#################################################################
def general_alert(location,lat,lng):
    wheather_check(lat,lng)
    sms(location, wheather_check(lat,lng))
    mail()




