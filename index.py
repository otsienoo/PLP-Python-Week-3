def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it is 20% or higher.
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount if the discount is 20% or higher, otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function and print the result
    final_price = calculate_discount(original_price, discount_percent)

    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
