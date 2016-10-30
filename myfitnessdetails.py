import sys
import time
from Tkinter import *
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
from email.Utils import COMMASPACE, formatdate
from email import Encoders

from datetime import date


today=date.today()

#print today

def value():
	num1.set(today)
	return
def value2():
	today=time.asctime(time.localtime(time.time()))
	num1.set(today)
	return


root=Tk()
root.title("Entry Detials")
root.geometry("800x300+0+0")
num1=StringVar()
radbtn=StringVar()

label_1=Label(root, text="Enter  Breakfast / Lunch \n Snacks /Dinner")
label_2=Label(root, text="Enter the food item")
label_date=Label(root, text="Todays Date")
label_Sodium=Label(root, text="Soduim")
label_Fat=Label(root, text="Fat")
label_Carbohydrate=Label(root, text="Carbohydrate")
label_Protein=Label(root, text="Protein")
label_water=Label (root, text="How Many Glasses of water have you had")
label_Calories=Label(root, text="What was the Calory intake?")

#display of the labels on the screen


label_date.grid(row=2,column=0,sticky=W)
label_1.grid(row=6,column=0,sticky=E)
label_2.grid(row=7,column=0,sticky=E)
label_Sodium.grid(row=8,column=1,sticky=E)
label_Fat.grid(row=9,column=1,sticky=E)
label_Carbohydrate.grid(row=10,column=1,sticky=E)
label_Protein.grid(row=11,column=1,sticky=E)
label_Calories.grid(row=12,column=1,sticky=E)
label_water.grid(row=15,column=1,sticky=E)

#declaration of the text boxes

entry_1=Entry(root)
entry_2=Entry(root)
Sodium=Entry(root)
Fat=Entry(root)
Carbohydrate=Entry(root)
Protein=Entry(root)
Water=Entry(root)
Calories=Entry(root)


#getting the entry to be done
entry_1.grid(row=6,column=1)
entry_2.grid(row=7,column=1)
Sodium.grid(row=8,column=2)
Fat.grid(row=9,column=2)
Carbohydrate.grid(row=10,column=2)
Protein.grid(row=11,column=2)
Calories.grid(row=12,column=2)
Water.grid(row=16,column=1)



txt_display=Entry(root, textvariable=num1)
txt_display.grid(row=2,column=1)
radiobutton_1=Radiobutton(root, text="Local time", variable=radbtn, value="local time", command=value2).grid(row=3,column=1)



button_ok=Button(root, text="OK")
button_ok.grid(row=21,column=1,sticky=W)

button_cancel=Button(root,text="Cancel")
button_cancel.grid(row=21, column=1)





filePath = "filehere"#my file path

From = 'fitness.unlimited2016@gmail.com'
To = 'harcharan1984@gmail.com'

msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = 'fitness detail'

msg.attach(MIMEText(Sodium.get,Protein.get,Calories.get))

try:
    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.starttls()
    smtp.login('fitness.unlimited2016@gmail.com', 'fitnessunlimited2016')
except:
    i = 1
else:
    i = 0

if i == 0:
    ctype, encoding = mimetypes.guess_type(filePath)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        fp = open(filePath)
        # Note: we should handle calculating the charset
        part = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'image':
        fp = open(filePath, 'rb')
        part = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(filePath, 'rb')
        part = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(filePath, 'rb')
        part = MIMEBase(maintype, subtype)
        part.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % filePath)
    msg.attach(part)
    try:
        smtp.sendmail(From, To, msg.as_string())
    except:
        print "Mail not sent"
    else:
        print "Mail sent"
    smtp.close()
else:
    print "Connection failed"

root.mainloop()


