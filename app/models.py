from django.db import models


class TimeOfSleep(models.Model):
    time_of_sleep = models.DateTimeField("Time Of Sleep")
    datetime = models.DateTimeField("Time when record inserted")
    id_str = models.CharField(max_length=50)

    def __str__(self):
        return "id_str: {}, tos: {}, record time: {}".format(
            self.id_str, self.time_of_sleep, self.datetime
        )
