import matplotlib.pyplot as plt
products=["Apple","mango","cherry"]
prices=[30000,9000,8000]
plt.bar(products,prices)
plt.title("Product Price")
plt.xlabel("product")
plt.ylabel("price (PKR)")
plt.show()   