from django.contrib import admin
from .models import Category,Article

class ArticleAdmin(admin.ModelAdmin):
    '''
        1）列表
    '''
    list_display = ('title', 'desc', 'author', 'category')  # 列表显示字段
    search_fields = ('title', 'desc')  # 条件搜索字段
    list_filter = ('title',)  # 列表右边显示过滤器
    date_hierarchy = 'createtime'  # 设置一个日期字段作为钻取条件
    list_per_page = 2  # 控制列表每页的记录数
    ordering = ('-createtime',)  # 降序

    '''
        2）动作actions
    '''
    # actions_on_top = True
    # actions_on_bottom = True
    # actions_selection_counter = True

    '''
        3）add 或 update 页面
    '''
    # fields = ('title','desc','author','category')            # 设置记录 add 或 update 时显示的字段
    # exclude = ('username','nickname')                  # 设置记录 add 或 update 时不显示的字段
    # fieldsets：分组显示
    fieldsets = (
        ('first', {
            'fields': ('title',)
        }),
        ('second', {
            'fields': ('desc', 'content')
        }),
        ('关联字段', {
            'fields': ('author', 'category')
        }),
    )

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
