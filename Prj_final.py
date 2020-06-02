# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 05:54:18 2019

@author: Akash
"""

from tkinter import * # Imported for the GUI
import os # Imported for file read write operations
import time # To add time pauses
import playsound # To play mp3 files
import speech_recognition as sr# for speech to text conversion
from gtts import gTTS # Google text to speech
 

 

 
def myfunction(): 
    """this is a user defined function which has the script for speech recognition and order generation
    It will be executed when the pushbutton is pressed"""
    
    
    label_2['text']="hello, what will you like to have?"
    
    string =""        # here, we define all the variables used in this function
    item_name = ""
    how_many = ""
    price = 0.0
    multiplier = 0.0
    total = 0.0
    item_to_cancel = ""
    
    
    def speak(text): # this function will convert the text passed as argument into an mp3 file and play it
        
        tts = gTTS(text=text, lang="en",slow=False) # Define an instance for the gTTS module.
        filename = "voice.mp3"
        
        tts.save(filename) # here, the mp3 file is saved as 'voice.mp3'
        playsound.playsound(filename) # this will play out the file
        os.remove(filename) # this will delete the file
    
    
    def get_audio(): # This function will be called to convert speech into a text string
        r = sr.Recognizer()# here, we create an instance for the SpeechRecognition module
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=100)# Take the speech input through the microphone.
            #It will wait for 100sec to receive an input, otherwise it will throw an error
            said = ""
    # Now, we use exception handling
            try:
                said = r.recognize_google(audio)# Use google speech recognition to convert the voice input to text
                #and save it as 'said'
                said = said.lower()# Convert the entire string to lower case for better processing
                
            except Exception: 
                label_2['text']="Didn't get that please try again"
                speak("Didn't get that please try again")
                #The following 2 lines are necessary to dynamically update the GUI labels
                screen.update_idletasks()
                screen.update()
                time.sleep(0.02)# wait for 0.02 secs    
        return said # the function will return 'said' which is a string
    # Now, we are done with the function definations , this is where the execution starts 
    label_2['text']="hello, what will you like to have?"
    screen.update_idletasks()
    screen.update()
   
    speak("hello, what will you like to have?")
    
    while(1):
# This is a continuous loop, the script inside will be executed again and again till a 'break' argument is given        

        text = get_audio()# get_audio() function is called here. It will return the string 'said' which is saved as 'text'
        
        if "like" in text or  "have" in text or "give" in text:# here, we see if the customer wants to record an order
                  
            for word in text.split():
            #Here, we split the string 'text' into a list. Each word in the list ...
            #..will be checked for the following conditions, one by one.
                if word == "fries" or word == "price":
                    text = text.replace(word, "")
                    item_name = "fries"
                if word == "burger" or word == "burgers" or word=="hamburger":
                    text = text.replace(word, "")
                    item_name = "burger"
                if word == "hotdog" or word == "hotdogs" or word == "dogs" or word == "dog":
                    text = text.replace(word, "")
                    item_name = "hotdog" 
                if word == "pizza" or word == "pizzas":
                    text = text.replace(word, "")
                    item_name = "pizza" 
                if word == "popcorn" or word == "popcorns" or word == "corns" or word == "corn":
                    text = text.replace(word, "")
                    item_name = "popcorn"
                if word == "icecream" or word == "icecreams" or word == "ice" or word == "cream":
                    text = text.replace(word, "")
                    item_name = "icecream"  
                if word == "coffee" or word == "coffees" :
                    text = text.replace(word, "")
                    item_name = "coffee" 
                if word == "drink" or word == "drinks" or word == "cola" or word == "coke":
                    text = text.replace(word, "")
                    item_name = "drinks"                    
                if word == "1" or word == "one":
                    text = text.replace(word, "")
                    how_many = "1"
                if word == "2" or word == "two" or word == "to":
                    text = text.replace(word, "")
                    how_many = "2"
                if word == "3" or word == "three":
                    text = text.replace(word, "")
                    how_many = "3"
                if word == "4" or word == "four":
                    text = text.replace(word, "")
                    how_many = "4"
                if word == "5" or word == "five":
                    text = text.replace(word, "")
                    how_many = "5"
                if word == "6" or word == "six":
                    text = text.replace(word, "")
                    how_many = "6"
                    
                if item_name != "" and how_many != "" :
                #only when both these conditions are satisfied, the item name and no. of items will be added to variable 'string'
                    string = string + item_name+"\n"+how_many+"\n"
                    item_name = "" #clear the variables
                    how_many = ""
                
            label_3['text']="Order Displayed Here:\n"+str(string) # display order on GUI lable 3
            screen.update_idletasks()
            screen.update()
            time.sleep(0.02)
            # The following loop is used for price calculation
            # We split the data in 'string' into a list
            for word in string.split():
                if word == "fries":                    
                    price = 9.50
                if word == "burger":                    
                    price = 10.99
                if word == "hotdog":                    
                    price = 11.50
                if word == "pizza":                   
                    price = 13.50
                if word == "popcorn":                    
                    price = 7.99
                if word == "icecream":                    
                    price = 8.99
                if word == "coffee":                    
                    price = 5.99
                if word == "drinks":                    
                    price = 5.99
                if word == "cancelled":                    
                    price = 0.00001
                if word == "1":                    
                    multiplier = 1
                if word == "2":                    
                    multiplier = 2
                if word == "3":                    
                    multiplier = 3
                if word == "4":
                    multiplier = 4
                if word == "5":                    
                    multiplier = 5
                if word == "6":                    
                    multiplier = 6

                if price != 0 and multiplier != 0 :#this condition will be satisfied only if both values for price and multiplier...
                    #...are available
                    total = round(total + (price*multiplier),2)# calculate total amount
                    price=0 # Clear values
                    multiplier=0
                    
            
            
            label_3['text']="Order Displayed Here:\n"+str(string)+"\nTotal="+str(total)# Display the total amount on the GUI lable 3
            label_2['text']="anything else?"
            screen.update_idletasks()
            screen.update()
            time.sleep(0.02)
            total=0
            speak("anything else?")
        
        #The following if loop is used for cancelling a perticular item:
        
        if "cancel" in text or "remove" in text:
            # Here, we find the item to cancel in the string given by the customer's voice input
            for word in text.split():
                if word == "fries" or word == "prize" or word == "price":
                    item_to_cancel = "fries"
                elif word == "burger" or word == "burgers" or word=="hamburger":
                    item_to_cancel = "burger"
                elif word == "hotdog" or word == "hotdogs" or word == "dogs" or word == "dog":
                    item_to_cancel = "hotdog"
                elif word == "pizza" or word == "pizzas":
                    item_to_cancel = "pizza"
                elif word == "popcorn" or word == "popcorns" or word == "corns" or word == "corn":
                    item_to_cancel = "popcorn"                    
                elif word == "icecream" or word == "icecreams" or word == "ice" or word == "cream":
                    item_to_cancel = "icecream"
                elif word == "coffee" or word == "coffees" :
                    item_to_cancel = "coffee" 
                elif word == "drink" or word == "drinks" or word == "cola" or word == "coke":
                    item_to_cancel = "drinks"                     
                    
            for word in string.split():
                # Here we find the item to cancel in 'string' and substitute it with the word 'cancelled'
                
                        
                if word == item_to_cancel:
                    string = string.replace(word,"cancelled")
                    speak("The item "+ item_to_cancel + "has been removed")
                
            total=0    
            
            
            #Now, we recalculate the tptal amount and print it
            for word in string.split():
                if word == "fries":                    
                    price = 9.50
                if word == "burger":                    
                    price = 10.99
                if word == "hotdog":                    
                    price = 11.50
                if word == "pizza":                   
                    price = 13.50
                if word == "popcorn":                    
                    price = 7.99
                if word == "icecream":                    
                    price = 8.99
                if word == "coffee":                    
                    price = 5.99
                if word == "drinks":                    
                    price = 5.99
                if word == "cancelled":# when the word 'cancelled' is detected, we set the price to an insifignicant amount...
                #... this will be like multiplying by 0 but it will also allow the 'price!=0' condition to be satisfied.                    
                    price = 0.00001
                if word == "1":                    
                    multiplier = 1
                if word == "2":                    
                    multiplier = 2
                if word == "3":                    
                    multiplier = 3
                if word == "4":
                    multiplier = 4
                if word == "5":                    
                    multiplier = 5
                if word == "6":                    
                    multiplier = 6
                if price != 0 and multiplier != 0 :
                    total = round(total + (price*multiplier),2)
                    price=0
                    multiplier=0    
            
            # the total is calculated and printed again
            label_3['text']="Order Displayed Here:\n"+str(string)+"\nTotal="+str(total)
            label_2['text']="anything else?"
            screen.update_idletasks()
            screen.update()
            time.sleep(0.2)
            speak("anything else?")
        #Here, we see if the customer is enquiring about a certain item on the menu
        elif "what" in text :
            for word in text.split():
                #Now we detect the name of the item
                if word == "hotdog" or word == "hotdogs" or word == "dogs" or word == "dog":
                    label_1['image'] = load1 # Here, we set the image of 'hotdog' to label 1
                    label_1['width'] = 700
                    label_1['height'] = 400
                    label_2['text']="Hotdog"
                    screen.update_idletasks()
                    screen.update()
                    #Now, the script will speak out the info about the perticular item
                    speak("The hot dog is our speciality. Its a grilled or steamed link-sausage sandwich where the sausage is served in the slit of a partially sliced ​​bun")
                    label_1['image'] = load # The image in label 1 is set back to the menu image
                    label_2['text']="anything else?"
                    screen.update_idletasks()
                    screen.update()
                    speak("anything else?")
                #The same things are repeated in case of 'hamburger'
                if word == "burger" or word == "burgers" or word=="hamburger":
                    label_1['image'] = load2
                    label_1['width'] = 700
                    label_1['height'] = 400
                    label_2['text']="Hamburger"
                    screen.update_idletasks()
                    screen.update()
                    speak("Our hamburgers are famous throughout the city, its a sandwich consisting of one or more cooked patties of ground meat.")
                    label_1['image'] = load
                    label_2['text']="anything else?"
                    screen.update_idletasks()
                    screen.update()
                    speak("anything else?")
        #Here, we detect if the customer wants to confirm the order
        elif "that" in text and "all" in text or "confirm" in text or "that is all" in text or "that's all" in text or "finished" in text or "that is on" in text or "no" in text:
                
                label_2['text']="Order confirmed. Your total amount is " + str(total)+" Dollars"
                screen.update_idletasks()
                screen.update()
                time.sleep(0.02)
                speak("Order confirmed. Your total amount is " + str(total)+" dollars. Have a nice day.")
                break # This will exit the continous loop while(1)
 

  
def main_screen(): #Function to define the main screen of the GUI
  global screen
  screen = Tk() #Create an instance called 'screen' for Tkinter
  
  #screen.geometry("800x700") ...We do not define the geometry as we want the screen size to be dynamic 
  global label_1 #We declare all the variables as 'global' since we want to access them from different functions
  global label_2
  global label_3
  global load
  global load1
  global load2
  screen.title("Technology Project Group 6")
  #Load images into variables
  load = PhotoImage(file="fastfood_img.png")
  load1 = PhotoImage(file="hot.png")
  load2 = PhotoImage(file="hamb.png")
  #Define labels
  label_1=Label(image=load, width = "700", height = "400")
  label_1.pack() #Used to create the widget on the GUI screen

  label_2=Label(screen,text = "", height = "2")
  label_2.pack()
  #Define Button
  Button(screen,text = "New Order", height = "2", width = "30", command = myfunction).pack()
  
  label_3=Label(screen,text = "Order Display :", bg = "white", width = "600", height = "200",anchor=N)
  label_3.pack()
  label_3.config(font=("Courier",15))
  label_2['text']="Waiting...."

 
  screen.mainloop() #Keeps updating the screen

main_screen() #Call function for main screen