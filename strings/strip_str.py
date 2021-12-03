url = 'https://google.com'

# print(url.strip('https://'))

# Google 
# print(url.lstrip('https://'))
# print(url.rstrip('.com'))

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)
