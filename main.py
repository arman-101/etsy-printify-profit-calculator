# Testing
# --- Imports --- #

from tkinter import *

# --- Window --- #

window = Tk()
window.title("Etsy Printify - Profit and Costs Calculator")
window.minsize(width=650, height=325)
window.config(background="#247881")

# --- Calculate Function --- #


def calculate():
    # Rounded / Floated values from outer scope
    price = float(selling_price_entry.get())
    cost = float(cost_to_make_entry.get())
    shipping = float(shipping_cost_entry.get())
    coupon = float(with_coupon_entry.get()) / 100
    additional = float(additional_entry.get())

    # VAT + Tax
    printify_making_vat = cost * 0.2
    printify_shipping_tax = shipping * 0.2
    etsy_selling_vat = 1

    # Etsy Listing
    listing_fees = 0.2
    transaction_fees = price * 0.05
    processing_fees = (price * 0.04) + 0.25
    operating_fees = price * 0.0025
    total_etsy_fees = round(listing_fees + transaction_fees + processing_fees + operating_fees, 2)

    # Changing Labels for calculation
    total_costs = round(cost + total_etsy_fees + etsy_selling_vat + printify_making_vat + shipping + printify_shipping_tax + additional, 2)

    profit = round(price - total_costs, 2)

    profit_label.config(text=f"Profit = ${profit}")

    profit_with_coupon = round(profit - (price * coupon), 2)
    profit_with_coupon_label.config(text=f"Profit  with coupon = ${profit_with_coupon}")

    to_make_label.config(text=f"To Make = ${cost}")
    shipping_label.config(text=f"Shipping = ${shipping}")
    etsy_fees_label.config(text=f"Etsy Fees = ${total_etsy_fees}")
    etsy_vat_label.config(text=f"Etsy VAT = ${etsy_selling_vat}")
    printify_vat_tax_label.config(text=f"Printify VAT + Shipping Tax = ${round(printify_making_vat + printify_shipping_tax, 2)}")
    additional_label.config(text=f"Additional = ${additional}")

    total_cost_label.config(text=f"Total Cost = ${total_costs}")


# --- Labels + Entries + Button --- #

selling_price_label = Label(background="#247881", text="Selling Price: $", font=("Arial", 15, "normal"))
selling_price_label.grid(row=0, column=0, padx=20, pady=(15, 0))

selling_price_entry = Entry(width=15)
selling_price_entry.grid(row=0, column=1, padx=20, pady=(15, 0))

cost_to_make_label = Label(background="#247881", text="Cost to Make: $", font=("Arial", 15, "normal"))
cost_to_make_label.grid(row=1, column=0, padx=20, pady=(15, 0))

cost_to_make_entry = Entry(width=15)
cost_to_make_entry.grid(row=1, column=1, padx=20, pady=(15, 0))

shipping_cost_label = Label(background="#247881", text="Shipping Cost: $", font=("Arial", 15, "normal"))
shipping_cost_label.grid(row=2, column=0, padx=20, pady=(15, 0))

shipping_cost_entry = Entry(width=15)
shipping_cost_entry.grid(row=2, column=1, padx=20, pady=(15, 0))

with_coupon_label = Label(background="#247881", text="Coupon: %", font=("Arial", 15, "normal"))
with_coupon_label.grid(row=3, column=0, padx=20, pady=(15, 0))

with_coupon_entry = Entry(width=15)
with_coupon_entry.grid(row=3, column=1, padx=20, pady=(15, 0))

additional_label = Label(background="#247881", text="Additional: $", font=("Arial", 15, "normal"))
additional_label.grid(row=4, column=0, padx=20, pady=(15, 0))

additional_entry = Entry(width=15)
additional_entry.grid(row=4, column=1, padx=20, pady=(15, 0))

calculate_btn = Button(highlightbackground="#247881", fg="#203239", text="Calculate Total Cost and Profit", command=calculate, font=("Arial", 20, "bold"))
calculate_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=(15, 20))

to_make_label = Label(background="#247881", text="To Make = $", font=("Arial", 15, "normal"))
to_make_label.grid(row=0, column=2, padx=20, pady=(15, 0))

shipping_label = Label(background="#247881", text="Shipping = $", font=("Arial", 15, "normal"))
shipping_label.grid(row=1, column=2, padx=20, pady=(15, 0))

etsy_fees_label = Label(background="#247881", text="Etsy Fees = $", font=("Arial", 15, "normal"))
etsy_fees_label.grid(row=2, column=2, padx=20, pady=(15, 0))

etsy_vat_label = Label(background="#247881", text="Etsy VAT = $", font=("Arial", 15, "normal"))
etsy_vat_label.grid(row=3, column=2, padx=20, pady=(15, 0))

printify_vat_tax_label = Label(background="#247881", text="Printify VAT + Shipping Tax = $", font=("Arial", 15, "normal"))
printify_vat_tax_label.grid(row=4, column=2, padx=20, pady=(15, 0))

additional_label = Label(background="#247881", text="Additional = $", font=("Arial", 15, "normal"))
additional_label.grid(row=5, column=2, padx=20, pady=(15, 20))

dashed_line_label = Label(background="#247881", text="---------------------------------------------------------------------------------------------------------------------", font=("Arial", 15, "normal"))
dashed_line_label.grid(row=6, column=0, columnspan=3, pady=0)

total_cost_label = Label(background="#247881", fg="#F7F7F7", text="Total Cost = $", font=("Arial", 20, "bold"))
total_cost_label.grid(row=7, column=0, padx=20, pady=(15, 20))

profit_label = Label(background="#247881", fg="#F7F7F7", text="Profit = $", font=("Arial", 20, "bold"))
profit_label.grid(row=7, column=1, padx=20, pady=(15, 20))

profit_with_coupon_label = Label(background="#247881", fg="#F7F7F7", text="Profit with Coupon = $", font=("Arial", 20, "bold"))
profit_with_coupon_label.grid(row=7, column=2, padx=20, pady=(15, 20))

# --- End --- #

window.mainloop()
