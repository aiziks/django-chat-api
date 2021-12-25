from django.contrib import admin
from chat.models import GroupChat , Message
# Register your models here.

admin.site.register(Message)

# class GroupChatAdmin(admin.ModelAdmin):
#     ''' enable chat group admin'''
#     list_display = ('id' , 'name' , 'description' , 'icon' , 'mute_notification' )
#     list_filter = ('id' , 'name' , 'description' , 'icon' , 'mute_notification' )
#     list_display_links = ('name' , )


# admin.site.register(GroupChat , GroupChatAdmin)