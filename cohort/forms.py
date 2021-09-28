from django import forms

from cohort.models import Cohort


class CohortCreationForm(forms.ModelForm):

    class Meta:
        model = Cohort
        fields = "__all__"
