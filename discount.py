def calculate_discount(price, discount_percent):
    """
    Calculate the final price after discount if it is 20% or higher.
    Args:
    price (float): the original price of the item.
    discount_percent (float): the discount percentage to be applied.
    Returns:
    float: the final price after applying the discount or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price or the original price if no discount was applied
if final_price != original_price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount was applied. The final price is: {original_price:.2f}")

