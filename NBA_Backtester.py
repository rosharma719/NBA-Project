import csv
import sys
from termcolor import colored, cprint 
import pandas as pd

def guess(team1, team2): #guesser function
    team1odds = 0
    team2odds = 0
    with open("directory", 'r') as csvfile: #replace with file in specified format
        csvreader = csv.reader(csvfile)
        
        #assigns var to each team
        for row in csvreader:
            if row[1] == team1: 
                team1odds += float(row[28])
                team1odds -= float(row[21])
            if row[1] == team2:
                team2odds += float(row[28])
                team2odds -= float(row[21])
        team1odds = team1odds/15
        team2odds = team2odds/15
        
        if team1odds > team2odds:
            expected = team1
            return(team1)
        elif team2odds > team1odds:
            expected = team2
            return(team2)
        else:
            expected = "idk"
            return("idk")

def returnteamodds(team): #guesser function
    teamodds = 0
    
    with open("C:\\Users\\kragg\\Downloads\\NBA stats wins2 - Sheet5.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        #assigns var to each team
        for row in csvreader:
            if row[1] == team: 
                teamodds += float(row[28])
                teamodds -= float(row[21])
        teamodds = teamodds/15            
    return teamodds

#main backtester
with open("C:\\Users\\kragg\\Downloads\\NBA Algo - Games (3).csv", 'r') as csvfile:
    reader = csv.reader(csvfile)

    wins = 0
    losses = 0
    rowcount = 0

    df_merged = pd.DataFrame(columns=['Team 1', 'Team 1 Odds', 'Team 2', 'Team 2 Odds', 'Expected Winner', 'Winner'])

    for row in reader:
        rowcount+=1
        team1 = row[0]
        team2 = row[2]
        winner = row[4]
        expect = guess(team1, team2)
        team1odds = returnteamodds(team1)
        team2odds = returnteamodds(team2)

        df2 = pd.DataFrame([[team1, team1odds, team2, team2odds, expect , winner]], columns=['Team 1', 'Team 1 Odds', 'Team 2', 'Team 2 Odds', 'Expected Winner', 'Winner'])
        df_merged = pd.concat([df_merged, df2], ignore_index=True, sort=False)


        if expect == winner:
            wins +=1
        else:
            losses +=1
            
    print(" ")
    text = colored(str(wins) + " wins", 'green')           
    print(text)
    text = colored(str(losses) + " losses", 'red')
    print(text)
    print(" ")
    if wins/(wins+losses) > 0.5:
        text = colored(str(wins/(wins+losses)) + " winrate", 'green')
    else: 
        text = colored(str(wins/(wins+losses)) + " winrate", 'red')
    print(text)        
    print("")

    #print(df_merged) #print list instead of sending to csv 

    df_merged.to_csv('out.csv')
