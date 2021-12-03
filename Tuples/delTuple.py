post = ( 'Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

#removing elements from end
# post = post[:-1]

# #removing from elements from beginning
# post = post[1:]

# removing element(messy/not recommended)
post = list(post)
post.remove('published')
post = tuple(post)

print(post)