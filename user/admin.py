from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin):
    # fields = ('username','nickname','email')            # 设置记录 add 或 update 时显示的字段
    # exclude = ('username','nickname')                  # 设置记录 add 或 update 时不显示的字段
    # fieldsets：分组显示
    fieldsets = (
        ('first',{
            'fields': ('username', 'password')
        }),
        ('second', {
            'fields': ('nickname', 'email')
        }),
    )
    list_display = ( 'username', 'nickname','email','sex')  # 列表显示字段
    search_fields = ('username','nickname')              # 条件搜索字段
    list_filter = ('username',)                            # 列表右边显示过滤器
    date_hierarchy = 'last_login'                          # 设置一个日期字段作为钻取条件
    list_per_page = 1                                       # 控制列表每页的记录数
    ordering = ('-username',)                              # 降序

    # actions_on_top = True
    # actions_on_bottom = True
    # actions_selection_counter = True


admin.site.register(User,UserAdmin)
