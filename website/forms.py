from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    middle_initial = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Middle Initial", "class":"form-control"}), label="")
    sex = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sex", "class":"form-control"}), label="")
    strand = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Strand", "class":"form-control"}), label="")
    graduation_year = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Graduation Year", "class":"form-control"}), label="")
    college_university = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"College University", "class":"form-control"}), label="")
    college_course = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"College Course", "class":"form-control"}), label="")
    hei = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Public or Private", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)


