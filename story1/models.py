from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length = 150, null = True)
    lecturer = models.CharField(max_length = 150, null = True)
    credits = models.PositiveIntegerField(null = True)
    description = models.TextField(max_length = 250, null = True)
    TERM_CHOICES = (
        ('odd', 'odd'),
        ('even', 'even')
    )
    term = models.CharField(
        max_length = 5,
        choices = TERM_CHOICES,
        default = 'odd',
        null = True
    )
    ACADEMIC_YEAR = (
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022')
    )
    academic_year = models.CharField(
        max_length = 10,
        choices = ACADEMIC_YEAR,
        default = '2020/2021',
        null = True
    )
    room = models.CharField(max_length = 20, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return '{}'.format(self.course_name)

# class Event(models.Model):
#     event = models.CharField(max_length = 50, null = True)
#     brief_description = models.CharField(max_length = 200, null = True)
#     complete_description = models.TextField(max_length = 1000, null = True)

#     def __str__(self):
#         return '{}'.format(self.event)

# class Visitor(models.Model):
#     visitor_name = models.CharField(max_length = 75, null = True)
#     visitor_age = models.PositiveIntegerField(null = True)
#     ID_TYPE = (
#         ('KTM', 'KTM'),
#         ('KTP', 'KTP'),
#         ('SIM', 'SIM'),
#         ('Passport', 'Passport'),
#     )
#     id_type = models.CharField(
#         max_length = 10 ,
#         choices = ID_TYPE,
#         default = 'KTM',
#         null = True
#     )
#     identity_number = models.CharField(max_length = 75, null = True)
#     event = models.ForeignKey(Event, on_delete = models.CASCADE)

#     def __str__(self):
#         return '{}'.format(self.visitor_name)