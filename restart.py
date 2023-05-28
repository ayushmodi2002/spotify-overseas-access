import smtplib

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def restart():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('spotifylogbot@gmail.com','wrumlwfskiyfjzbr')

    reciever_email="ayushmodi04@gmail.com"

    subject='Raspberry Pi Restarted'
    body = '''
Dear User,
Your Raspberry pi just rebooted.
'''
    message="Subject: {} \n\n {}".format(subject,body)

    mail=server.sendmail('spotifylogbot@gmail.com',reciever_email,message)

    try:
        verify=server.verify(mail)
        if verify:
            print("Mail sent successfully!")
    except exception:
        print("error sending mail please report a bug")
    finally:
        server.quit()
restart()
