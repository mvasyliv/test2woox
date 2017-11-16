import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class Hall(models.Model):
    #! Інформація про зал
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    hall_name = models.CharField(max_length=30,
                                 verbose_name=_("Назва залу"))
    description = models.CharField(max_length=200,
                                   verbose_name=_("Примітка"),
                                   blank=True,
                                   null=True)
    hall_length = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      verbose_name=_("Довжина залу"),
                                      help_text=_("в метрах"))
    hall_width = models.DecimalField(max_digits=5,
                                     decimal_places=2,
                                     verbose_name=_("Ширина залу"),
                                     help_text=_("в метрах"))

    def __str__(self):
        return _("Зал: {}").format(self.hall_name)


class Board(models.Model):
    #! Інформація по столу
    number_choose = (
        (1,'1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )

    form_choose = (
        ('R', _('Прямокутний')),
        ('O', _('Овальний'))
    )

    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    hall = models.ForeignKey('Hall', verbose_name=_("Зал"))
    board_number = models.IntegerField(verbose_name=_("№ стола"),
                                       choices=number_choose)
    number_seats = models.IntegerField(verbose_name=_("Кількість місць"),
                                       choices=number_choose,
                                       default=2)
    board_form = models.CharField(max_length=1,
                                  verbose_name=_("Форма стола"),
                                  choices=form_choose,
                                  default='R')
    board_length = models.DecimalField(max_digits=5,
                                       decimal_places=2,
                                       verbose_name=_("Довжина стола"),
                                       help_text=_("в % від довжини залу"))
    board_width = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      verbose_name=_("Ширина стола"),
                                      help_text=_("в % від ширини залу"))
    coordinate_horizontal = models.DecimalField(max_digits=5,
                                                decimal_places=2,
                                                verbose_name=_("Координата стола в залі по горизонталі"),
                                                help_text=_("в %"))
    coordinate_vertical = models.DecimalField(max_digits=5,
                                              decimal_places=2,
                                              verbose_name=_("Кордината стола в залі по вертикалі"),
                                              help_text=_("в %"))
    description = models.CharField(max_length=200,
                                   verbose_name=_("Примітка"),
                                   blank=True,
                                   null=True)

    class Meta:
        #! унікальний індекс по двох полях
        unique_together = [
            ('hall', 'board_number')
        ]

    def __str__(self):
        return _("№ стола: {}. Кількість місць: {}").format(self.board_number, self.number_seats)

class OrderHeader(models.Model):
    #! Заголовок замовлення стола
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    customer_name = models.CharField(max_length=200,
                                     verbose_name=_("Ім'я"))
    customer_email = models.EmailField(verbose_name=_("Електронна адреса"))
    customer_mobile = models.CharField(max_length=50,
                                       verbose_name=_("Контактний телефон"))
    order_date = models.DateTimeField(verbose_name=_("Дата замовлення"),
                                      default=timezone.now)
    ordered_by_date = models.DateTimeField(verbose_name=_("Замовлено на дату"))
    description = models.CharField(max_length=200,
                                   verbose_name=_("Примітка"))

    def __str__(self):
        return _("Замовлення {} на {}").format(self.customer_name, self.ordered_by_date)


class OrderDetails(models.Model):
    #! Позиції в замовленні
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    order_header = models.ForeignKey('OrderHeader', verbose_name=_("Замовлення"))
    board_number = models.ForeignKey('Board', verbose_name=_("Стіл"))
    number_line = models.IntegerField(verbose_name=_("№ позиції"))
    description = models.CharField(max_length=200,
                                   verbose_name=_("Примітка"))


    def __str__(self):
        return _("№ позиції: {}").format(self.number_line)

