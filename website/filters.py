import django_filters
from .models import Record
from django import forms

class RecordFilter(django_filters.FilterSet):

    last_name = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Last Name'
        )
    
    strand = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='ABM or STEM:'
        )
    
    graduation_year = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Graduated at Year:'
        )
    
    college_university = django_filters.CharFilter(
        lookup_expr='istartswith', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label = 'College University'
        )

    college_course = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label = 'Enrolled Course'
        )

    hei = django_filters.CharFilter(
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label = 'Public or Private'
        )

    class Meta:
        model = Record
        fields = ['last_name', 'strand', 'graduation_year', 'college_university', 'college_course', 'hei']

    


