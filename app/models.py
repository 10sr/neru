from django.db import models


class TimeOfSleep(models.Model):
    time_of_sleep = models.DateTimeField("Time Of Sleep")
    datetime = models.DateTimeField("Time when record inserted")
    # Twitter id in number
    id_str = models.CharField(max_length=50)

    def __str__(self):
        return "id_str: {}, tos: {}, record time: {}".format(
            self.id_str, self.time_of_sleep, self.datetime
        )

class TwitterUsername(models.Model):
    # Twitter id in number
    id_str = models.CharField(max_length=50)
    # Twitter screen name
    username = models.CharField(max_length=20)

    def __str__(self):
        return "id_str: {}, username: {}".format(
            self.id_str, self.username
        )
