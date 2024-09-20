import os
import pywhatkit as pyw
from twilio.rest import Client
from googlesearch import search
import smtplib
import schedule
import time
import cv2
import pyudev as py
from datetime import datetime
import numpy as np
import boto3
import playsound
import google.generativeai as gen
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto
import pandas
from sklearn.linear_model import LinearRegression
import numpy
import joblib






print("""
      You can run these things:

        Browser
        Files
        sms/text
        call
        mail
        google
        schedule email
        ip camera
        face replace
        USB
        multi (sms)
        vlc
        multiwhatsapp
        train 
        budget alexa
        AI marks predictor
        play dino game with gestures


        type 'quit' or 'exit' to exit program

""")


while True:


    flag = input("What do you want to do? \n >>>")


    if(("browser"in flag or "firefox" in flag) and not ("dont" in flag or "not" in flag)):

        os.system("firefox &")


    elif(("file manager"in flag or "files" in flag or "dolphin" in flag)and not ("dont" in flag or "not" in flag)):

        os.system("dolphin &")


    elif(("sms"in flag or "text" in flag)and not ("dont" in flag or "not" in flag)):

    

        
        account_sid = 'sid'
        auth_token = 'token'

    
        
        def send_sms_message(to_number, message):
            
            client = Client(account_sid, auth_token)
            client.messages.create(body=message,
                                from_='+number',  
                                to=to_number)

        
        def main():
            while True:
                
                
                to_number = '+number'
             

                
                
        
                message = input("Enter message to send: ")
                send_sms_message(to_number, message)
                print("SMS message sent successfully!")
                break
                
        
        main()


    elif(("call" in flag) and not ("dont" in flag or "not" in flag)):

        
        account_sid = 'sid'
        auth_token = 'token'

        number = "number"
        number = "+91" + number
        client = Client(account_sid, auth_token)

        
        call = client.calls.create(
            twiml='<Response><Say>hi  how are you </Say></Response>',
            to=number,  
            from_='+number'  
        )

        print("ring ring")


    elif(("mail" in flag or "email" in flag) and not ("dont" in flag or "not" in flag)):

        s = smtplib.SMTP('smtp.gmail.com', 587)


        msg = input("Enter your message: ")
        sender = "mail@gmail.com"
        reciever = input("Enter reciever email: ")

        s.starttls()

        s.login(sender, "app pass")

        s.sendmail(sender, reciever, msg)

        s.quit()    


    elif(("search" in flag or "google" in flag) and not ("dont" in flag or "not" in flag)):

        query = input("Enter your search: ")

        for j in search(query, num = 5, stop = 5):
            print(j)    


    elif(("sched" in flag or "schedule" in flag) and not ("dont" in flag or "not" in flag)):
    

            
        def send_email( body, to_email):
            
            from_email = "mail@gmail.com"
            from_password = "app pass" 
            smtp_server = "smtp.gmail.com"
            smtp_port = 587  


            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls() 
            server.login(from_email, from_password)
            server.sendmail(from_email, to_email, body)
            server.quit()
            print("Email sent to successfully!")

        
        body_t= input("Enter your message: ")
        reciever = input("Enter reciever Email: ")
        timeing = input("Enter your time: ")
        schedule.every().day.at(timeing).do(send_email, body_t, reciever)

        
        while True:
            schedule.run_pending()
            time.sleep(10) 


    elif(("cam" in flag or "camera" in flag) and not ("dont" in flag or "not" in flag)):
        

        cap = cv2.VideoCapture("https://100.85.10.139:8080/video")
        while True:
            status, photo = cap.read()
            cv2.imshow("videowu", photo)
            if cv2.waitKey(10) == 13:
                break


        cv2.destroyAllWindows()
            

    elif(("replace" in flag or "face" in flag) and not ("dont" in flag or "not" in flag)):



        print("press 1 for picture")

        flag = int(input())

        if flag == 1:
            
            cap = cv2.VideoCapture(0)
            status1, photo1 = cap.read()
            cap.release()
            
        print("press 2 for another picture")            

        flag = int(input())

        if flag == 2:
            cap = cv2.VideoCapture(0)
            status2, photo2 = cap.read()
            cap.release()
            
            
        photo1[200:400, 200:400] = photo2 [200:400, 200:400]


        cv2.imshow("yes", photo1)
        cv2.waitKey(12000)
        cv2.destroyAllWindows()

        cap.release()
                

    elif(("usb" in flag or "USB" in flag) and not ("dont" in flag or "not" in flag)):


        def pic():
            date = datetime.now()
            cap = cv2.VideoCapture(0)
            status, photo = cap.read()
            cv2.imwrite(date.strftime("%H:%M:%S")+ ".png", photo)
            print("!!!PIC TAKEN!!!")
            cap.release()


        context = py.Context()
        monitor = py.Monitor.from_netlink(context)
        monitor.filter_by("usb")

        for devices in iter(monitor.poll, None):
            pic()


    elif(("exit" in flag or "quit" in flag) and not ("dont" in flag or "not" in flag)):
        break


    elif(("multiple" in flag or "multi" in flag) and not ("dont" in flag or "not" in flag)):

        def collect_data(num_team_members):
            data = []
            for i in range(num_team_members):
                print(f"Collecting data for team member {i+1}:")
                name = input("Enter Name: ")
                city = input("Enter City: ")
                college = input("Enter College: ")
                whatsapp_number = input("Enter Whatsapp Number: ")
                life_purpose = input("Enter Life Purpose (in max 5 words): ")
                data.append([name, city, college, whatsapp_number, life_purpose])
            return np.array(data)

        # Function to send SMS using Twilio
        def send_sms_twilio(recipient_number, message_body):
            # Replace with your Twilio Account SID, Auth Token, and Twilio phone number
            account_sid = 'sid'
            auth_token = 'toekn'
            twilio_phone_number = '+number'

            # Initialize Twilio client
            client = Client(account_sid, auth_token)

            try:
                # Send SMS
                message = client.messages.create(
                    body=message_body,
                    from_=twilio_phone_number,
                    to=recipient_number
                )
                print(f"SMS sent successfully to {recipient_number}. SID: {message.sid}")
            except Exception as e:
                print(f"Error sending SMS to {recipient_number}: {str(e)}")

        # Collect data from 5 team members
        num_team_members = 2
        team_data = collect_data(num_team_members)

        # Print collected data
        print("\nCollected Data:")
        print("Name\t\tCity\t\tCollege\t\tWhatsapp Number\t\tLife Purpose")
        for row in team_data:
            print("\t\t".join(row))

        # Send SMS to team members not from Jaipur
        message = "Welcome to Pink City, Jaipur"
        for member in team_data:
            name, city, whatsapp_number = member[0], member[1], member[3]
            if city.strip().lower() != 'jaipur':
                send_sms_twilio(whatsapp_number, message)

      
    elif(("vlc" in flag or "cvlc" in flag) and not ("dont" in flag or "not" in flag)):

        name_mov = input("Enter movie name: ")
        os.system("cvlc ~/Documents/LunixWorld/Pytjon/" + name_mov)


    elif(("multiwhatsapp" in flag) and not ("dont" in flag or "not" in flag)):

        def collect_data():
            data = []
            for i in range(2):
                print(f"Collecting data for team member {i+1}:")
                name = input("Enter Name: ")
                city = input("Enter City: ")
                college = input("Enter College: ")
                whatsapp_number = input("Enter Whatsapp Number: ")
                whatsapp_number = "+91" + whatsapp_number
                life_purpose = input("Enter Life Purpose (in max 5 words): ")
                
                # Append the collected data as a list to the data array
                data.append([name, city, college, whatsapp_number, life_purpose])
            
            return np.array(data)

        # Collect the data
        team_data = collect_data()

        # Print the data in table format
        print("\nCollected Data:")
        print("Name\t\tCity\t\tCollege\t\tWhatsapp Number\t\tLife Purpose")
        for row in team_data:
            print("\t\t".join(row))

        subarray = team_data[:,3]
        print(subarray)
        for i in subarray:
            pyw.sendwhatmsg_instantly(i, "ghffghg")


    elif(("train" in flag) and not ("dont" in flag or "not" in flag)):

        os.system("sl -G")


    elif (("alexa" in flag) and not ("dont" in flag or "not" in flag)):

      

        src = input("Enter your source language code: ")
        tar = input("Enter your target language code: ")

        src_text = input("Enter your text: ")



        trans = boto3.client(service_name = "translate", use_ssl = True, region_name = "ap-south-1", aws_access_key_id = "key",
                                aws_secret_access_key = "secretkey")

        result = trans.translate_text(Text = src_text, SourceLanguageCode = src, TargetLanguageCode = tar)

        out = result.get("TranslatedText")

        prompt = out



        gen.configure(api_key="api key")

        model = gen.GenerativeModel('gemini-1.5-flash')

        answer = model.generate_content( prompt)

        generated_text = answer._result.candidates[0].content.parts[0].text






        polly_client = boto3.Session(
                            region_name = "ap-south-1", 
                            aws_access_key_id = "key",
                            aws_secret_access_key = "secret key").client('polly')

        response = polly_client.synthesize_speech(VoiceId='Kajal',
                        OutputFormat='mp3', 
                        Text = generated_text,
                        Engine = 'neural        ',
                        LanguageCode ="hi-IN")

        file = open('speech.mp3', 'wb')
        file.write(response['AudioStream'].read())
        file.close()


        playsound.playsound("speech.mp3")


    elif (("dinosaur" in flag or "dino" in flag) and not ("dont" in flag or "not" in flag)):

            
        cap = cv2.VideoCapture(0)
        detector = HandDetector(detectionCon=0.8, maxHands=1)
        while True:
            # Get image frame
            success, img = cap.read()
            hands, img = detector.findHands(img, draw=True)
            if hands:
            # Hand 1
                hand1 = hands[0]
                HandLandMarkList1 = hand1["lmList"]  # List of 21 Landmark points
                length,info,frame = detector.findDistance(HandLandMarkList1[4][0:2],HandLandMarkList1[8][0:2],img)
                length = round(length)
            
                if length<25:
                    auto.press('up')
            
            cv2.imshow("Image", img)
            if cv2.waitKey(1) == ord('q'):
                break


        cap.release()
        cv2.destroyAllWindows()


    elif (("marks" in flag or "ai" in flag) and not ("dont" in flag or "not" in flag)):
    


        db = pandas.read_csv("/home/jay2/Documents/LunixWorld/Pytjon/pandaman.txt")

        y = db["marks"]
        x = db["hours"]
        x = x.values.reshape(-1, 1)

        brain = LinearRegression()

        brain.fit(x,y)

        joblib.dump(brain, "brain_model")

        print(brain.predict([[1]]))


    