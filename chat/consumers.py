# # Sync to sync channels
# from django.contrib.auth.models import User
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import AsyncWebsocketConsumer
# import json
# from .models import Message


# class ChatConsumer(AsyncWebsocketConsumer):

#     # first command function to execute by returning the initial messages to the client
#     def fetch_messages(self , data):
#         messages  = Message.last_10_messages
#         print('DB messages => '+messages) 
#         print('Converting messages to json => '+self.messages_to_json(messages))
#         content = {
#             'command':'messages',
#             'messages' : self.messages_to_json(messages)
#         }
#         print('Gotten Messages from DB =>' + content)
#         self.send_initial_messages(content)
    


    
#     # command function when new conversation starts
#     def new_message(self, data):
#         author = data['from']
#         author_user = User.objects.filter(username = author)[0]
#         message = Message.objects.create(author=author_user, content=data['message'])
#         content = {
#             'command':'new_message',
#             'message': self.message_to_json(message)
#         }

#         return self.send_chat_message(content)
        
        
#     # function to convert each initial messages to json
#     def messages_to_json(messages):
#         result = []
#         for message in messages:
#             result.append(self.message_to_json(message))

#         return result
    
#     # function to convert each message to json
#     def message_to_json(message):
#         print(message)
#         return {
#             'id':message.id,
#             'author': message.author.username,
#             'message': message.content,
#             'timestamp' : str(message.timestamp)
#         }

        




# # command section starts 

#     commands = {
#         'fetch_messages':fetch_messages,
#         'new_message': new_message
#     }

# # command section ends




#     # the connection starts inidiately the websocket is initialized
#     def connect(self):
#         print(self.scope)
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s'  % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)


#         # it accepts the web socket connection / and must be called last if u want to accept the connection
#         self.accept()

#     # the connection starts inidiately the websocket/chatsocket is closed
#     def disconnect(self , close_code):
#        #leaves a group
#        astnc_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name )

    
#     # Receive message from websocket FIRST HIT FROM WEBSOCKET
#     def receive(self , text_data):
#         data = json.loads(text_data)
#         #we must invoke this  command immediately the chat starts to preload the chat
#         self.commands[data['commands']](self, data)  


#     # function to be called when sending initial messages
#     def send_initial_messages(self, message):
#         self.send(text_data = json.dumps({'message' : message }))


#     # function to be called when having new conversation
#     def send_chat_message(self , message):        
#         # send message to room group
#         # it works like just react-redux dispatch({'type':'',payload': value'})
#         async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'type':'chat_message','message' : message} )



#     # Received message from room group is now sent back to the frontend js to append chat
#     # this function invoke the onmessage event on the web socket handler
#     def chat_message(self, event):
#         message = event['message']

#         # send message to websocket
#         self.send(text_data = json.dumps(message))
















# ASYNCHRONOUS channels

# from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s'  % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name )


        # it accepts the web socket connection / and must be called last if u want to accept the connection
        await  self.accept()


    async def disconnect(self , close_code):
       #leaves a group
       await self.channel_layer.group_discard(self.room_group_name, self.channel_name )

    
    # Receive message from websocket
    async def receive(self , text_data):
        # print(type(text_data))  # JSON string coming from the server
        text_data_json = json.loads(text_data)
        # print(type(text_data_json))  #python dictionary accessed using key index
        message = text_data_json['message']

        # send message to room group
        # it works like just react-redux dispatch({'type':'',payload': value'})
        await self.channel_layer.group_send(self.room_group_name, {'type':'chat_message','message' : message} )


    # Receives message from room group is now sent back to the frontend js to append chat
    async def chat_message(self, event):
        message = event['message']
        # print( event )
        # send message to websocket
        # print(json.dumps('socket message : ',message))
        await self.send(text_data = json.dumps({
            'message':message
        }))

















# SYNCHRONOUS

# # chat/consumers.py
# import json
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         # print(text_data) //recieves a text format of json
#         text_data_json = json.loads(text_data) #convert the text to json using json.loads("{'message':'themessage'}") 
#         # print(text_data_json)
#         message = text_data_json['message'] #accessing the message value from the converted json format

#         # then the consumer returns back the data in json format using json.dumps({'message':message})
#         print(json.dumps({'message':message}))
#         self.send(text_data=json.dumps({
#             'message': message
#         }))