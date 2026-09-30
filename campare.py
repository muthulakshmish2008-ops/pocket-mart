# Price compare logic di
products = {
  "iPhone 14": {"amazon": 62000, "flipkart": 59999, "ikea": 0},
  "Redmi Note 13": {"amazon": 18000, "flipkart": 16999, "ikea": 0},
  "IKEA Chair": {"amazon": 4000, "flipkart": 3800, "ikea": 2999}
}

item = input("Enna product venum di? ")
if item in products:
  p = products[item]
  best = min(p, key=p.get)
  print(f"{item} ku best price {best} la di: Rs {p[best]}")
else:
  print("Idhu list la illa di, Amazon la search pannu!")