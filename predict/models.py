from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    depressive = models.FloatField(default=0)
    suicide = models.FloatField(default=0)
    cyberbullying = models.FloatField(default=0)
    total = models.IntegerField(default=0)
    time = models.FloatField(default=0)
    graph_home = models.JSONField(default=list)
    graph_dep = models.JSONField(default=list)
    graph_sui = models.JSONField(default=list)
    graph_cyb = models.JSONField(default=list)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'predict'
        db_table = 'person'  # Specify the name of the database table
        managed = True
        default_related_name = 'person'
        verbose_name = 'person'
        verbose_name_plural = 'people'
        db_tablespace = ''
        # Remove the invalid db_template attribute
        # db_template = 'template0'
        abstract = False
        indexes = []
        constraints = []
        db_tablespace = ''
