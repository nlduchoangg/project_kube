from skpy import Skype
import credentials

def post_message(msg,channel_id):
  skype_obj = Skype(credentials.username,credentials.password)
  channel = skype_obj.chats.chat(channel_id)
  channel.sendMsg(msg)

# print(skype_obj.chats) #Returns SkypeChats() Not useful
# print(skype_obj.chats.recent()) #aha! This was useful

post_message('Hello! This is my first automatic message.', credentials.group_chat_id)

