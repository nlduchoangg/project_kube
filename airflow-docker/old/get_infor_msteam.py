from urllib.parse import urlparse, parse_qs

# URL mẫu
url = 'https://teams.live.com/_?tenantId=9188040d-6c67-4c5b-b112-36a304b66dad#/conversations/19:HUqYKjeDi6lQOqb0TALK644xKEuwNLzXU5SL2ANnQ0M1@thread.v2?ctx=chat'

# Phân tích cú pháp URL
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)
fragment = parsed_url.fragment

# Lấy tenantId từ query params
tenant_id = query_params.get('tenantId', [None])[0]

# Lấy group_chat_id từ fragment
group_chat_id = None
channel_id = None

if fragment.startswith('/conversations/'):
    parts = fragment.split('/')
    if len(parts) > 2:
        group_chat_id_part = parts[2]
        if '@thread.v2' in group_chat_id_part:
            group_chat_id = group_chat_id_part.split('@thread.v2')[0]
            channel_id = group_chat_id_part  # Sử dụng group_chat_id làm channel_id

print(f'Tenant ID: {tenant_id}')
print(f'Group Chat ID: {group_chat_id}')
print(f'Channel ID: {channel_id}')
