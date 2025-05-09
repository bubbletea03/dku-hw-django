from django.contrib import admin
from django.db.models import Avg
from PortfolioApp.models import Project, Rating

admin.site.register(Rating)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'average_rating')  # 'average_rating'은 아래 메서드 이름

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(avg_rating=Avg('rating__rating')).order_by('-avg_rating')
        self.project_ranking_map = {
            project.id: rank + 1 for rank, project in enumerate(qs)
        }
        
    def average_rating(self, obj):
        avg = obj.rating_set.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 2)
    # average_rating.admin_order_field = 'rating__avg'  # 정렬 가능하게
    average_rating.short_description = '평균 평점'

    def ranking(self, obj):
        return self.project_ranking_map.get(obj.id, '-')
    ranking.short_description = '등위'


admin.site.register(Project, ProjectAdmin)