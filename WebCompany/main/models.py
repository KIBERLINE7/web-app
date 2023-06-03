from django.db import models

class Department(models.Model):
    name_department = models.CharField('Название', max_length=250)

    def __str__(self):
        return self.name_department

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Position_Empl(models.Model):
    name_position = models.CharField('Должность', max_length=250)

    def __str__(self):
        return self.name_position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class Users(models.Model):
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='main/img/img.png')
    login = models.CharField('Логин', max_length=50)
    surname = models.CharField('Фамилия', max_length=250)
    name = models.CharField('Имя', max_length=250)
    secondname = models.CharField('Отчество', max_length=250)
    number_phone = models.CharField('Номер телефона', max_length=50)
    mail = models.CharField('Почта', max_length=250)
    born = models.DateField('Дата рождения')
    date_enter_company = models.DateField('Дата прихода в компанию')
    salary = models.CharField('Зарплата', max_length=250, default="")
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    id_position = models.ForeignKey(Position_Empl, on_delete=models.CASCADE)
    password = models.CharField('Пароль', max_length=250)
    is_authorization = models.BooleanField(default=False)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('login',)

class Tokens(models.Model):
    token = models.CharField('Токен', max_length=250)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'
        unique_together = ('token',)