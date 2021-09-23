from django.contrib import admin
from people.models import Person, Family, Wife, Husbands
from django.utils.safestring import mark_safe

# admin.site.register(Person)
# admin.site.register(Family)

admin.site.site_header = '项目管理'
admin.site.site_title = '项目管理系统'
admin.site.index_title = '欢迎使用项目管理系统'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['ID', 'age','name','xiangmjingl','create_time','last_time', 'is_delete', ]

    search_fields = ['age','name']
    # fields = ['name']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('ID',)



    # list_editable 设置默认可编辑字段
    # list_editable = ['age', 'name']

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id','age','husband', 'wife', 'children', 'parent', 'c_date','b_date','data_count']
    actions_on_bottom = True
    actions_on_top = True
    ordering = ('id',)

    search_fields = ['age', 'husband']





@admin.register(Husbands)
class HusbandsAdmin(admin.ModelAdmin):
    def show_img1(self, obj):  # obj为模型类对象
        try:
            img = mark_safe(
                '<a href="%s"><img src="%s" height="35px" weight="35px"></a>' % (obj.image1.url, obj.image1.url))
            # print(img)
        except:
            return ''
        return img
    show_img1.short_description ='报销单'

    def show_img2(self, obj):  # obj为模型类对象
        try:
            img = mark_safe(
                '<a href="%s"><img src="%s" height="35px" weight="35px"></a>' % (obj.image2.url, obj.image2.url))
        except:
            return ''
        return img
    show_img2.short_description ='报销详单'
    search_fields = ['name', 'age']
    list_per_page = 20  # 表示每一页只展示两条数据，值类型为整型，为几就表示展示几条数据
    list_display = ['id', 'name','age', 'height', 'salary', 'weight', 'birthday', 'show_img1', 'show_img2',]
    # 将模型类的字段显示在列表页
    actions_on_bottom = True
    actions_on_top = True
    ordering = ('id',)

@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'c_date', 'b_date', 'weight', 'filename']
    actions_on_bottom = True
    actions_on_top = True
    ordering = ('id',)
    search_fields = ['name', ]

    fieldsets = (
        ('基本信息', {'fields': ['name', 'c_date', 'b_date', 'weight']}),
        ('附件', {
            'fields': ['filename'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )

# Register your models here.
