#Bill Generation

#Initializing GST for Apple and Orange

apple_gst=0.12
orange_gst=0.05

"""
Taking Buyer Name,apple and orange price in kg 
and how much quantity they purchased in kg
"""
buyer_name=input("Enter buyer name: ")
apple_price_kg=int(input("Enter apple price per kg: "))
apple_quantity_kg=float(input("Enter apple quantity purchased: "))
orange_price_kg=int(input("Enter orange price per kg: "))
orange_quantity_kg=float(input("Enter orange quantity purchased: "))

#calculate  price for the bought items

total_apple_price=apple_price_kg*apple_quantity_kg
total_orange_price=orange_price_kg*orange_quantity_kg

#calculating gst for bought items

total_gst_apple=apple_gst*total_apple_price
total_gst_orange=orange_gst*total_orange_price

#calculate billing price 

total_billing_apple=total_apple_price+total_gst_apple
total_billing_orange=total_orange_price+total_gst_orange

#calculate total amount
total_amount=total_billing_orange+total_billing_apple
total_round_amount=round(total_amount)

#Printing format

print(f"Buyer Name : {buyer_name}")
print(f"{'-'*74}")
print(f"| {'Item Code':^10} | {'Price/Unit':^10} | {'unit':^5} | {'price':^5}  | {'GST':^10} | {'Total':^10} |")
print(f"{'-'*74}")
print(f"{'Apple':^10} | {'Rs'+str(apple_price_kg):^10} | {apple_quantity_kg:^5} | {'Rs'+str(total_apple_price)} | {'Rs'+str(total_gst_apple):^10} | {'Rs'+str(total_billing_apple):^10} |")
print(f"{'Orange':^10} | {'Rs'+str(orange_price_kg):^10} | {orange_quantity_kg:^5} | {'Rs'+str(total_orange_price)} | {'Rs'+str(total_gst_orange):^10} | {'Rs'+str(total_billing_orange):^10} |")
print(f"{'-'*74}")
print(f"Total {' '*50} \u20b9 {total_amount:.2f}")
print(f"Total Rounded {' '*43} \u20b9 {total_round_amount:.2f}")
print(f"{'-'*74}")