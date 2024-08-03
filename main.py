import calendar                                   #for displaying the calendar of user's choice month and year
import pandas                                     #for displaying table of the events and dates
import csv                                        #file storing in csv format
events = []                                       #empty events list

def display():                                    #method to display program
    print("")
    print("******EVENT MANAGING PROGRAM******")

def display_calendar(year, month):                #method to display calendar
    print("")
    print("------DISPLAYING CALENDAR-------")
    print(calendar.month(year, month, w = 1, l =1 ))
    print("")

def save_events():
    df = pandas.DataFrame(events)
    df.to_csv("events.csv", index=False)

def add_event():                                  #method to add event
    try:                                          #exception handling
        month = int(input("Enter the month number, you wanna add event in:"))
        year = int(input("Enter the year:"))
        display_calendar(year, month)
    except Exception as er:
        print(er)
    event_name = input(("Enter the event name:-"))
    event_date = input(("Enter the D/M/Y of the event:-"))
    events.append({"Event name": event_name, "Event Date" : event_date})
    save_events()
                                                  #adding events in the form of dictionary to the list of events
def delete_event():                               #method to delete any event based on he index in the list 
    print("")
    display_events(events)
    try:                                          #exception handling
        event_del = int(input("Enter the Event number you want to delete(0,1,2,3...):"))
        events.pop(event_del)
        save_events()
    except Exception as er:
        print("Event is not there",er)
    
def display_events(events):                       #method to display the events using pandas                     
    print("")
    if events:                              #checking if the events is not empty
        events_table = pandas.DataFrame(events)
        print(events_table)
    else:
        print("Empty Events list!")

try:                                              #Loading the events from the csv file, but if you are running the program without having file, error is handled!
    file_data = pandas.read_csv("events.csv")
    events =file_data.to_dict(orient="records")
except FileNotFoundError:
    print("Enter Events first!")                  #enter data and then if you run program, it will load the data from the file into events
except Exception as er:
    print("An error occurred while loading events:", er)

while True:                                       #running program
    display()                                     #user's choice
    ch = input('''
Your choice:- "a"dd,
              "d"isplay,
              "D"elete,
              "q"uit        ''')
    if ch == "a":                                #calling methods according to the User's choice
        add_event()
    elif ch == "d":
        display_events(events)
    elif ch == "D":
        delete_event()
    elif ch == "q" or ch =="Q":
        print("Exiting from the program!! Thankyou")
        exit()                                   #exiting program
    else:
        print("Choice is invalid!!")



