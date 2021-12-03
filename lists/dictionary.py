designers = {
  "purses": ["Dooney", "Dior", "YSL"],
  "shoes": ["Jordans", "LVs"],
  "glasses": ["Gucci", "Prada"]
}

# featured_designer = designers['purses']

featured_designer = designers.get('shoes', 'No featured designer')

# print(featured_designer)
print(designers.items())