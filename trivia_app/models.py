from django.db import models

# Create your models here.

class Person(models.Model):
    """ Save Player name in database """
    name = models.CharField(max_length=40, default='', null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FavPlayer(models.Model):
    name = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return self.color
    

class BestCrickter(models.Model):
    """ Save Best Cricket Player for a person """
    person = models.ForeignKey(
        Person, related_name="person_crickter", on_delete=models.CASCADE, default=''
    )
    fav_player = models.ForeignKey(
        FavPlayer, related_name="fav_player", on_delete=models.CASCADE, default='', null=True,
    )
    # player_name = models.CharField(max_length=50, null=True, blank=True, default='')
    

    # def __str__(self):
    #     return self.player_name

class IndianFlagcolor(models.Model):
    """ Save Indian Flag Colors for a person """
    person = models.ForeignKey(
        Person, related_name="person_flag_color", on_delete=models.CASCADE, null=True,blank=True
    )
    color = models.ForeignKey(
        Color, related_name="flag_color", on_delete=models.CASCADE, null=True,blank=True
    )
    # color = models.CharField(max_length=50, null=True, blank=True, default='')
    

    # def __str__(self):
    #     return self.color