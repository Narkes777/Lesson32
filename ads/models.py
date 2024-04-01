from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


def get_first_author():
    return Author.objects.first()

class Ad(models.Model):
    STATUSES = ((None, 'Выберите статус рекламы'),
                ('s', 'Продано'),
                ('a', 'Активна'),
                ('c', 'Отменена'))


    # CASCADE
    # SET (Ставит переданное значение)
    # SET_DEFAULT - ставит значени по умолчанию
    # SET_NULL - ставит None
    # PROTECT - не дает удалить первичную модель
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, verbose_name="Имя рекламы", help_text='Здесь заполняется имя рекламы', default='Имя по умолчанию', unique=True)
    status = models.CharField(max_length=1, choices=STATUSES, default='a', verbose_name='Статус рекламы')
    content = models.TextField(null=True, blank=True, verbose_name="Содержание рекламы", unique_for_year='published')
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def title_and_price(self):
        if self.price:
            return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
        ordering = ['price']
        # unique_together = (('name', 'price'))
        # get_latest_by = 'price' Ad.objects.last()

    def __str__(self):
        return self.name + ' ' + str(self.price)

    def save(self, *args, **kwargs):
        ad = super().save(*args, **kwargs) # None
        print(ad)
        return ad

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name




# class TestModel(models.Model):
#     name = models.CharField(max_length=100) # обязательный аттрибут max_length
#     content = models.TextField()
#     email = models.EmailField()
#     url = models.URLField()
#     is_active = models.BooleanField()
#     is_member = models.NullBooleanField()
#     price = models.IntegerField()
#     code = models.BigIntegerField()
#     id = models.SmallIntegerField()
#     discounted_price = models.PositiveIntegerField()
#     discount = models.FloatField()
#     new_price = models.DecimalField(max_digits=10, decimal_places=2)
#     date_of_issue = models.DateField(auto_now_add=True)
#     published = models.DateTimeField(auto_now=True)
#     time_of_expiration = models.TimeField()
#     bin_code = models.BinaryField()



# 1) objects.get() - Поиск по уникальному полю -> Ad
# 2) objects.all() - Все элементы
# 3) objects.create() - создание модели без необходимости вызывать метод save() самостоятельно
# 4) <название модели>_set - менеджер обратной связи (от первичной модели к вторичной)




