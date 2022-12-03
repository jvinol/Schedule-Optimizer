# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: <fill in the blank>
## EID : <fill in the blank>
## Section: <fill in the blank>

"""
import random
import numpy as np

class personSchedule:   
    # Earliest class start time
    EarliestStartTime = 8
    # Latest class start time on M,W,F
    LatestStartTime_MWF = 16
    # Latest class start time on T,TH
    LatestStartTime_TTH = 17
    # Class length on M,W,F =  1 hr
    ClassLength_MWF = 1
    # Class length T,Th = 1.5 hr
    ClassLength_TTH = 1.5
    # List of class start times for M,W,F in intervals of 30 mins
    StartTimes_MWF = [0] *  ((LatestStartTime_MWF - EarliestStartTime)*2 + 1)
    # List of class start times for M,W,F in intervals of 30 mins
    StartTimes_TTH = [0] *  ((LatestStartTime_TTH - EarliestStartTime)*2 + 1)
    
    # UT classes typically start at one the following times: 8:00, 9:30, 10:00, 11:00, 12:00, 12:30, 13:00, 14:00, 15:00, 15:30, 16:00, 17:00
    # Block start times that are not one of the above times
    StartTimes_MWF[1] = StartTimes_MWF[2] = StartTimes_MWF[5] = StartTimes_MWF[7] = StartTimes_MWF[11] = StartTimes_MWF[13] = 9
    StartTimes_TTH[1] = StartTimes_TTH[2] = StartTimes_TTH[5] = StartTimes_TTH[7] = StartTimes_TTH[11] = StartTimes_TTH[13] = StartTimes_TTH[17] = 9
    def __init__(self, **kwargs):
        # Number of classes on a specific day of the week
        self.NumberOfClasses = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0}
        self.NumberOfClasses.update(kwargs['classes'])
        # Student Name
        self.name = kwargs['name']
        # Total Available hours between 9 to 5
        self.TotalAvailableHours = 0 
        
        # Creating a random weekly schedule for the student between 8 AM and 6:30 PM and then saving the schedule between 9:00 AM and 5:00 PM
        # Intializing every day with 0s occupying every class start time position
        self.week = {'Mon': personSchedule.StartTimes_MWF.copy(), 'Tue': personSchedule.StartTimes_TTH.copy(),
                     'Wed': personSchedule.StartTimes_MWF.copy(), 'Thu': personSchedule.StartTimes_TTH.copy(), 'Fri': personSchedule.StartTimes_MWF.copy()}
        # Iterating through the days and number of classes on each day
        for day,number in self.NumberOfClasses.items():
            for i in range(number):
                # Finding open time slots where there are no classes
                NoClasses = [i for i,x in enumerate(self.week[day]) if x == 0]
                Index = random.choice(NoClasses)
                
                # Adding random classes                
                if day == 'Mon' or day == 'Wed' or day == 'Fri':
                    # Make the index position = 1
                    self.week[day][Index] = 1
                    # if this is 4:00 PM append an additional 1 to the end
                    if Index == len(self.week[day])-1:
                        self.week[day].append(1)
                    # else just make the next 30 min time slot = 1
                    else:
                        self.week[day][Index+1] = 1
                        
                    # Adding a placeholder to prevent an additional class from starting 30 mins before the current class    
                    if Index != 0 and self.week[day][Index-1] != 1:
                        self.week[day][Index-1] = 9
                        
                else:
                    # Make the index position = 1
                    self.week[day][Index] = 1
                    # If start time is 5:00 PM append 2 additional time slots at the end
                    if Index == len(self.week[day])-1:
                        self.week[day].append(1)
                        self.week[day].append(1)
                    # If start time is 4:30 PM append 1 additional time slots at the end
                    elif Index == len(self.week[day])-2:
                        self.week[day][Index+1] = 1
                        self.week[day].append(1)
                    # else just make the next two 30 min time slot = 1
                    else:
                        self.week[day][Index+1] = 1
                        self.week[day][Index+2] = 1
                        
                    # Adding a placeholder to prevent an additional class from starting 60 mins before the current class    
                    if Index != 0 and Index != 1 and self.week[day][Index-1] != 1:
                        self.week[day][Index-1] = 9
                        self.week[day][Index-2] = 9
                    elif Index != 0 and Index == 1:
                        self.week[day][Index-1] = 9
                         
            # Add padding at the end to ensure all the lists are the same length
            while len(self.week[day]) < 21:
                self.week[day].append(0)
                
            # Change the timeslots displayed to only show the schedule between 9:00 AM and 5:00 PM
            self.week[day] = self.week[day][2:18]
                
            # Get rid of the placeholders
            for count,value in enumerate(self.week[day]):
                if value == 9:
                    self.week[day][count] = 0
                    
            for number in self.week[day]:
                if number == 0:
                    self.TotalAvailableHours += 1
                
            
        
    def add_event(self,Time):
        Day = Time['day']
        
        # Convert Start and End time to float and put it in the right format
        StartTime = Time['time']['from'].split(':')
        EndTime = Time['time']['to'].split(':')
        if StartTime[1] == '30':
            StartTime[1] = '5'
        if EndTime[1] == '30':
            EndTime[1] = '5'
            
        EndTime = float('.'.join(EndTime))
        StartTime = float('.'.join(StartTime))
    
        StartTime_Index = (StartTime - 9)*2
        EndTime_Index = (EndTime - 9)*2
        Event_Index = np.arange(int(StartTime_Index),int(EndTime_Index))
        
        # Check to see if there is already an event in the time slot specified
        Flag = True
        for position in Event_Index:
            # If there is an event then print error message and set flag to false
            if self.week[Day][position] == 1:
                print('Failed to add this event because of the pre-existed events')
                Flag = False
                break
        
        # if there is no event then change the value in the schedule to 1
        if Flag:
            print('Successfully added this event into schedule')
            self.TotalAvailableHours -= (EndTime - StartTime)*2
            for position in Event_Index:
                self.week[Day][position] = 1
            
            print(self.name)
            # print the class schedule for the student
            for key, values in self.week.items():
                print(f"\t {key}: {values}")
            print(f"Total Available Hours: {self.TotalAvailableHours/2}")
                
            
    
    def del_event(self,Time):
        Day = Time['day']
        
        # Convert Start and End time to float and put it in the right format
        StartTime = Time['time']['from'].split(':')
        EndTime = Time['time']['to'].split(':')
        if StartTime[1] == '30':
            StartTime[1] = '5'
        if EndTime[1] == '30':
            EndTime[1] = '5'
            
        EndTime = float('.'.join(EndTime))
        StartTime = float('.'.join(StartTime))
        
        StartTime_Index = (StartTime - 9)*2
        EndTime_Index = (EndTime - 9)*2
        Event_Index = np.arange(int(StartTime_Index),int(EndTime_Index))
        
        # Check to see if there is an event in the time slot specified
        Flag = True
        for position in Event_Index:
            # If the time slot is empty print error message and set flag to false
            if self.week[Day][position] == 0:
                print('Failed to delete this event because of the empty slots')
                Flag = False
                break
        
        # if there is a event in the specified time slot then set the value in the schedule to 0
        if Flag:
            print('Successfully deleted this event from schedule')
            self.TotalAvailableHours += (EndTime - StartTime)*2
            for position in Event_Index:
                self.week[Day][position] = 0
                
            print(self.name)
            # print the class schedule for the student
            for key, values in self.week.items():
                print(f"\t {key}: {values}")
            print(f"Total Available Hours: {self.TotalAvailableHours/2}")
        
    def view_schedule(self):
        # print the student name
        print(self.name)
        # print the class schedule for the student
        for key, values in self.week.items():
            print(f"\t {key}: {values}")
        print(f"Total Available Hours: {self.TotalAvailableHours/2}")
        
    def return_schedule(self):
        
        return self.name, self.week 


if __name__ == '__main__':
    
    Input1 = [{'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}},
{'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}]
    # List of everyone in the Lab
    Members = []
    for count,person in enumerate(Input1):
        Members.append(personSchedule(**person))
        Members[count].view_schedule()
        
    time_dict_input = {'day': 'Wed', 'time': {'from': '09:30', 'to': '10:30'}}
    Members[0].add_event(time_dict_input)
        