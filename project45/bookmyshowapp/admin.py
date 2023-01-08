from django.contrib import admin
from bookmyshowapp.models import MovieInfo

# Register your models here.
class MovieInfoAdmin(admin.ModelAdmin):
	list_display=['moviename','hero','heroine','releasedate','rating','director','timing','language']

admin.site.register(MovieInfo,MovieInfoAdmin)