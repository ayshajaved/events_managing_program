import calendar                                   #for displaying the calendar of user's choice month and year
import pandas                                     #for displaying table of the events and dates
import csv                                        #file storing in csv format

class events_managing_program():
    def __init__(self):
        self.events = [] 
        self.load_events()
    def load_events(self):
        try:                                        #Loading the events from the csv file, but if you are running the program without having file, error is handled!
            file_data = pandas.read_csv("events.csv")
            self.events =file_data.to_dict(orient="records")
        except FileNotFoundError:
            print("Enter Events first!")             #enter data and then if you run program, it will load the data from the file into events
        except Exception as er:
            print("An error occurred while loading events:", er)

    def display(self):                               #method to display program
        print("")
        print("******EVENT MANAGING PROGRAM******")

    def save_events(self):
        df = pandas.DataFrame(self.events)
        df.to_csv("events.csv", index=False)

    def display_calendar(self,year, month):           #method to display calendar
        print("")
        self.year = year
        self.month = month
        print("------DISPLAYING CALENDAR-------")
        print(calendar.month(self.year, self.month, w = 1, l =1 ))
        print("")

    def add_event(self):                              #method to add event
        try:                                          #exception handling
            self.month = int(input("Enter the month number, you wanna add event in:"))
            self.year = int(input("Enter the year:"))
            self.display_calendar(self.year, self.month)
        except Exception as er:
            print(er)
        event_name = input(("Enter the event name:-"))
        event_date = input(("Enter the D/M/Y of the event:-"))
        self.events.append({"Event name": event_name, "Event Date" : event_date})
        self.save_events()                            #adding events in the form of dictionary to the list of events

    def delete_event(self):                           #method to delete any event based on he index in the list 
        print("")
        self.display_events()
        try:                                          #exception handling
            event_del = int(input("Enter the Event number you want to delete(0,1,2,3...):"))
            self.events.pop(event_del)
            self.save_events()
        except Exception as er:
            print("Event is not there",er)

    def display_events(self):                         #method to display the events using pandas                     
        print("")
        if self.events:                               #checking if the events is not empty
            events_table = pandas.DataFrame(self.events)
            print(events_table)
        else:
            print("Empty Events list!")

ob = events_managing_program()
def main():
    while True:                                       #running program
        ob.display()                                  #user's choice
        ch = input('''
    Your choice:- "a"dd,
                "d"isplay,
                "D"elete,
                "q"uit        ''')
        if ch == "a":                                 #calling methods according to the User's choice
            ob.add_event()
        elif ch == "d":
            ob.display_events()
        elif ch == "D":
            ob.delete_event()
        elif ch == "q" or ch =="Q":
            print("Exiting from the program!! Thankyou")
            exit()                                    #exiting program
        else:
            print("Choice is invalid!!")

if __name__ == "__main__":
    main()