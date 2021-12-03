# title = 1
# heading_type = "Hi There"

# heading_generator = "<h{0}> {1} </h{0}>". format(title,heading_type)

# print(heading_generator)

def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('YO', '2'))