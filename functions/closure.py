def outer():
    def inner():
        print("Hello from inner function")

    inner()

outer()

def discount_10():
    def apply_discount(price):
        return price * 0.9  # Apply a 10% discount

    return apply_discount

def discount_20():
    def apply_discount(price):
        return price * 0.8  # Apply a 20% discount

    return apply_discount


# Outer function
def create_discount(discount):

    # Inner function
    def calculate(price):

        # Calculate the discounted price based on the outer function's discount value
        return price - (price * discount / 100)

    # Return the inner function
    return calculate

# Create a 10% discount function
discount_10 = create_discount(10) #default discount 10%         

print(discount_10(1000))  # Output: 900.0

# Create a 20% discount function
discount_20 = create_discount(20) # 

# ₹1000 ki 10% discount
print(discount_10(1000))
# Output: 900.0

# ₹1000 ki 20% discount
print(discount_20(1000))
# Output: 800.0