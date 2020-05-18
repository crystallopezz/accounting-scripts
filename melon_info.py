"""Print out all the melons in our inventory."""


from melons import melons


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

def print_melon(melons):
    for melon in melons:
        print(melon)
        for attribute in melons[melon]:
            print(f"{attribute}:{melons[melon][attribute]}")