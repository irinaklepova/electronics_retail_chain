from django.contrib import admin, messages
from django.utils.html import format_html

from trading_network.models import Provider, Product, Contact


@admin.action(description="Очистить задолженность перед поставщиком у выбранных объектов")
def debt_clear(self, request, queryset):
    count = queryset.update(debt=0.00)
    self.message_user(request, f"{count} задолженностей были очищены!", messages.WARNING)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "supplier",
        "supplier_type",
        "level",
        "debt",
        "creation_time",
    )
    readonly_fields = ("supplier_link",)
    list_filter = ("contact__city",)
    actions = [debt_clear]

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/trading_network/provider/{obj.supplier.id}/change/"
            return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
        return "-"
    supplier_link.short_description = "Ссылка на поcтавщика"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "model", "release_date", "supplier",)
    search_fields = ("title",)
    list_filter = ("release_date", "supplier",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "supplier", "email", "country", "city", "street", "house_number",)
    search_fields = ("email",)
    list_filter = ("city",)
