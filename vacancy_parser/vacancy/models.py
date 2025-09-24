from django.db import models


class Vacancies(models.Model):

    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    # description = models.TextField(null=True, blank=True)
    # salary_from = models.IntegerField(null=True, blank=True)  # Минимальная зарплата
    # salary_to = models.IntegerField(null=True, blank=True)    # Максимальная зарплата
    # salary_currency = models.CharField(max_length=3, null=True, blank=True)
    # company = models.CharField(max_length=128, null=True, blank=True)
    # allowed_time = models.DateTimeField(auto_now_add=True)
    # site = models.CharField(max_length=64)
    site_id = models.CharField(max_length=128, null=True, blank=True)
    # company_rating = models.FloatField(null=True, blank=True)

    # class Meta:
        # verbose_name = _("")
        # verbose_name_plural = _("s")

    def __str__(self):
        return self.title
    
    # @property
    # def salary(self):
    #     """Вычисляемое поле для обратной совместимости"""
    #     if not self.salary_data:
    #         return 0
    #     if self.salary_data.get('from') and self.salary_data.get('to'):
    #         return (self.salary_data['from'] + self.salary_data['to']) // 2
    #     return self.salary_data.get('from') or self.salary_data.get('to') or 0

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
