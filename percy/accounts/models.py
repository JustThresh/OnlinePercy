from django.db import models


# Create your models here.
class TestModel(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='主键id')
    name = models.CharField(default='123456', max_length=12)
    pwd = models.CharField(default='', max_length=12, null=False)
    role = models.IntegerField(default=1)  # 0管理员，1.普通网站用户, 2.其他

    class Meta:
        db_table = 'test_model'


class DjangoPro(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='主键id')
    name = models.CharField(default='123456', max_length=12)

    class Meta:
        db_table = 'django_pro'


# 广告页提示语
class Words(models.Model):
    body = models.TextField(default="", verbose_name="广告提示语")

    class Meta:
        verbose_name = "广告提示语"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.body
