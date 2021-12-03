usernames = ['Deanna', 'Deborah','Quinton', 'Cornell', 'Danielle', 'David', 'DeForrest']

blacklist = 'Quinton'

# for username in usernames:
#   if username == blacklist:
#     print(f' Sorry, {username}, you are not allowed')
#     continue
#   else:
#     print(f'{username} is allowed')

for username in usernames:
  if username == blacklist:
    print(f' Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')