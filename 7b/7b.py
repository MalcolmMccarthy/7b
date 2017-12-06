'''
created by malcolm
in november 2017
for ics3u
this program does multiple math actions with random #s from an array, if the average is greater than 80, a special message will pop up
''' 
import ui
from numpy import random

number_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60,65, 70, 75, 80, 85, 90, 95, 100]

counter = 0
number_1 = random.choice(number_list)
number_2 = random.choice(number_list)
number_3 = random.choice(number_list)

def show_button(sender):
    view['random_number_label'].text = str(number_1) + ' ' + str(number_2) + ' ' + str(number_3)

def add_button(sender):
    add_total = int(number_1) + int(number_2) + int(number_3)
    view['add_label'].text = str(add_total)
    
def subtract_button(sender):
   subtract_total = int(number_1) - int(number_2) - int(number_3)
   view['subtract_label'].text = str(subtract_total)
   
def multiply_button(sender):
    multiply_total = int(number_1) * int(number_2) * int(number_3)
    view['multiply_label'].text = str(multiply_total)	

def average_button(sender):
    global counter
    while counter <= 0:
        total =  int(number_1) + int(number_2) + int(number_3)
        average_total = total / 3
        counter = counter + 1
        view['average_label'].text = str(average_total)
        if average_total > 80:
            view['special_label'].text = "congratulations! your average is over 80!"
        
view = ui.load_view()
view.present('sheet')
