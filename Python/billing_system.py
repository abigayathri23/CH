def calculate_total(items):
    """
    items: list of (price, quantity)
    """
    total = 0.0
    for price, qty in items:
        if price < 0 or qty < 0:
            raise ValueError("Invalid input: price or quantity cannot be negative")
        total += price * qty

    # Ensure total is never negative
    if total < 0:
        total = 0.0

    return round(total, 2)


# Example usage
items = [(100, 2), (50, 1), (-20, 3)]  # buggy input
try:
    print("Total:", calculate_total(items))
except ValueError as e:
    print("Error:", e)
