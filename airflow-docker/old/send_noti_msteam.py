import requests
import json

# Thay thế bằng access token của bạn
access_token = 'EwBwA8l6BAAUbDba3x2OMJElkF7gJ4z/VbCPEz0AAdJkEuY2oCpgIGrkGbArORwUvbYSqPkkXrpiEzYZxXZ7mDTOhbJZrSpktyHGn8Dkr3wfA6Q9j4b6EW8TYiayjbtpzIwFBDX7yxYuux88MBGnwbHLM3s09qyDVpWX05zeFZIGB2vRruLuO0J5KjidWPYpJDhGOcuJZHkX73W6brxQfWsOSIK5w/PJqH3ccH5OTr6u+AHnrGKGSpbzHO8594iJ7HiAktN6CoUwxaLlfKmiyy3VoLpmqrHBKOCoe7xJXscGxXvrlEvFHagd1OZk5D6BaKKlxrt9+XvItW5oUSBlSXOipP2O9Xd4h6OOH+9dkUnUWQrpV/HILA7vIRFvk0cDZgAACPW9pnP3fYgRQAJGH3CegU7d3YGiT28BNyr2846byBY9IueBjdsPWCGTwOZj/LI7qpL1/VmHWWjdvx8zmuE5RUgLbnnu8sSbXuZkCnbKR9s2NxBoqF1ss8HVuJsICpip9mi6sPIHtsLBGkj56WDfl/GVrtP61gZsjd9NAGrWgBt9dKKVzyHzkwpz904zEukKsdYzSktfkT6Ipsd9+42Cj7VJfw6RtF+0vK/U5lPEMLGYpnr8nd5MpGS8JBthmb9ytYgdWKMfOeWFOFyEBIX9llyTAjTjYBV49eN42w6ByboEpzZKsEVKIMfYGJksT5j92a63D017a4J3rsWHTCmKg/hbv25cNkYHXomZKr6KB7INLGs2M7WEs74eCe7t5C324qYC25Ynxwh54W9tbbyol1cyYLnEW/lDdsG7F+20+Bc8mb4HFUENZXr3PR30q5rB5hf3va81LvhZvyNpvcqONZWHVSkMtGkzkKw60U4p2i3NspZQhPGJM3Z27TjvZfFbEW4fO1HyuOnsHCb3ZEUSAxY46ixGbvCds6vsBq5ZQva7GF8InIl/6W0qJdKtbogvH67TGuPt39yNZUlDDgjXROFNh8bY9vF9KbYmkRHEruYVE5eaOP83mV8BVMWnRCiFewVF9glqyXMgwFUvVROYtiOSXVV24iJac0xmgJDELm99cKMyEX0edIPXh4z0pGo5BBUXeRAv4KMbWv3/0LyJ5CaCFZSnMZ+f59pJC+Ml8ShN1K4FTaw0LDFJf1yAtDr+KlHmjKbTUYK5/aiDAg=='
# Thay thế bằng ID của group chat trong Microsoft Teams
group_chat_id = '19:HUqYKjeDi6lQOqb0TALK644xKEuwNLzXU5SL2ANnQ0M1'
channel_id = '19:HUqYKjeDi6lQOqb0TALK644xKEuwNLzXU5SL2ANnQ0M1@thread.v2?ctx=chat'

# URL endpoint để gửi tin nhắn vào group chat
url = f'https://graph.microsoft.com/v1.0/teams/{group_chat_id}/channels/{channel_id}/messages/archive'

# Nội dung tin nhắn
message_body = {
    "body": {
        "contentType": "text",
        "content": "Hello from Python!"
    }
}

# Headers để gửi request
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# Gửi POST request để gửi tin nhắn
response = requests.post(url, headers=headers, json=message_body)

# Kiểm tra kết quả của request
if response.status_code == 201:
    print('Tin nhắn đã được gửi thành công!')
else:
    print(f'Có lỗi xảy ra: {response.status_code} - {response.text}')


