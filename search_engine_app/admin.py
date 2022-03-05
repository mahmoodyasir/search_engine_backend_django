from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(EveryData)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ['value', 'category']
    list_filter = ['value', 'category']
    list_display = ['id', 'value', 'description', 'category', 'search_count']


class SearchRecordAdmin(admin.ModelAdmin):
    search_fields = ['user_id', 'search_id']
    list_filter = ['user_id', 'search_id']
    list_display = ['id', 'user_id', 'search_id', 'search_value', 'search_date', 'search_time']


admin.site.register(SearchRecord, SearchRecordAdmin)
