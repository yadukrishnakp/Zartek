from django.contrib import admin
from .models import Story, StoryInformation


# Register your models here.

admin.site.register(Story)
admin.site.register(StoryInformation)


# class StoryInformationAdmin(admin.StackedInline):
#     model = StoryInformation
#
#
# @admin.register(Story)
# class StoryAdmin(admin.ModelAdmin):
#     inlines = [StoryInformationAdmin]
#
#     class Meta:
#         model = StoryInformation
#
#
# @admin.register(StoryInformation)
# class StoryInformationAdmin(admin.ModelAdmin):
#     class Meta:
#         model= Story

# class StoryAdmin(admin.StackedInline):
#     model = Story
#
#
# class StoryInformationAdmin(admin.ModelAdmin):
#     inlines = [StoryAdmin]
#
#     class Meta:
#         model = StoryInformation
#
#
# admin.site.register(Story)
# admin.site.register(StoryInformation, StoryInformationAdmin)
