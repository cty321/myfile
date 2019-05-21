#!/usr/bin/env python

def get_omelet_ingredients(omelet_name):
    """This contains a dictionary of omelet names that can be produced, and their
    ingredients"""
    # All of our omelets need eggs and milk
    ingredients = {"eggs":2,"mikl":1}
    if omelet_name == "cheese":
        ingredients["cheddar"] = 2
    elif omelet_name == "western":
        ingredients["jack_cheese"] = 2
        ingredients["ham"] = 1
        ingredients["pepper"] = 1
        ingredients["onion"] = 1
    elif omelet_name == "greek":
        ingredients["feta_cheese"] = 2
        ingredients["spinach"] = 2
    else:
        print("That's not on the menu,sorry")
        return None
    return ingredients
