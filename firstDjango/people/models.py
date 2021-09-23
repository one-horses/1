from django.core.paginator import Paginator
from django.db import models
from django.db.models import Manager

# 项目信息
class Person(models.Model):
    ID = models.AutoField(primary_key = True,verbose_name='序号')
    age = models.CharField(verbose_name='项目编号',max_length=128)
    name = models.CharField(verbose_name='项目名称', max_length=128)
    xiangmjingl = models.CharField(verbose_name='项目经理', max_length=128)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    last_time = models.DateTimeField(auto_now=True,verbose_name='上次更新时间')
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'Person'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



    # def result(self):
    #     res =Person.objects.all()
    #     choices= [(x.ID,x.name) for x in res]
    #     print(choices)
    #     return choices
    #       # 返回结果即为列表页中显示的数据值
    # result.short_description = '序号'


class Family(models.Model):
    lq = Manager()  # Manager类在模型类中如果没有重写的话，默认django会为开发人员实例化一个objects对象
    CHILDREN_CHOICE = (
            (1, '湖北省'),
            (2, '湖南省'),
            (3, '广东省'),
            (4, '安徽省'),
            (5, '四川省'),
            (6, '宁夏回族自治区')
        )
    Parents_CHOICE = (
        ('军史馆', '军史馆'),
        ('博物馆', '博物馆'),
        ('展会', '展会'),

        )
    age = models.CharField(verbose_name='出差编号', max_length=128)
    husband = models.ForeignKey(Person,on_delete=models.CASCADE,verbose_name="项目名称",max_length=12,)
   # charfield时，max_length参数是必须要添加的
    wife = models.CharField(max_length=12, verbose_name='项目经理')
    children = models.IntegerField(choices=CHILDREN_CHOICE,verbose_name='目的地')
    parent = models.CharField(choices=Parents_CHOICE, max_length=12,verbose_name='项目类别')  # charfield最大长度为2的31次方-1
    c_date = models.DateField(max_length=12,default='',verbose_name='出差开始时间')  # auto_created表示将当前的时间作为该数据的创建时间
    b_date = models.DateField(max_length=12,default='',verbose_name='出差结束时间')  # auto_created表示将当前的时间作为该数据的创建时间

    # auto_now将当前的时间作为这一条数据的创建时间
    # 如果没有设置元类来设置表名的话，默认情况下，数据库表名的格式为：子应用名小写_模型类类名小写
    # 当模型类发生了改变时，需要重新迁移然后重新生成表
    class Meta:
        """Meta和db_table不要自定义名字"""
        db_table = 'table_family'  # 设置数据库表的表名
        verbose_name = '出差管理'
        verbose_name_plural = verbose_name
    def data_count(self):
        b =self.b_date-self.c_date
        # print(type(b))
        return b.days
    data_count.short_description = '出差天数'
    def __str__(self):
        return self.age


class Husbands(models.Model):
    CHILDREN_CHOICE = (
        (1, '采购经费'),
        (2, '活动经费'),
        (3, '差旅费'),
        (4, '邮寄费'),
        (5, '其他')
    )
    name = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="项目名称", max_length=12, )
    age = models.OneToOneField(Family, on_delete=models.CASCADE, verbose_name="出差编号", max_length=12,)
    height = models.IntegerField(choices=CHILDREN_CHOICE,verbose_name='报销类别')
    salary = models.FloatField(verbose_name='预支金额')
    weight = models.FloatField(verbose_name='报销金额')
    birthday = models.CharField(verbose_name='费用明细',max_length=128)
    image1 = models.ImageField(upload_to='baoxiaodan', verbose_name='报销单', null=True)
    image2 = models.ImageField(upload_to='baoxiaoxiangdan', verbose_name='报销详单', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_time = models.DateTimeField(auto_now=True, verbose_name='上次更新时间')

    class Meta:
        db_table = 'Husbands'
        verbose_name = '报销管理'
        verbose_name_plural = verbose_name



class Wife(models.Model):
    name = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name="项目名称", max_length=12, )
    c_date = models.DateField(max_length=12, default='', verbose_name='项目开工时间')  # auto_created表示将当前的时间作为该数据的创建时间
    b_date = models.DateField(max_length=12, default='', verbose_name='项目验收时间')
    weight = models.IntegerField(verbose_name='工期')
    filename = models.FileField(upload_to ='upload', verbose_name='项目文档', null=True)

    class Meta:
        db_table = 'Wife'
        verbose_name = '项目文档'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.filename

# class Children(models.Model):
#     Children_choice = (
#             (1, '男'),
#             (2, '女')
#         )
#
#     name = models.CharField(verbose_name='孩子姓名', max_length=8)
#     age = models.IntegerField(verbose_name='年龄')
#     sex = models.CharField(choices=Children_choice, verbose_name='性别', max_length=2)
#     father = models.ForeignKey(Husbands, on_delete=models.CASCADE, related_name='dad')  # 多对一
#     mother = models.ForeignKey(Wife, on_delete=models.CASCADE, related_name='mom')
#
#     class Meta:
#         db_table = 'Children'
#         verbose_name = '孩子'
#         verbose_name_plural = verbose_name




# Create your models here.
