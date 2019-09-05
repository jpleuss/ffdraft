from django.db import models
from django.urls import reverse




# All Players in DB
class Player(models.Model):
    """The individual players to be drafted"""
    rk = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    pos = models.CharField(max_length=20)
    bye = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Draft instance
class Draft(models.Model):
    draft_round = models.IntegerField(null=False, blank=False)
    draft_team = models.CharField(max_length=100, null=False, blank=False)
    player = models.OneToOneField('Player', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.draft_round, self.draft_team)


    def get_absolute_url(self):
        return reverse('draft-update', kwargs={'pk': self.pk})
