from django.contrib import admin
from principal.models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = MyUser

class MyUserAdmin(UserAdmin):
	form = MyUserChangeForm

	fieldsets = UserAdmin.fieldsets + (
			(None , {'fields':('telefono',)}),
		)

admin.site.register(MyUser,MyUserAdmin)