def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
        elif unit == "meters to feet":
            return value * 3.28084
        elif unit == "feet to meters":
            return value / 3.28084
            
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
        elif unit == "grams to ounces":
            return value * 0.035274
        elif unit == "ounces to grams":
            return value / 0.035274
            
    elif category == "Time":
        if unit == "hours to minutes":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
            
    return None  # Return None if no valid conversion is found