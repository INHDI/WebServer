from django.contrib import admin
from .models import Loaisp, SanPham, SPBan


class LoaispAdmin(admin.ModelAdmin):
    list_display = ('Ma_l','Ten_l')

admin.site.register(Loaisp, LoaispAdmin)


class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('Ma_sp','Ten_sp','Loai_sp')


admin.site.register(SanPham, SanPhamAdmin)


class SPBanAdmin(admin.ModelAdmin):
   list_display = ('San_Pham',)
admin.site.register(SPBan, SPBanAdmin)