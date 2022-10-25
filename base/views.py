from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AllPlayer, Team
import os
import random

team_list = [
    "team_1.txt",
    "team_2.txt",
    "team_3.txt",
    "team_4.txt",
    "team_5.txt",
    "team_6.txt",
    "team_7.txt",
    "team_8.txt"
]

def split_males(team_count, players_count):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    maleList = []

    #read original txt
    with open(f"{ROOT_DIR}/files/players.txt", 'r') as f:
        males = f.readlines()

    #append data in txt to maleList
    if len(males) != 0:
        for i in males:
            maleList.append(i.replace("\n", ""))

        for team_no in range(team_count):

            #no of males in a team
            for val in range(players_count):

                #pick one randomly
                random_male = random.sample(maleList, 1)
                # print(random_male[0] + "removed")
                maleList.pop(maleList.index(random_male[0]))

                #remove the picked one from original txt
                with open(f"{ROOT_DIR}/files/players.txt", 'r') as f, open(f"{ROOT_DIR}/files/players.txt" , 'w') as r:
                    for i in maleList:
                        r.write(i + "\n")
                    

                #add picked one to selected_players txt
                with open(f"{ROOT_DIR}/files/selected_players.txt" , 'a') as s:
                    s.write(random_male[0] + "\n")
                
                # num_lines = sum(1 for line in open(f"teams/{team_list[val]}"))
                # if num_lines != 7:
                
                with open(f"{ROOT_DIR}/files/teams/{team_list[team_no]}" , 'a') as s:
                    s.write(random_male[0] + "\n")

                print(f"{random_male[0]} added to {team_list[team_no]}")


    else:
        print("All required male players have been selected")

def split_females(team_count, players_count):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    maleList = []

    #read original txt
    with open(f"{ROOT_DIR}/files/female_players.txt", 'r') as f:
        males = f.readlines()

    #append data in txt to maleList
    if len(males) != 0:
        for i in males:
            maleList.append(i.replace("\n", ""))

        for team_no in range(team_count):

            #no of males in a team
            for val in range(players_count):

                #pick one randomly
                random_male = random.sample(maleList, 1)
                # print(random_male[0] + "removed")
                maleList.pop(maleList.index(random_male[0]))

                #remove the picked one from original txt
                with open(f"{ROOT_DIR}/files/female_players.txt", 'r') as f, open(f"{ROOT_DIR}/files/female_players.txt" , 'w') as r:
                    for i in maleList:
                        r.write(i + "\n")
                    

                #add picked one to selected_players txt
                with open(f"{ROOT_DIR}/files/selected_players.txt" , 'a') as s:
                    s.write(random_male[0] + "\n")
                
                # num_lines = sum(1 for line in open(f"teams/{team_list[val]}"))
                # if num_lines != 7:
                
                with open(f"{ROOT_DIR}/files/teams/{team_list[team_no]}" , 'a') as s:
                    s.write(random_male[0] + "\n")

                print(f"{random_male[0]} added to {team_list[team_no]}")


    else:
        print("All required male players have been selected")


def home(request):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    all_players_txt_path = f"{ROOT_DIR}/files/"
    all_teams_txt_path = f"{ROOT_DIR}/files/teams/"
    team_list = os.listdir(all_teams_txt_path)

    num_of_teams = list(range(1, 9))
    male_players = 56
    female_players = 24
    error = ""
    error2 = ""

    #get data from teams txts
    team_list_2 = []
    for i in team_list:
        with open(f"{all_teams_txt_path}/{i}", 'r') as r:
            all_team_list = r.readlines()
            team_list_2.append(all_team_list)

    #get data from all players txt
    with open(f"{all_players_txt_path}/players.txt", 'r') as p:
        players = p.readlines()
    
    if request.method == 'POST':
        if 'Shuffle_Males' in request.POST:
            listStr = request.POST['name']
            listOfStr = listStr.split("\n")
            if len(listOfStr) == 56:
                if listStr != "":
                    print("empty")
                    splitList = listStr.split("\n")
                
                    if splitList:
                        for i in splitList:
                            with open(f"{ROOT_DIR}/files/players.txt" , 'a') as s:
                                s.write(i)
                split_males(8, 7)
                return redirect('/')
            else:
                error = "Male players count should be 56"
        
        if 'Shuffle_Females' in request.POST:
            listStr = request.POST['name2']
            listOfStr = listStr.split("\n")
            if len(listOfStr) == 24:
                if listStr != "":
                    print("empty")
                    splitList = listStr.split("\n")
                
                    if splitList:
                        for i in splitList:
                            with open(f"{ROOT_DIR}/files/female_players.txt" , 'a') as s:
                                s.write(i)
                split_females(8, 3)
                return redirect('/')
            else:
                error2 = "Female players count should be 24"

        if 'Clear' in request.POST:
            with open(f"{ROOT_DIR}/files/female_players.txt" , 'r+') as file:
                    file.truncate(0)
            for i in team_list:
                os.remove(f"{all_teams_txt_path}/{i}")
            return redirect('/')
                
    
        
    return render(request, 'base.html', 
        {
            'players': players, 
            'male_players':male_players,
            'female_players':female_players,
            'num_of_teams': num_of_teams,
            'all_team_list':team_list_2,
            'error': error,
            'error2': error2,
        })






def room(request):
    return render(request, 'room.html' )
