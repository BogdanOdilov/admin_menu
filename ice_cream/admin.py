from django.contrib import admin

from .models import TreeMenu, TreeMenuCategory, models


class MenuItemInline(admin.TabularInline):
    model = models.MenuItem

    list_display = ['name', 'url']
    search_fields = ['name', 'url', 'title']
    

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['slug', 'name']

    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]


admin.site.register(models.Menu, MenuAdmin)

@admin.register(TreeMenuCategory)
class TreeMenuCategoryAdmin(admin.ModelAdmin):

    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):

    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]

