import requests
import json


def air_q(lat, lng):
    url = 'https://airquality.googleapis.com/v1/currentConditions:lookup?key=AIzaSyAbIP7DzmjSr0vta5i4dcDA9_8deC9ruXk'
    headers = {'Content-Type': 'application/json'}
    data = {
        "location": {
            "latitude": lat,
            "longitude": lng
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    json_response = response.json()

    category = json_response['indexes'][0]['category']
    # return(category)
    print(category)


lat = 44.4309909
lng = 26.1097773
air_q(lat, lng)

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
        MIMEText(f"Subject:GreenPath!\n\nMultumim pentru ca ati contribuit la siguranta si aspectul orasului!\nPentru mai multe infomatii va rugam sa accesati site-ul institutiei locale  {URL_ADP}",
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

def sms(message,locatie):
    from twilio.rest import Client
    message = f"Constatarea dvs ce se afla :{locatie} a ajuns la  noi,in cel ma scurt timp ne vom ocupa de problema!\nPentru ca faptele bune sunt rasplatite ,intra pe mail si vezi ce cadouri ti-am pregatit!"
    account_sid = 'ACbf1fe13d076ad16a26389696e4ab2cbc'
    auth_token = '6984a61e2f37cd6172978429c4c28e57'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12292672147',
        body=message,
        to='+40726608693')
    print(message.sid)
def garbage_alert(locatie):
    sms(locatie)
    mail()


def dangerus_alert(locatie):
    sms(locatie)
    mail()


def damaged_sidewalk(locatie):
    sms(locatie)
    mail()

##damaged_sidewalk("bucuresti")
mail()