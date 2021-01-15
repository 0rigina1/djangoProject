from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline): # TabularInline 扁平化类 StackedInline 正常
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基础信息', {'fields': ['questionText']}),
        ('发布时间', {'fields': ['pubDate'], 'classes': ['collapse']}), # 'classes': ['collapse'] 隐藏字段
    ]

    inlines = [ChoiceInline]
    list_display = ('questionText', 'pubDate', 'wasPublishedRecently')
    list_filter = ['pubDate'] # 增加一个根据pubDate的筛选器
    search_fields = ['questionText'] # 增加一个根据questionText的搜索器


admin.site.register(Question, QuestionAdmin)