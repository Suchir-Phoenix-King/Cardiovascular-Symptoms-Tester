# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 17:38:16 2022

@author: PC_RC
"""

from tkinter import *
root = Tk()
root.title("Fever Report")
root.geometry("600x600")
root.configure(background = "red")

question1_radioButton = StringVar(value ="0")
Question1 = Label(root, text="Do you experience shortness of breath in daily activities?", bg = "red")
Question1.pack()
question1_r1 = Radiobutton(root, text = "yes", variable = question1_radioButton, value = "yes", bg = "red")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "no", variable = question1_radioButton, value = "no", bg = "red")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Do you have swelling in your feet/ankles/legs(shoes feel tighter)or abdomen?", bg = "red")
Question2.pack()
question2_r1 = Radiobutton(root, text = "yes", variable = question2_radioButton, value = "yes", bg = "red")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "no", variable = question2_radioButton, value = "no", bg = "red")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "Do you feel any of these symptoms - confusion, disorientation, loss of memory?", bg = "red")
Question3.pack()
question3_r1 = Radiobutton(root, text = "yes", variable = question3_radioButton, value = "yes", bg = "red")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "no", variable = question3_radioButton, value = "no", bg = "red")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")
Question4 = Label(root, text = "Do you experience shortness of breath while laying down or while at rest?", bg = "red")
Question4.pack()
question4_r1 = Radiobutton(root, text = "yes", variable = question4_radioButton, value = "yes", bg = "red")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "no", variable = question4_radioButton, value = "no", bg = "red")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")
Question5 = Label(root, text = "Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?", bg = "red")
Question5.pack()
question5_r1 = Radiobutton(root, text = "yes", variable = question5_radioButton, value = "yes", bg = "red")
question5_r1.pack()
question5_r2 = Radiobutton(root, text = "no", variable = question5_radioButton, value = "no", bg = "red")
question5_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+10
    if question2_radioButton.get()=="yes":
        score = score+10
    if question3_radioButton.get()=="yes":
        score = score+10
    if question4_radioButton.get()=="yes":
        score = score+10
    if question5_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if score <= 10:
        
        print("You don't need to visit the doctor")
    elif score > 10 and score <= 30:
        
        print("You perhaps might need to visit the doctor")
    else:
        
        print("You must visit the doctor")
        
btn = Button(root, text = "Get Results", command = fever_score)
btn.pack()
root.mainloop()