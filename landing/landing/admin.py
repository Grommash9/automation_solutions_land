from django.contrib import admin
from django import forms

from .models import TeamMember, WorkExample


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'member_name', 'position_title', 'avatar_name')
    search_fields = ['member_name']


@admin.register(WorkExample)
class WorkExampleAdmin(admin.ModelAdmin):
    list_display = ('work_id', 'title')
    search_fields = ['description', 'title']

