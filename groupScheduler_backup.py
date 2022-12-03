# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: <fill in the blank>
## EID : <fill in the blank>
## Section: <fill in the blank>

"""

import memberScheduler

class groupScheduler:

    def __init__(self, listPeople):
        # listPeople are the list of memberScheduler instances
        # complete instance initialization here
        
        DailySlots = 19
        EmptySlots = [0]*DailySlots
        
        print('------TEST-------')
        
        open_slots = {'Mon': [1]*19, 'Tue': [1]*19, 'Wed': [1]*19, 'Thu': [1]*19, 'Fri': [1]*19}
        print(open_slots)
        
        # need to add group for-loop
        
        # create a single list with the number of classes in each time slot (zero means everyone is available)
        for person in listPeople:
            print(person.name)
            for key, values in listPeople[0].week.items():
                print(f"{key}: {values}")
                #SumSlots = [0] * 19
                
                for i in range(len(values)):
                    if values[i] == 1:
                        open_slots[key][i] = 0
                    #print(values[i])
                    #SumSlots[i] += values[i]
            print(open_slots)
                
            
        pass
    

        
    def MeetingScheduler(self, **kwargs):
        # output needs to be returned as a dictionary containing days and keys and open times as values
        
        pass
 
# Function used to generate a .md file for Q3 and Q4
def report(file = False, file_name = 'Random.md', file_append = False, **kwargs):
    pass
    
if __name__ == '__main__':
    
    # Inputs for Q1, Q2 and Q4
    
    Input1 = [{'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}},
              {'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}]
    Input2 = {"C++ Learning Group" : [60, ["Albert Kaplan", "Sherri Strickland"]]}
    
    groups_dict = {
            "C++ Learning Group" : [60, ["Avery", "Jordan", "Parker"]], 
            "Team Meeting" : [90, ["Avery", "Riley", "Jordan", "Angel", "Parker", "Matt", "Lorne", "Anna" ]],
            "NASA Project Team" : [ 30, ["Angel", "Parker", "Anna" ]],
            "NSF Project Team" : [60, ["Riley", "Jordan", "Angel", "Lorne"]],
            "Thesis Writers" : [60, ["Riley", "Jordan", "Angel", "Matt"]]
            }

    
    # List of everyone in the Lab
    Members = []
    # Create a random schedule and display the schedule for everyone in the lab
    for count,person in enumerate(Input1):
        Members.append(memberScheduler.personSchedule(**person))
        Members[count].view_schedule()
    
    # Create a group of all members in the lab
    Group = groupScheduler(Members)
        
    # Find the open meeting slots for everyone in a particular group
    # open_slots = Group.MeetingScheduler(**Input2)
    open_slots = {'A':[1,2,3,4],'B':[5,4,3,2,1]}
    # Generate a report about the open meeting slots that are available
    report(**open_slots, file=False, file_name="Q3report/README.md", file_append=False)
    
    # Find open meeting slots for people in multiple groups
    # meeting_dict = Group.MeetingScheduler(**groups_dict)
    meeting_dict = {'A':[1,2,3,4],'B':[5,4,3,2,1]}
    
    # Generate a report about open meeting slots
    report(**meeting_dict, file=False, file_name="Q4report/README.md", file_append=False)