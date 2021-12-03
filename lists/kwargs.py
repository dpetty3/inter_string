# def shop(**products):
#   print(products)

# shop()
# shop(clothes = 'shirts', jewelery ='necklace')

def shop(**products):
  if products:
    print(f"Are you looking for {products['clothes']} or a {products['jewelery']}?")
  else: 
    print("Continue Shopping")

shop()
shop(clothes = 'shirts', jewelery ='necklace')