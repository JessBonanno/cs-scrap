"""
practice
"""

"""
Grouping Dishes
---------------
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. 
You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

Example

For
  dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]
For
  dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]
the output should be
  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Chicken", "Chicken Curry", "Quesadilla"],
                            ["Nuts", "Fried Rice", "Salad"],
                            ["Onions", "Fried Rice", "Pasta"]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.string dishes

An array of dishes, where dishes[i] for each valid i contains information about the ith dish: dishes[i][0] is the name of the dish, and all the elements after it are the ingredients of that dish. Both the dish name and the ingredient names consist of English letters and spaces. It is guaranteed that all dish names are different. It is also guaranteed that the ingredient names for any one dish are also pairwise distinct.

Guaranteed constraints:
1 ≤ dishes.length ≤ 500,
2 ≤ dishes[i].length ≤ 10,
1 ≤ dishes[i][j].length ≤ 50.

[output] array.array.string

The array containing the grouped dishes.
"""

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]


def groupingDishes(dishes):
    # create a dictionary to hold the ingredients as keys and then dishes that use them as the values
    ingredient_dishes = {}
    # populate the dictionary with the dishes
    for dish in dishes:
        for i in range(1, len(dish)):
            if dish[i] not in ingredient_dishes:
                ingredient_dishes[dish[i]] = []
            # add the dish ( 0th element of current array) to the ingredient
            # (i th element of current array) key array in the dictionary
            ingredient_dishes[dish[i]].append(dish[0])

    # new dict to hold ingredients with more than 2 dishes
    ing_in_more_than_2_dishes = {}

    # remove ingredients from dictionary if they only are used in 1 dish
    for key, value in ingredient_dishes.items():
        if len(value) >= 2:
            ing_in_more_than_2_dishes[key] = sorted(value)

    # sort the keys of the dictionary and create a matrix
    result = []
    for key in ing_in_more_than_2_dishes:
        result.append([])

    # get the ingredients in alphabetical order and append it one at a time
    # to each array in the result matrix
    sorted_ings = sorted(ing_in_more_than_2_dishes.keys())
    for i in range(len(sorted_ings)):
        result[i].append(sorted_ings[i])

    # append dishes from dict to result matrix for corresponding ingredient
    for i in range(len(result)):
        if result[i][0] in ing_in_more_than_2_dishes:
            result[i].extend(ing_in_more_than_2_dishes[result[i][0]])

    return result


print(groupingDishes(dishes))
