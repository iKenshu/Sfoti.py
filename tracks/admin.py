from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('artist', 'title', 'order', 'album', 'player')
	list_filter = ('artist', 'album')
	search_fields = ('title', 'artist__first_name')
	list_editable = ('title', 'album')
	raw_id_fields = ('artist', )



admin.site.register(Track, TrackAdmin)