from logging import exception
import smtplib

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def successmail(username):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('spotifylogbot@gmail.com','wrumlwfskiyfjzbr')
    
    reciever_email=['ayushmodi04@gmail.com',username]
    
    subject='Verification SUCCESSFUL' 

    
    tuple=""" 
Dear user,
Login from origin country verification of  """,username
    string1=convertTuple(tuple)
    string2="""  is successful. Continue Enjoying your Free spotify account overseas.
    
if you like my work support me on github https://github.com/ayushmodi2002 
"""
    string=string1+string2
    body = string
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


def unsuccessmail(username):
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('spotifylogbot@gmail.com','wrumlwfskiyfjzbr')
    
    reciever_email=['ayushmodi04@gmail.com',username]
    
    subject='Verification UNSUCCESSFUL' 

    
    tuple=""" 
Dear user,
Login from origin country verification of  """,username
    string1=convertTuple(tuple)
    string2=""" 
is UNSUCCESSFUL. Please send a request to retry again.  
  
Report a bug to me on github https://github.com/ayushmodi2002 
"""
    string=string1+string2
    body = string
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
def startup():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login('spotifylogbot@gmail.com','wrumlwfskiyfjzbr')
    
    reciever_email="ayushmodi04@gmail.com"
    
    subject='script started running'
    body = '''
Dear User,
Your script is running successfully
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
