from calc import apply_vat
import sys

price = sys.argv[1]
percent= sys.argv[2]

try:
    price=float(price)
    percent= float(percent)
except ValueError:
    print("erreur ! le prix et la tva doivent etre un foat entre d'index")


print (apply_vat(price, percent))