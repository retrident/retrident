# Define the restaurant choices and their dietary options
restaurants = {
   "Joe's Gourmet Burgers": {"Vegetarian": False, "Vegan": False, "Gluten-Free": False},
   "Main Street Pizza Company": {"Vegetarian": True, "Vegan": False, "Gluten-Free": True},
   "Corner Cafe": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True},
   "Mama's Fine Italian": {"Vegetarian": True, "Vegan": False, "Gluten-Free": False},
   "The Chef's Kitchen": {"Vegetarian": True, "Vegan": True, "Gluten-Free": True}
}

# Function to filter and display restaurant choices based on dietary preferences
def find_restaurants():
   vegetarian = input("Is anyone in your party a vegetarian? ").strip().lower()
   vegan = input("Is anyone in your party a vegan? ").strip().lower()
   gluten_free = input("Is anyone in your party gluten-free? ").strip().lower()
   valid_choices = []
   for restaurant, options in restaurants.items():
       if (vegetarian == "yes" and options["Vegetarian"]) or \
          (vegan == "yes" and options["Vegan"]) or \
          (gluten_free == "yes" and options["Gluten-Free"]):
           valid_choices.append(restaurant)
   return valid_choices

# Main program
if __name__ == "__main__":
   print("Restaurant Options:")
   valid_restaurants = find_restaurants()
   if valid_restaurants:
       print("You can take your group to the following restaurants:")
       for restaurant in valid_restaurants:
           print(restaurant)
   else:
       print("Unfortunate")
