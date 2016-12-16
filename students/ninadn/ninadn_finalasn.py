'''Final assignment. This is a program that reads the gamescore.csv file, which has game information regarding a football match. 
The program has a number of pre-created statements. Based on the score, by quarter (and assuming 2 OT), the program will
print the box score, game summary, and auto-generate a short report about the game. The program can identify blowouts, close 
finishes, and low scoring games. The long term aim of this project is to create a comprehensive program to scrape the internet
for additional match information and create reports that offer historical perspective, etc.'''

import numpy as numpy
import pandas as pd
import matplotlib as plt

def printBoxScore(away_team, home_team, away_team_score, home_team_score):
	star = '*'
	print ('\n\n\n\n{:^100}'.format("BOX SCORE"))
	print (star*100)
	print (star," "*96,star)
	print ('{:<2} {:>30} {:>10} {:^10} {:<10} {:<30} {:>2}'.format(star,away_team, away_team_score," ",home_team_score, home_team,star))
	print (star," "*96,star)
	print (star*100,'\n')

def printDetailScore(away_team, home_team, P1ATS, P1HTS, P2ATS, P2HTS, P3ATS, P3HTS, P4ATS, P4HTS,P5ATS, P5HTS, P6ATS, P6HTS, away_team_score, home_team_score):
	dash = "-"
	sep = "|"
	us = "_"
	print ('\n{:^99}'.format("GAME SUMMARY"))
	print (" ", us*95, " ")
	print (sep," "*95,sep)
	print ('{:<2} {:<30} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:>2}'.format(sep, "Team", "Q1", "Q2", "Q3", "Q4", "OT/1", "OT/2", "FINAL", sep))
	print (sep,dash*95,sep)
	print ('{:<2} {:<30} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:>2}'.format(sep, away_team, P1ATS, P2ATS, P3ATS, P4ATS, P5ATS, P6ATS, P6ATS, sep))
	print (sep,dash*95,sep)
	print ('{:<2} {:<30} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:>2}'.format(sep, home_team, P1HTS, P2HTS, P3HTS, P4HTS, P5HTS, P6HTS, P6HTS, sep))
	print (sep,us*95,sep)

def returnWinner(away_team_score, home_team_score):
	'''If away team wins, return 1. If home wins, return 0. If tie, return 2.'''
	if away_team_score > home_team_score:
		winner = int(1)
	elif home_team_score > away_team_score:
		winner = int(0)
	else: winner = int(2)
	return winner

def returnGameType(away_team, home_team, P1ATS, P1HTS, P2ATS, P2HTS, P3ATS, P3HTS, P4ATS, P4HTS,P5ATS, P5HTS, P6ATS, P6HTS, away_team_score, home_team_score):
	''' This function will take in all the quarter-by-quarter scores and return one of 7 game types, including whether the game was a 
	blowout, a shutout, had a lead change, etc. Using these gametypes, we will construct a story.

	Gametypes:
	1	One team maintains lead throughout
	2	Lead changes
	3	Blowout
	4	Close finish
	5	Shut out
	6	Low scoring
	7	Generic
	'''
	gametype = []
	blowoutMargin = int(21) #Defining a blowout as a points differential of at least 21 points
	closeFinishMargin = int(7) #Defining a close fiinish as a points differential of at most 7 points
	LowScoringThreshold = int(14) #Defining a low scoring game as one where the winning team scored 14 points or less


	P1DIFF = int(P1ATS) - int(P1HTS)
	P2DIFF = int(P2ATS) - int(P2HTS)
	P3DIFF = int(P3ATS) - int(P3HTS)
	P4DIFF = int(P4ATS) - int(P4HTS)
	P5DIFF = int(P5ATS) - int(P5HTS)
	P6DIFF = int(P6ATS) - int(P6HTS)

	if numpy.sign(P1DIFF) and numpy.sign(P2DIFF) and numpy.sign(P3DIFF) and numpy.sign(P4DIFF) and numpy.sign(P5DIFF) and numpy.sign(P6DIFF) == 1:
		gametype.append(1)
	elif numpy.sign(P1DIFF) and numpy.sign(P2DIFF) and numpy.sign(P3DIFF) and numpy.sign(P4DIFF) and numpy.sign(P5DIFF) and numpy.sign(P6DIFF) == -1:
		gametype.append(1)
	else: gametype.append(2)
	
	if abs(int(away_team_score) - int(home_team_score)) > blowoutMargin:
		gametype.append(3)
	elif abs(int(away_team_score) - int(home_team_score)) < closeFinishMargin:
		gametype.append(4)

	if int(home_team_score) == 0 or int(away_team_score) == 0:
		gametype.append(5)

	if int(home_team_score) < LowScoringThreshold and int(away_team_score) < LowScoringThreshold:
		gametype.append(6)

	if len(gametype) == 0:
		gametype.append(7)

	return gametype

def printStory (gametype, winner, home_team_score, away_team_score, home_team, away_team, Home_Alias, Away_Alias, Location_Stadium, Location_City, Location_Province):
	if winner == 1:
		gameWinner = away_team
		gameWinnerAlias = Away_Alias
		victoryMargin = int(away_team_score) - int(home_team_score)
	elif winner == 0:
		gameWinner = home_team
		gameWinnerAlias = Home_Alias
		victoryMargin = int(home_team_score) - int(away_team_score)
	else:
		gameWinner = 2
		victoryMargin = int(0)
	
	wiretag = "AUTOMATED WIRE"
	gametype_0_text = ''
	gametype_1_text = ''
	gametype_2_text = ''
	gametype_3_text = ''
	gametype_4_text = ''
	gametype_5_text = ''
	gametype_6_text = ''
	gametype_7_text = ''

	if gameWinner != 2:
		if winner == 1:
			gametype_0_text = '[{}, {}, {}] The {} today beat the {} {} - {} at {}.'.format(wiretag, Location_City, Location_Province, away_team, home_team, away_team_score, home_team_score, Location_Stadium)
		elif winner == 0:
			gametype_0_text = '[{}, {}, {}] The {} today beat the {} {} - {} at {}.'.format(wiretag, Location_City, Location_Province, home_team, away_team, home_team_score, away_team_score, Location_Stadium)
	else:
		gametype_0_text = '[{}, {}, {}] The {} and the {} played for a stunning {} - {} tie here at the {} in {}.'.format(wiretag, Location_City, Location_Province, home_team, away_team, home_team_score,away_team_score, Location_Stadium,Location_City)

	for i in gametype:
		if i == 1 and P2ATS > P2HTS:
			gametype_1_text = ' The {}s led throughout and headed into half time with a {} - {} lead.'.format(gameWinnerAlias, away_team_score, home_team_score)
		elif i == 1 and P2HTS > P2ATS:
			gametype_1_text = ' The {}s led throughout and headed into half time with a {} - {} lead.'.format(gameWinnerAlias, home_team_score, away_team_score)
		elif i == 3:
			gametype_3_text = ' It was a blowout win for the {}s and the {} point margin of victory will be a shot in the arm for the team. '.format(gameWinnerAlias, victoryMargin)
		elif i == 4:
			gametype_4_text = ' It was a narrow {}-point win for the {}.'.format(victoryMargin, gameWinnerAlias)
		elif i == 5:
			gametype_5_text = ' It was a brilliant shutout victory for the {}s and the team is looking forward to repeating this splendid performance.'.format(gameWinnerAlias)
		elif i == 6:
			gametype_6_text = ' It was a low scoring affair, with neither team particularly brilliant on offense.'





	'''This where I will concatenate all the various texts into a paragraph.'''
	gametext = gametype_0_text + gametype_1_text + gametype_2_text + gametype_3_text + gametype_4_text + gametype_5_text + gametype_6_text + gametype_7_text
	print('\n\n', gametext)

def print_story_control(questionlist, answerlist):
	home_team = answerlist[5]+" "+answerlist[6]
	away_team = answerlist[8]+" "+answerlist[9]
	away_team_score = answerlist[22]
	home_team_score = answerlist[21]
	Location_Stadium = answerlist[1]
	Location_City = answerlist[2]
	Location_Province = answerlist[3]
	Location_Country = answerlist[4]
	Home_Team_Name = answerlist[5]
	Home_Alias = answerlist[6]
	Home_Team_Coach = answerlist[7]
	Away_Team_Name = answerlist[8]
	Away_Alias = answerlist[9]
	Away_Team_Coach = answerlist[10]
	P1HTS = answerlist[11]
	P1ATS = answerlist[12]
	P2HTS = answerlist[13]
	P2ATS = answerlist[14]
	P3HTS = answerlist[15]
	P3ATS = answerlist[16]
	P4HTS = answerlist[17]
	P4ATS = answerlist[18]
	P5HTS = answerlist[19]
	P5ATS = answerlist[20]
	P6HTS = answerlist[21]
	P6ATS = answerlist[22]

	'''I will simplify the above later on by using dicts where the key is the team and the values 
	is a list of scores ordered by period.'''

	winner = returnWinner(away_team_score, home_team_score)
	gametype = returnGameType (away_team, home_team, P1ATS, P1HTS, P2ATS, P2HTS, P3ATS, P3HTS, P4ATS, P4HTS,P5ATS, P5HTS, P6ATS, P6HTS, away_team_score, home_team_score)

	printBoxScore(away_team, home_team, away_team_score, home_team_score)
	printDetailScore(away_team, home_team, P1ATS, P1HTS, P2ATS, P2HTS, P3ATS, P3HTS, P4ATS, P4HTS,P5ATS, P5HTS, P6ATS, P6HTS, away_team_score, home_team_score)
	printStory(gametype, winner, home_team_score, away_team_score, home_team, away_team, Home_Alias, Away_Alias, Location_Stadium, Location_City, Location_Province)
	#printboxscore(away_team, home_team, away_team_score, home_team_score)

def printindexlist (questionlist, answerlist):
	for i, j, k in zip(questionlist, answerlist, range(0,len(questionlist)-1)):
		print ('{:<4} {:30} {:15}'.format(k, i, j))

def organize_data(infolist):

	questionlist = []
	answerlist = []
	masterlist = []

	for line in infolist:
		questionlist.append(line.split()[0])
		alist = line.split()
		answer = ''
		for a in alist [1:]:
			answer = answer + a + " "
		answerlist.append(answer.rstrip())
	masterlist.append(questionlist)
	masterlist.append(answerlist)
	return masterlist

if __name__ == '__main__':
	'''In this function, I am reading the csv file using the with open method, then
	going through the file line by line and putting each line in a list called infolist. 
	As I do this, I am stripping out the \n at the end of each line, which was introducing 
	an extra space after each line. Infolist is therefore a list where each element is a line
	from the csv file. From this info list, I am splitting the first line and checking the 
	element, which should tell me what the sport is. If the sport is football, I will proceed
	or else I will exit as other sports are not supported. I then invoke the organize_data 
	function which will split the infolist list into two separate lists, one with the key (which 
	I call questionlist) and the other with the values (which I call answerlist). '''
	with open ('gamescore.csv', mode = 'r', encoding = 'utf-8') as a_file:
		#print(a_file.read())
		infolist = []
		for line in a_file:
			line = line.replace('\n',"")
			infolist.append(line)
		#print (infolist)
		sport = infolist[0].split()[1]
		#print (sport)
		masterlist = []
		if sport == 'football' or sport == 'Football' or sport == 'FOOTBALL':
			masterlist = organize_data(infolist)
			#print (masterlist)
			questionlist_master = masterlist[0]
			answerlist_master = masterlist[1]
		else:
			print ("Sport not supported\n")
		
		'''The below are two important functions. One starts printing the score and the story 
		and the other (printindexlist) prints the questions and answers with an index column so 
		that I can refer to it and update indices easily later on.'''

		print_story_control(questionlist_master, answerlist_master)
		#printindexlist(questionlist_master,answerlist_master)
