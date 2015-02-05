# webscrape.py

from bs4 import BeautifulSoup
import requests
import re
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bowlgames.settings')

import bowlgames
from django.contrib.auth.models import User
from picks.models import *

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

# Find winners and save to database
winTeam = []

games = soup.find_all('div', class_='gameDay-Container')
for game in games:
    winners = game.find_all('div', class_='winner-arrow', style='display:block')
    for team in winners:
        winTeam.append(re.sub(r'^[0-9]+|;', '', team.parent.find('p', class_='team-name').text.strip()))

# for tm in winTeam:
#     print tm

for tm in Team.objects.filter(game__season = currentseason):
    if tm.team in winTeam:
        tm.win = tm.game.weight
        tm.save()

# Get game total scores
for gm in soup.find_all('div', class_='game-notes'):
    if champgame in gm.text:
        scores = gm.parent.find_all('li', class_='final')
        total = int(scores[1].text) + int(scores[2].text)
        bcschamp = Game.objects.filter(season=currentseason, game__contains=champgame)[0]
        bcschamp.totalscore = total
        bcschamp.save()

# Get all in one pass
for gm in soup.find_all('div', class_='game-notes'):
    # get game total score
    scores = gm.parent.find_all('li', class_='final')
    total = int(scores[1].text) + int(scores[2].text)
    # Get game winner
    winner = re.sub(r'^[0-9]+|;', '', gm\
        .parent.find('div', class_='winner-arrow', style='display:block')\
        .parent.find('p', class_='team-name').text.strip())
    # Match game in html to game in database
    this_game = Game.objects.filter()
    # Assign values to game
    this_game.totalscore = total
    this_game.team_set.filter(team = winner)[0].win = True
    this_game.save()











#
