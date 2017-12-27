from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)

class Characters(models.Model):

    nick = models.CharField(max_length=200, verbose_name='Имя персонажа')
    SEX_CHOICE = (
        ('Y', 'Мальчик'),
        ('N', 'Девочка'),
        ('X', 'Оно'),
    )
    sex = models.CharField(max_length=200, choices=SEX_CHOICE, verbose_name='Пол')
    avatar = models.ImageField(verbose_name='Аватар', blank=True)
    author = models.CharField(max_length=200, verbose_name='Автор')
    APPROVED_CHOICE = (
        ('Y', 'Да'),
        ('N', 'Нет'),
    )
    approved = models.CharField(max_length=200, choices=APPROVED_CHOICE, verbose_name='Одобрено')

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'персонажи'

    def __str__(self):
        return self.nick

class Owls(models.Model):

    name = models.CharField(max_length=1000, verbose_name='Имя совы')
    where_now = models.CharField(max_length=200, verbose_name='У кого находится')
    picture = models.ImageField(verbose_name='Аватар', blank=True)
    master = models.IntegerField()
    time_from = models.DateTimeField(default=timezone.now(), verbose_name='Время вылета совы')
    time_to = models.DateTimeField(default=timezone.now() + timedelta(hours=1), verbose_name='Время прилета совы')
    message = models.IntegerField()

    class Meta:
        verbose_name = 'Сова'
        verbose_name_plural = 'совы'

    def __str__(self):
        return self.name

class Letters(models.Model):

    # from_adr = models.CharField(max_length=200, verbose_name='От кого', blank=True)
    send_to = models.CharField(max_length=200, verbose_name='Кому')
    message = models.CharField(max_length=200, default='SOME STRING', verbose_name='Кому')
    # departure = models.DateTimeField('date published')
    # arrival = models.DateTimeField('date published')
    # owl_id = models.IntegerField(blank=True)
    # reading_time = models.DateTimeField('date published')
    # message = models.CharField(max_length=1000, default='SOME STRING', verbose_name='Текст')

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'письма'

    def __str__(self):
        return self.title

class TestForm(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    message = models.CharField(max_length=1000, verbose_name='Текст')

    class Meta:
        verbose_name = 'Тестовая форма'
        verbose_name_plural = 'тестовые формы'

    def __str__(self):
        return self.title


class SignUp(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000, default='SOME STRING')
