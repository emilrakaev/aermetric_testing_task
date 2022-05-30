from django.db import models

USUAL = 'Usual'
EASY = 'Easy'
HARD = 'Hard'
PRIORITY = (
    (USUAL, USUAL),
    (EASY, EASY),
    (HARD, HARD),
)

LOWER_A = 'Lower A'
LOWER_B = 'Lower B'
PAIRED_A = 'Paired A'
PAIRED_B = 'Paired B'
UPPER_A = 'Upper A'
PRELEGEND = 'PreLegend'
LEGEND = 'Legend'
REPEAT_LEGEND = 'Repeat Legend'
WARNING = 'Warning'

TYPE = (
    (LOWER_A, LOWER_A),
    (LOWER_B, LOWER_B),
    (PAIRED_A, PAIRED_A),
    (PAIRED_B, PAIRED_B),
    (UPPER_A, UPPER_A),
    (PRELEGEND, PRELEGEND),
    (LEGEND, LEGEND),
    (REPEAT_LEGEND, REPEAT_LEGEND),
    (WARNING, WARNING),
)

FINISHED = 'Finished'
INPROGRESS = 'In progress'
STARTED = 'Started'
KICKBACK = 'Kickback'
SUSPEND = 'Suspend'
STATUS = (
    (FINISHED, FINISHED),
    (INPROGRESS, INPROGRESS),
    (STARTED, STARTED),
    (KICKBACK, KICKBACK),
    (SUSPEND, SUSPEND),
)


class AircraftErrorData(models.Model):
    priority = models.CharField(max_length=50, choices=PRIORITY)
    type = models.CharField(max_length=50, choices=TYPE)
    aircraft = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)
    errors_count = models.IntegerField(default=0)
    info_count = models.IntegerField(default=0)

    def __str__(self):
        return f'id - {self.id} aircraft - {self.aircraft} errors_count - {self.errors_count}'
