# Build a calendar

""" In this project, a basic calendar will be built that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar (V)
Add an event to the calendar (A)
Update an existing event (U)
Delete an existing event (D)"""

from time import sleep, strftime

user_name = "Fanying Tang"

calendar = {}

def welcome():
  print "Welcome " + user_name + "!"
  print "The calendar is opening!"
  sleep(1)
  print strftime("%A %b %d, %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  
print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "The calendar is empty!"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date?")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "The calendar is updated"
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:10]) < int(strftime("%Y")):
        print "The input date is invalid"
        try_again = raw_input("Try again? Y for Yes, N for No: ")
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "The event was successfully added"
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "The event is deleted!"
            print calendar
          else:
              print "Incorrect event was specified."
    elif user_choice == "X":
      start = False
    else:
      print "Invalid coomand was entered"
      
start_calendar()
        
