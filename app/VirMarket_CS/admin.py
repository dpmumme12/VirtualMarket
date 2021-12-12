import json
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from .models import Transactions, User_Finances, Stocks, User_Finance_History, newstats

# Register your models here

admin.site.register(Transactions)
admin.site.register(User_Finances)
admin.site.register(Stocks)
admin.site.register(User_Finance_History)
admin.site.register(Permission)

@admin.register(newstats)
class NewStatsAdmin(admin.ModelAdmin):
    
    def changelist_view(self, request, extra_context=None):

        stat_data = (
            newstats.objects.annotate().values('win', 'mac', 'iphone', 'android', 'other')
        )

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {'stats_data': as_json}

        return super().changelist_view(request, extra_context=extra_context)