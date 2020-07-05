from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm

class ReviewInLine(admin.TabularInline):
    model = Review

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'review_count')
    list_filter = ('brand', 'model', )
    search_fields = ('model', 'brand', )
    ordering = ('id', )
    inlines = [
        ReviewInLine
    ]


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title', )
    search_fields = ('title', )
    ordering = ('car', )

admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
