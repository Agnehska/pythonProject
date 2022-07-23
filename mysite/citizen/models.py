from django.db import models


class People(models.Model):
    name = models.CharField('Фамилия, Имя', max_length=100, db_index=True)
    age = models.PositiveSmallIntegerField('Возраст')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True, default=3)
    master = models.CharField('Командир', blank=True, max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/citizen/{self.id}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['name']


class Status(models.Model):
    status = models.CharField('Статус', max_length=100)
    earn = models.PositiveIntegerField('Доход')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['status']
