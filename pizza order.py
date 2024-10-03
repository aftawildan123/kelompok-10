print("""
====================selamat datang di MI pizza=====================
silahkan pilih menu anda
1. size pizza (kecil, sedang, dan besar)
2. topping pizza (pepperoni, frankfurter, chicken supreme)
3. crust pizza (pan crust, cheesy bite crust, chili cheesy stuffed)
====================================================================""")

size_pizza = input("pilih size pizza yang anda inginkan ?")
topping_pizza = input("pilih topping pizza yang anda inginkan ?")
crust_pizza = input("pilih crust pizza yang anda inginkan ?")
extra_cheese = input("apakah anda ingin menambahkan extra keju pada pizza anda ? (yes/no)")
bill = 0

if size_pizza == "kecil":
    bill += 75000
elif size_pizza == "sedang":
    bill += 100000
elif size_pizza == "besar":
    bill += 150000
else:
    print("")

if topping_pizza == "pepperoni":
    bill += 20000
elif topping_pizza == "frankfurter":
    bill += 25000
elif topping_pizza == "chicken supreme":
    bill += 30000
else:
    print("anda tidak memilih topping")

if crust_pizza == "pan crust":
    bill += 10000
elif crust_pizza == "cheesy bite crust":
    bill += 20000
elif crust_pizza == "chili cheesy stuffed":
    bill += 20000
else:
    print("topping tidak tersedia")

if extra_cheese == "yes":
    bill += 5000
else:
    print()


print(
f"""terima kasih telah pesan di MI pizza
total pesanan anda : {bill}""")
