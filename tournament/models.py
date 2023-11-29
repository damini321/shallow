from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    def matches_played(self):
        return self.team_matches.count()

    def matches_won(self):
        return self.team_matches.filter(match__winner=self).count()

    def matches_lost(self):
        return self.matches_played() - self.matches_won()

    def __str__(self):
        return str(self.country)

class Match(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()

    def __str__(self):
        return str(self.team)
    