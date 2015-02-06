from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# League models (reference these in other apps):
class Sports(models.Model):
    sportName = models.CharField(max_length = 30)
    displayName = models.CharField(max_length = 80)
    def __unicode__(self):
        return self.sportName

class Rules(models.Model):
    rulesName = models.CharField(max_length = 80)
    rulesDescription = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.rulesName

class League(models.Model):
    leagueName = models.CharField(max_length = 100)
    ruleFormat = models.ForeignKey(Rules)
    isPrivate = models.BooleanField(default = False)
    password = models.CharField(max_length = 40, null = True, blank = True)
    # isActive
    creator = models.ForeignKey(User)
    sportId = models.ForeignKey(Sports)
    def __unicode__(self):
        return self.leagueName

class LeagueUsers(models.Model):
    leagueId = models.ForeignKey(League)
    userId = models.ForeignKey(User)
    def __unicode__(self):
        return self.userId.username + self.leagueId.leagueName


# NCAA football bowl game and playoff models:
class ncaafTeam(models.Model):
    espnName = models.CharField(max_length = 80)
    displayName = models.CharField(max_length = 80)
    displayInitial = models.CharField(max_length = 2)
    displayInitial2 = models.CharField(max_length = 2)
    def __unicode__(self):
        return self.displayName

class ncaafGame(models.Model):
    espnName = models.CharField(max_length = 80)
    displayName = models.CharField(max_length = 80)
    def __unicode__(self):
        return self.displayName

class ncaafMatchups(models.Model):
    season = models.CharField(max_length = 40)
    gameId = models.ForeignKey(ncaafGame)
    homeTeam = models.ForeignKey(ncaafTeam, null=True, related_name='homeTeam')
    visitTeam = models.ForeignKey(ncaafTeam, null=True, related_name='visitTeam')
