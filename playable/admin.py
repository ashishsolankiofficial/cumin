from django.contrib import admin
from playable.models import PlayableCategories, PlayableGroup, MultiChoice, Choice

class PlayableCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlayableGroupAdmin(admin.ModelAdmin):
    exclude = ('ext_id',)
    list_display = ('description',)

class MultiChoiceAdmin(admin.ModelAdmin):
    exclude = ('ext_id',)
    list_display = ('description',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('description',)


admin.site.register(PlayableCategories, PlayableCategoriesAdmin)
admin.site.register(PlayableGroup, PlayableGroupAdmin)
admin.site.register(MultiChoice, MultiChoiceAdmin)
admin.site.register(Choice, ChoiceAdmin)
