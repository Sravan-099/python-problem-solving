"""Write a Python program that uses arithmetic operators to calculate subtotal, discount, tax, and final bill."""
def calculate_bill(subtotal, discount_rate, tax_rate):
    # Calculate discount amount
    discount_amount = subtotal * (discount_rate / 100)
    
    # Calculate subtotal after discount
    subtotal_after_discount = subtotal - discount_amount
    
    # Calculate tax amount
    tax_amount = subtotal_after_discount * (tax_rate / 100)
    
    # Calculate final bill
    final_bill = subtotal_after_discount + tax_amount
    
    return {
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "subtotal_after_discount": subtotal_after_discount,
        "tax_amount": tax_amount,
        "final_bill": final_bill
    }