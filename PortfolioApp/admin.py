from django.contrib import admin
from django.db.models import Avg, Window
from django.db.models.functions import Rank
from PortfolioApp.models import Project, Rating

admin.site.register(Rating)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'average_rating', 'ranking')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(
            avg_rating=Avg('rating__rating'),
            rank = Window(
                expression=Rank(),
                order_by=Avg('rating__rating').desc()
            )
        )
        return qs
        
    def average_rating(self, obj):
        avg = obj.avg_rating
        return round(avg, 2) if avg else "점수 없음"
    average_rating.short_description = '평균 평점'

    def ranking(self, obj):
        return obj.rank
    ranking.short_description = '등위'


admin.site.register(Project, ProjectAdmin)