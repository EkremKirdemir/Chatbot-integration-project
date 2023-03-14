from fbchat import Client
from fbchat.models import *

client = Client('kirdemir.ekrem@gmail.com', '<ortabayir123>')

# Send a message to a user
client.send(Message(text='Hello, world!'), thread_id='<ekrem.kirdemir>', thread_type=ThreadType.USER)

# Send a message to a group chat
# client.send(Message(text='Hello, group!'), thread_id='<group_id>', thread_type=ThreadType.GROUP)

# Fetch messages from a thread
# messages = client.fetchThreadMessages(thread_id='<thread_id>', limit=10)
# for message in messages:
#     print(message.text)

# Disconnect the client
client.logout()
