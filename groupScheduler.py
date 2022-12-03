# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: <fill in the blank>
## EID : <fill in the blank>
## Section: <fill in the blank>

"""

import memberScheduler
import markdown 
import os

class groupScheduler:

    def __init__(self, listPeople):
        # listPeople are the list of memberScheduler instances
        # complete instance initialization here
        
        self.listPeople = listPeople
        self.listPeopleNames =  []
        for person in listPeople:
            self.listPeopleNames.append(person.name)
    
    def MeetingScheduler(self, **kwargs):
        # output needs to be returned as a dictionary containing days and keys and open times as values
        
        # initiate open schedule for a person
        slots_in_day = 16
        open_slots_i = {'Mon': [1]*slots_in_day, 'Tue': [1]*slots_in_day, 'Wed': [1]*slots_in_day,
                      'Thu': [1]*slots_in_day, 'Fri': [1]*slots_in_day, 'Duration': 60}
        
        # initiate dictionary for all group meetings
        # key = group name, value = schedule of open slots
        open_slots = {}
        
        
        # assign kwarg inputs
        for key,value in kwargs.items():
            group = key
            duration = value[0]
            names = value[1]
            if group not in open_slots:
                open_slots[key] = {'Mon': [0]*slots_in_day, 'Tue': [0]*slots_in_day, 'Wed': [0]*slots_in_day,
                              'Thu': [0]*slots_in_day, 'Fri': [0]*slots_in_day, 'Duration': 60}
            
            # create new list as subset of listPeople (only the selected names)
            # if names aren't in listPeople, throw error
            MeetingNames = []
            listPeopleMeet = []
            for i in range(len(names)):
                if names[i] in self.listPeopleNames:
                    MeetingNames.append(names[i])
                else:
                    raise NameError(names[i] + " is not a part of the lab group")
                    
            for i in range(len(self.listPeople)):
                if self.listPeople[i].name in MeetingNames:
                    listPeopleMeet.append(self.listPeople[i])
                        
            for i in range(len(listPeopleMeet)):
                for day,slots in listPeopleMeet[i].week.items():
                    for j in range(len(slots)):
                        if duration == 30:
                            open_slots_i['Duration'] = 30
                            if listPeopleMeet[i].week[day][j] == 1:
                                open_slots_i[day][j] = 0
                        elif duration == 60:
                            open_slots_i['Duration'] = 60
                            if listPeopleMeet[i].week[day][j] == 1:
                                open_slots_i[day][j] = 0
                                open_slots_i[day][j-1] = 0
                            if j == len(slots)-1:
                                open_slots_i[day][j] = 0
                        elif duration == 90:
                            open_slots_i['Duration'] = 90
                            if listPeopleMeet[i].week[day][j] == 1:
                                open_slots_i[day][j] = 0
                                open_slots_i[day][j-1] = 0
                                open_slots_i[day][j-2] = 0
                            if j == len(slots)-1 or j == len(slots)-2:
                                open_slots_i[day][j] = 0
                    open_slots[group][day] = open_slots_i[day].copy()
            
        # Generate Report for Q3 and Q4
        if len(kwargs)==1:
            filename="Q3report/README.md"
        else:
            filename="Q4report/README.md"
                
        report(open_slots, file=False, file_name=filename, file_append=False)
            
        return open_slots
    
        pass
 
# Function used to generate a .md file for Q3 and Q4
def report(open_slots, file = False, file_name = 'Random.md', file_append = False, **kwargs):
    
    daytime = ['9:00','9:30','10:00', '10:30', '11:00', '11:30', 
               '12:00','12:30', '13:00', '13:30', '14:00', '14:30', '15:00', 
               '15:30', '16:00','16:30', '17:00']
    
    dirname = file_name.split("/")[0]
    if not os.path.exists(dirname):
        os.makedirs(dirname)

            
    with open(file_name, 'bw+') as f:
        for group, schd in open_slots.items(): 
            f.write('<ins>**{}**</ins> <br />'.format(group).encode('utf-8'))
            
            
            # Parses open_slots for duration and deletes the item after
            for day, time in schd.items():
                if day == 'Duration':
                    dur = time

            if 'Duration' in schd:
                del schd['Duration']      

            
            if dur == 30:
                dt = 1
            elif dur == 60:
                dt = 2
            elif dur == 90:
                dt = 3
            
            for day, time in schd.items():
                f.write('**{}** <br />'.format(day).encode('utf-8'))
                for i in range(0, dt):
                    time.append(0)
                optionCounter = 1
                
                for i in range(0, len(time)-1):
                    if time[i] == 1:
                        if time[i+dt-1] == 1:
                            st = daytime[i]
                            et = daytime[i+dt]
                            f.write('&emsp; *Option {}*: Starts from *{}* to *{}* <br />'.format(optionCounter, st, et).encode('utf-8'))
                            optionCounter += 1
                if optionCounter == 1:
                    f.write('&emsp; No feasible time slots <br />'.encode('utf-8')) 
            
            f.write('<br /> <br />'.encode('utf-8'))

    
if __name__ == '__main__':
    
    # Inputs for Q1, Q2 and Q4
    
    # Input1 = [{'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}},
    #           {'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}]
       
    # Input2 = {"C++ Learning Group" : [60, ["Albert Kaplan", "Sherri Strickland"]]}
    
    # Input3 = {"C++ Learning Group" : [60, ["Albert Kaplan", "Sherri Strickland"]],"NASA Project Team" : [60, ["Albert Kaplan", "Sherri Strickland"]] }

    
    # groups_dict = {
    #         "C++ Learning Group" : [60, ["Avery", "Jordan", "Parker"]], 
    #         "Team Meeting" : [90, ["Avery", "Riley", "Jordan", "Angel", "Parker", "Matt", "Lorne", "Anna" ]],
    #         "NASA Project Team" : [ 30, ["Angel", "Parker", "Anna" ]],
    #         "NSF Project Team" : [60, ["Riley", "Jordan", "Angel", "Lorne"]],
    #         "Thesis Writers" : [60, ["Riley", "Jordan", "Angel", "Matt"]]
    #         }

    
    # # List of everyone in the Lab
    # Members = []
    # # Create a random schedule and display the schedule for everyone in the lab
    # for count,person in enumerate(Input1):
    #     Members.append(memberScheduler.personSchedule(**person))
    #     Members[count].view_schedule()
    
    # # Create a group of all members in the lab
    # Group = groupScheduler(Members)
        
    # # Find the open meeting slots for everyone in a particular group
    # open_slots = Group.MeetingScheduler(**Input2)
    # # open_slots = {'A':[1,2,3,4],'B':[5,4,3,2,1]}
    # # Generate a report about the open meeting slots that are available
    # report(open_slots, file=False, file_name="Q3report/README.md", file_append=False)
    
    # # Find open meeting slots for people in multiple groups
    # meeting_dict = Group.MeetingScheduler(**Input3)
    # # meeting_dict = {'A':[1,2,3,4],'B':[5,4,3,2,1]}
    
    # # Generate a report about open meeting slots
    # report(meeting_dict, file=False, file_name="Q4report/README.md", file_append=False)

    # Test for Q1
    p_list = []
    test1_member = {'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}}
    test2_member = {'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}} 
    test3_member = {'name': 'Jan Serrano', 'classes': {'Mon': 3, 'Tue': 3, 'Wed': 1, 'Thu': 4, 'Fri': 3}}
    p1 = memberScheduler.personSchedule(**test1_member)
    p2 = memberScheduler.personSchedule(**test2_member)
    p3 = memberScheduler.personSchedule(**test3_member)
    p_list.append(p1)
    p_list.append(p2)
    p_list.append(p3)

    
    # start test for Q2/3/4 here
    # Test for Q2
    g1 = groupScheduler(p_list)
    meeting_input =  {"C++ Learning Group" : [60, ["Albert Kaplan", 'Jan Serrano']]}
    g1.MeetingScheduler(**meeting_input)

        
    # Test for Q4
    g2 = groupScheduler(p_list)
    meeting_input2 =  {"C++ Learning Group" : [60, ["Albert Kaplan", "Sherri Strickland"]],"NASA Project Team" : [60, ["Albert Kaplan", 'Jan Serrano', "Sherri Strickland"]]}
    g2.MeetingScheduler(**meeting_input2)
