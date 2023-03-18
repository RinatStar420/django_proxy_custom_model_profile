from django.db import models


# кастомный менеджер интерфейс через который создается модель django
class PersonManager(models.Manager):

    def get_staff_user(self):
        return super(PersonManager, self).get_queryset().filter(is_staff=True)