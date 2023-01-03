from enum import Enum
import os
import random
import re
    
allRecipes = []

class Recipe:

    dish = ''
    ingredients = []

    def __init__(self, dish, ingredients):
        self.dish = dish
        self.ingredients = ingredients

def populateRecipes():
    print('Populating recipes...')

    currentDir = os.getcwd()

    # Print the current working directory1
    #print("Current working directory: {0}".format(currentDir))

    if(os.path.exists(currentDir+'\Export\\')): # check that recipe directory exists
        os.chdir('Export')
    else:
        print("Error, recipe folder not found")
        return

    recipeDir = os.getcwd()

    r = open("Recipes.txt","w+") 

    for (root, dirs, file) in os.walk(recipeDir):
        for f in file:
            if '.md' in f:
                g = open(f, 'r')
                text = g.readlines()
                last = text[-1]
                ingredients = [] # list of ingredients for current recipe
                for j in (text):

                    if(j[0] == "#"):
                        #print(j) # this is the name of the recipe
                        currentDishName = re.sub(r"# ", "", j).strip() # strip the markdown and assign it to the name
                    
                    elif(j[0] == "-"):
                        j = re.sub(r"- ","",j).strip()
                        #print("Adding Ingredient " + j )
                        ingredients.append(j)

                    elif (j is last):
                        #print("Adding "+ currentDishName + " to recipe list")
                        r.write(currentDishName + "\n")
                        currentRecipe = Recipe(currentDishName,ingredients)
                        allRecipes.append(currentRecipe)
    print("There are " + str(len(allRecipes)) + " recipes recorded")
    r.close()

def chooseMeals():
    topLimit = len(allRecipes)-1 

    for recipe in allRecipes:
        firstMeal = random.randint(0, topLimit)
        secondMeal = random.randint(0, topLimit)
        while (secondMeal == firstMeal):
            secondMeal = random.randint(0, topLimit)    # Generate the computer's choice
        thirdMeal = random.randint(0, topLimit)
        while (thirdMeal == secondMeal or thirdMeal == firstMeal):
            thirdMeal = random.randint(0, topLimit)    # Generate the computer's choice

    chosenRecipes = []

    chosenRecipes.append(allRecipes[firstMeal])
    chosenRecipes.append(allRecipes[secondMeal])
    chosenRecipes.append(allRecipes[thirdMeal])

    print('\n\n\n')
    print('Meal Plan: \n\t' + allRecipes[firstMeal].dish + '\n\t' + allRecipes[secondMeal].dish + '\n\t' + allRecipes[thirdMeal].dish)
    print('\n\n\n')

    return [firstMeal, secondMeal, thirdMeal] # 3 numbers

def mealPlan():

    dishName = ''
    ingredients = []

    recipeNums = chooseMeals()

    again = input('Sound good? Y or N\n')
    while again == 'n':
        recipeNums = chooseMeals()
        again = input('Sound good? Y or N\n')

    f = open("GroceryList.txt",'w+')

    print('Grocery list:\n')
    f.write('Grocery list:\n')

    FirstMeal = allRecipes[recipeNums[0]]
    for item in FirstMeal.ingredients:
        print(item)
        f.write("- [ ]  "+ item + "\n")
    SecondMeal = allRecipes[recipeNums[1]]
    for item in SecondMeal.ingredients:
        print(item)
        f.write("- [ ]  "+ item + "\n")
    ThirdMeal = allRecipes[recipeNums[2]]
    for item in ThirdMeal.ingredients:
        print(item)
        f.write("- [ ]  "+ item + "\n")

    
           

populateRecipes()
mealPlan()