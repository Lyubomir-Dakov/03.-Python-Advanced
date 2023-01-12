def shopping_list(budget, **kwargs):
    basket = []
    result = ''
    if budget < 100:
        return "You do not have enough budget."
    for product, data in kwargs.items():
        price, amount = data
        total_price = price * amount
        if total_price > budget:
            continue
        budget -= total_price
        result += f"You bought {product} for {total_price:.2f} leva.\n"
        if product not in basket:
            basket.append(product)
        if len(basket) == 5:
            break
    return result


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))




