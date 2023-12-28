from django.contrib import admin
from singup_in.models import cheakTable,makePersionalDe

class CheakAdminTable(admin.ModelAdmin):
    list_display=('ids','name','dep','code')

admin.site.register(cheakTable,CheakAdminTable)

class makePersionalAdmin(admin.ModelAdmin):
    list_display=('id','name','email','department','dep_code','password')
admin.site.register(makePersionalDe,makePersionalAdmin)
