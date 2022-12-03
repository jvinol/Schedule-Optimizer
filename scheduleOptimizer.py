# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: <fill in the blank>
## EID : <fill in the blank>
## Section: <fill in the blank>

"""

from groupScheduler import groupScheduler
import memberScheduler
import os
import copy

class scheduleOptimizer:
    

    def __init__(self, g1, m_schedule):

        pass
        
    def MeetingScheduler(self, **kwargs):
        
        pass
        
        
def report(open_slots, lp, dt_d, nameList, m_schedule_initial, file = False, file_name = 'Random.md', file_append = False, **kwargs):
    pass
  
    
if __name__ == '__main__':
    
    #self_testing region
    
    meeting_input = {"ME396 Project discussion with G1" : [60, ["Albert Kaplan", "Sherri Strickland", "Linda Ruiz", "Jen Madden", "Katherine Medina", "Deb Shah", "Hope Glover", "Ruben Forbes", "Alice Parsons", "Ira McGuire", "Viola Caldwell", "Annie Gilbert", "Laurie Carroll", "Kristin Holder", "Lindsay Munoz", "Terrance Bates"]],
                      "ME396 Project discussion with G2" : [60, ["Inez Barrett", "Katie Gaines", "Herbert Woodard", "Rochelle Boone", "Sabrina Hart", "Yvonne Glass", "Al Clements", "Shelia Porter", "Wendell Kelly"]],
                      "ME396 Project discussion with G3" : [60, ["Jan Serrano", "Sherri Strickland", "Debbie Trujillo", "Lydia May", "Wendell Kelly", "Herbert Woodard", "Katie Gaines"]],}
    
    # meeting_input = {"ME396 Project discussion with G1" : [60, ["Albert Kaplan"]],
    #                   "ME396 Project discussion with G2" : [60, ["Inez Barrett", "Katie Gaines"]],
    #                   "ME396 Project discussion with G3" : [60, ["Inez Barrett"]],}
    
    # meeting_input = {"ME396 Project discussion with G1" : [60, ["Albert Kaplan", "Katie Gaines", "Inez Barrett"]],}
    
    memlist = [{'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}},
    {'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}, 
    {'name': 'Linda Ruiz', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}, 
    {'name': 'Jen Madden', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}, 
    {'name': 'Katherine Medina', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}, 
    {'name': 'Herbert Woodard', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}, 
    {'name': 'Kelli Underwood', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}, 
    {'name': 'Katie Gaines', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Rochelle Boone', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Sabrina Hart', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Debbie Trujillo', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Lydia May', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Wendell Kelly', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Jan Serrano', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Inez Barrett', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Deb Shah', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Hope Glover', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Ruben Forbes', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Alice Parsons', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Ira McGuire', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Viola Caldwell', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Annie Gilbert', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Laurie Carroll', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Kristin Holder', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Lindsay Munoz', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Terrance Bates', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Yvonne Glass', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Al Clements', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Shelia Porter', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},
    {'name': 'Mae Tate', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}},]
    
       
    # List of everyone in the Lab
    p_list = []
    # Create a random schedule and display the schedule for everyone in the lab
    for count,person in enumerate(memlist):
        p_list.append(memberScheduler.personSchedule(**person))
        # p_list[count].view_schedule()
    
    # Create a group of all members in the lab
    G1 = groupScheduler(p_list)
    s = G1.MeetingScheduler(**meeting_input)
    # print(s)
    
    # Dr. Pryor's Schedule 
    main_schedule = {'Mon': [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                      'Tue': [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                      'Wed': [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                      'Thu': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                      'Fri': [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    
    
    o1 = scheduleOptimizer(G1, main_schedule)
    o1.MeetingScheduler(**meeting_input)










