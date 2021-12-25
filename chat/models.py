from django.db import models
from django.contrib.auth.models import User , Group
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User , related_name='contact' , on_delete=models.CASCADE )
    friends = models.ManyToManyField('self' , blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    contact = models.ForeignKey(Contact , related_name = 'messages' , on_delete = models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.contact.user.username

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]



class Chat(models.Model):
    participants =  models.ManyToManyField(Contact , related_name='chats')
    messages = models.ManyToManyField(Message  , blank = True)

    def last_10_messages(self):
        return self.messages.objects.order_by('-timestamp').all()[:10]
    
    def __str__(self):
        return "{}".format(self.pk)





class GroupChat(models.Model):
    # extends group model to add  extra info
    description = models.TextField(blank = True , help_text='description of group')
    mute_notification = models.BooleanField(default = False)
    icon = models.ImageField(upload_to = '' , help_text='group icon' , blank=True)
    date_created =  models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse('chat:room' , args = [str(self.id)])


        
