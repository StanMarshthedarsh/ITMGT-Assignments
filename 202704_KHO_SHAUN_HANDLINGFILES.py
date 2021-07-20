products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code, property):
    return products[code][property]

def main():
    products_dict = dict()
    for i in products.keys():
        products_dict[i]=0
    total_price = 0
    while True:
        order = input("Input orders: ")
        if order == "/":
            break
        order_data = order.split(",")
        previous_order_value = products_dict[order_data[0]]
        products_dict[order_data[0]] = previous_order_value + int(order_data[1])
    for i in products.keys():
        total_price = total_price + products_dict[i] * get_property(i, "price")
    # RECEIPT
    receipt = open("receipt.txt", "w")
    receipt.write(f'''
    ==
    CODE\t\t\t  NAME\t\t\t   QUANTITY\t\t   SUBTOTAL
    ''')
    
    for i in products.keys():
        if products_dict[i] > 0:
            receipt.write(f"{i}        {get_property(i, 'name')}            {products_dict[i]}            {products_dict[i]*get_property(i, 'price')}")
            receipt.write("\n\t")
    receipt.write(f"\n\tTotal:\t\t\t\t\t\t\t\t\t\t\t{total_price}\n\t==") 
main()