from django.contrib import admin

from cohort.models import Cohort


class CohortAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Cohort, CohortAdmin)
