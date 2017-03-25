#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:01:51 2017

@author: zachary
"""
 # import required modules
import csv, random

# create teams and prep for data from kids
teams = {'Sharks': {}, 'Dragons': {}, 'Raptors': {}}

# empty lists for sorting purposes
list_of_kids = []
exp_kids = []
non_exp_kids = []

# pull kids' data and store for later use
def kid_dicts(kid, exp, guardians):
    list_of_kids.append({kid: [exp, guardians]})

# sort kids based on experience
def exp_sorter(kid):
    for info in kid.values():
        if info[0].upper() == 'YES':
            exp_kids.append(kid)
        else:
            non_exp_kids.append(kid)

# divide number of kids by number of teams
# assign kids to teams based on experience
def team_assigner(kid_list):
    num_of_kids = len(kid_list)
    for team, values in teams.items():
        kids = random.sample(kid_list, int(num_of_kids / len(teams))) 
        for kid in kids:
            values.update(kid)
            kid_list.remove(kid)
            
            
# write letters to guardians
def letter_writer(child, guardians, team):
    with open('{}.txt'.format(child), 'w') as letter:
        letter.write("""
                     Dear {}, \n
                     I want to welcome you and your child to the youth soccer league.
                     I'm glad your child gets to partake in this fun and exciting activity!'
                     I want to let you know that practice will start on May 15th at 5:00 PM.
                     {} is on the {} team, and I have no doubt they will do well!
                     Hope you all get the most out of this league! \n
                     Sincerely,
                     Zachary Williamson
                     """.format(guardians, child, team)
                     )
        
            
if __name__ == "__main__":
    
    # open and set up csvfile
    with open('/home/zachary/Downloads/soccer_players.csv') as csvfile:
        soccer_roster = csv.DictReader(csvfile)
        
        # pull data from roster to send to other functions
        for row in soccer_roster:
            kid_dicts(row['Name'], row['Soccer Experience'], row['Guardian Name(s)'])
            
        # sort and assign kids
        for kid in list_of_kids:
            exp_sorter(kid)
        team_assigner(exp_kids)
        team_assigner(non_exp_kids)
                
    # write the team roster textfile
    with open('teams.txt', 'w') as teamfile:
        for team, members in teams.items():
            teamfile.write('{} \n'.format(team))
            for member, stats in members.items():
                teamfile.write('{}, {}, {} \n'.format(member, stats[0], stats[1]))
                letter_writer(member, stats[1], team)
            teamfile.write('\n')



                    
        
        
            
