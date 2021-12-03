teams = [
  {
    'baddies': {
      'IG': 'Jayda',
      'Snap': 'Ari',
      'Twitter': 'Chyna'
    }
  },
  {
    'haters': {
      'blog1': 'shaderoom',
      'blog2': 'hollywoodunlocked',
    }
  }
]

haters = teams[1].get('haters','Team not found')

print(list(haters.values())[1])