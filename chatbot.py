from fbchat import Client
from fbchat.models import *
import facebook
import requests
access_token = 'EAAvlbQDWvOkBAHpitAmVmSS7GCmzsEftuwc8ZAZAFCJzZBGcsxTA9KWPXzVCmiJI0eFqnFig5y5zKfL9a0rLAAIwrRW87VKOzTH93ihZBxt1GXCnttPo7BqZB8iKSo7ZBdiNS2Qe0MfeZA0faBbgVvZB7xZB37rBaxCCaLMRHtOQMgMnIqtvvjCK8ZCIXyyNgT1wDHSTn0ISktuTGmJrd5EzQ9bdap6ZAoWcUMZD'
graph = facebook.GraphAPI(access_token)

# Make an API request using the Graph API object
result = graph.get_object('/me/friends')
print(result)
recipient_id = 'kirdemirekrem'
params = {
    'access_token': access_token,
    'recipient': '{"users": ["<kirdemirekrem>"]}',
    'message': 'Hello, friend!'
}
data = {'text': 'message'}

# Send the direct message
url = f'https://graph.instagram.com/{recipient_id}/messages?access_token={access_token}'
response = requests.post(url, data=data)
# Send the direct message
# response = requests.post(url, params=params)

# Check the response status code
if response.status_code == 200:
    print('Direct message sent successfully!')
else:
    print('Failed to send direct message')
# user_id = 'ekrem.kirdemir'

# Send a message to the user
# message = 'Hello, this is a test message!'
# graph.put_object(parent_object=user_id, connection_name='feed', message=message)
# session_cookies = {
#     'c_user': '<chatbotinteg>',
#     'xs': access_token,
# }
# client = Client(session_cookies=session_cookies)
# client = Client('<kirdemir.ekrem@gmail.com>', '<EAAvlbQDWvOkBAIBXa7sYzerVLhn5veJctAXowlHajGWXm0aZCTYx2ZAs6HlEr1drwWLpPAVCfZAwTtTfjRy4od0XLkRayABA8ZBk1KOPfiiBCZAgcz60WzvdMLY1wAU8ZCepbZBYzzh9WZAsULcMPEdexOOmPOjVo8DwfrGAkS5Vt4tZAgDZC4KL6JAZB3PrRKZBDFLgVbcZBwA0Rl6a2KEFXrXFz>')

# Send a message to a user
# client.send(Message(text='Hello, world!'),
#             thread_id='<ekrem.kirdemir>', thread_type=ThreadType.USER)
# app id:3348481072086249   app secret:c6dcb1bb2a2f0bfdb2a054a0c09769bc
# Send a message to a group chat
# client.send(Message(text='Hello, group!'), thread_id='<group_id>', thread_type=ThreadType.GROUP)

# Fetch messages from a thread
# messages = client.fetchThreadMessages(thread_id='<thread_id>', limit=10)
# for message in messages:
#     print(message.text)

# Disconnect the client
# client.logout()
