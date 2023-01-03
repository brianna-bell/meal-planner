# from calendar import c
from enum import Enum
# from operator import contains
# from unicodedata import category
import os
import random
import re

# class Difficulty(Enum):
#     EASY = 1
#     MEDIUM = 2
#     HARD = 3

    
allRecipes = []



# globalIngredients = [] # should be as many of these as there are dishes
# currentIngredients = [] # to be cleared out


class Recipe:

    dish = ''
    ingredients = []
    # difficulty = ''
    # category = ''

    def __init__(self, dish, ingredients):
        self.dish = dish
        self.ingredients = ingredients
        # self.difficulty = difficulty
        # self.category = category


def populateRecipes():
    print('Populating recipes...')

    currentDir = os.getcwd()

    # Print the current working directory1
    print("Current working directory: {0}".format(currentDir))

    if(os.path.exists(currentDir+'\Export\\')): # check that recipe directory exists
        os.chdir('Export')
    else:
        print("Error, recipe folder not found")
        return

    recipeDir = os.getcwd()

    # Print the current working directory1
    # print("Current working directory: {0}".format(cwd2))

    # RecipesList = os.listdir()

    # list = []

    # dirs=directories
    for (root, dirs, file) in os.walk(recipeDir):
        for f in file:
            if '.md' in f:
                g = open(f, 'r')
                text = g.readlines()
                last = text[-1]
                for j in (text):
                    ingredients = [] # list of ingredients for current recipe
                    
                    if(j[0] == "#"):
                        #print(j) # this is the name of the recipe
                        currentDishName = re.sub(r"# ", "", j).strip() # strip the markdown and assign it to the name
                    
                    elif(j[0] == "-"):
                        j = re.sub(r"- ","",j).strip()
                        print("Adding Ingredient " + j )
                        ingredients.append(j)

                    elif (j is last):
                        print("Adding "+ currentDishName + " to recipe list")
                        currentRecipe = Recipe(currentDishName,ingredients)
                        allRecipes.append(currentRecipe)

                        
                    
    print("There are " + str(len(allRecipes)) + " recipes recorded")


#currentRecipe = Recipe(dishName, ingredients, difficulty, category)
 #           allRecipes.append(currentRecipe)


    #for recipe in RecipesList:
    #    o = open(RecipesList)
        

    #f = open("Recipes.txt","a+") # todo later: make a new one
#     dishName = input('Enter the dish\'s name: ')
#     while dishName != 'x':
#         f.write('Dish Name: ' + dishName + '\n')

#         ingred = []

#         currentIng = input('What is the next ingredient? Type x to break\n')
#         while currentIng != 'x':
#             ingred.append(currentIng)
#             currentIng = input('What is the next ingredient? Type x to break\n')

#         f.write('Ingredients: ')

#         for item in ingred:
#             f.write(item + ', ')

#         f.write('\n')

#         Diff = input('On a scale of 1 to 3, how difficult is this dish? ')

#         if int(Diff) == 1:
#             f.write('Difficulty: EASY\n')
#             print('Easy chosen')
#         elif int(Diff) == 2:
#             f.write('Difficulty: MEDIUM\n')
#             print('Medium chosen')
#         elif int(Diff) == 3:
#             f.write('Difficulty: HARD\n')
#             print('Hard chosen')
        
#         category = input('What is the category of this dish? ')
#         f.write('Category: ' + category + '\n')

#         dishName = input('(Type x to break) Enter the dish\'s name: ')

#    # f.write('END')
#     f.close()

def mealPlan():

    dishName = ''
    ingredients = []
    difficulty = ''
    category = ''

    #populate database
    f = open("Recipes.txt")
    for line in f:
        if line.startswith('Dish Name: '):
            dishName = line.strip('Dish Name: ').rstrip()
        elif line.startswith('Ingredients: '):
            ingredientString = line.strip('Ingredients: ').rstrip()
            ingredients = ingredientString.split(', ')
            ingredients[-1] = ingredients[-1].rstrip(',')
        elif line.startswith('Difficulty: '):
            difficulty = line.strip('Difficulty: ').rstrip()
        elif line.startswith('Category: '):
            category = line.strip('Category: ').rstrip()
            #print('Recipe added: ' + dishName)
            #print('\tIngredients: ' + ingredients[0])
            #print('\tDifficulty: ' + difficulty)
            #print('\tCategory: ' + category)
            currentRecipe = Recipe(dishName, ingredients, difficulty, category)
            allRecipes.append(currentRecipe)
    f.close()  

    topLimit = len(allRecipes)-1 

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

    again = input('Sound good? Y or N\n')
    while again == 'n':
        firstMeal = random.randint(0, topLimit)
    
        secondMeal = random.randint(0, topLimit)
        while (secondMeal == firstMeal):
            secondMeal = random.randint(0, topLimit)    # Generate the computer's choice


        thirdMeal = random.randint(0, topLimit)
        while (thirdMeal == secondMeal or thirdMeal == firstMeal):
            thirdMeal = random.randint(0, topLimit)    # Generate the computer's choice

        chosenRecipes.clear()

        chosenRecipes.append(allRecipes[firstMeal])
        chosenRecipes.append(allRecipes[secondMeal])
        chosenRecipes.append(allRecipes[thirdMeal])

        print('\n\n\n')
        print('Meal Plan: \n\t' + allRecipes[firstMeal].dish + '\n\t' + allRecipes[secondMeal].dish + '\n\t' + allRecipes[thirdMeal].dish)
        print('\n\n\n')

        again = input('Sound good? Y or N\n')

    print('Grocery list:\n')

    for recipe in chosenRecipes:
        for item in recipe.ingredients:
            print(item)

    #todo - make a grocery list

    allRecipes.clear()

            

#times = 3
#selection = input("What would you like to do? \n\t1 for adding new recipe\n\t2 for meal planning for the week\n\tx to quit\n\t")
#while selection != 'x':

    #if selection == '1':
    #    print('hooray!')
populateRecipes()
    #elif selection == '2':
    #    mealPlan()
        
   # selection = input("What would you like to do? \n\t1 for adding new recipe\n\t2 for meal planning for the week\n\tx to quit\n\t")








































#import csv


##dishes=[]
##recipes=[]
##fields = []
##rows = []
##with open('MainDishes.csv', newline='') as f:
##    reader = csv.reader(f, delimiter='\n')
##    for row in reader:
##        #print('.'.join(row))
##        print(row)
##        print("##################") 
####        oneRecipe = '.'.join(row)
##
##        print(oneRecipe)
##
##        for line in oneRecipe:
##            print('one line')
##        
##        print("##################") 



        
    #csvreader = csv.reader(f)
    
    # extracting field names through first row
    #fields = next(csvreader)
    #print("##################") 
    # extracting each data row one by one
##    for recipe in csvreader:
##        #print(recipe)
##        recipes.append(recipe)
        #i.split('\n',1)[0] for i in recipe
        #for i in recipe:
         #   dishes.append(i.split('\t')[0])


       # print(dishes)
       # print("##################")           
        
        #print(row) # each row is a recipe

        #numRecipes = len(row)
        #print(numRecipes)
        #if(row.startswith('"')):
        #    dishes.append(row)

        #rows.append(row[0])
 
    # get total number of rows
    #print("Total no. of rows: %d"%(csvreader.line_num))

##print(recipes)
##print("Number of recipes: " + str(len(recipes)))
##
##print("##################")         
##for rec in recipes:
##    other = rec.split('\n')
##    print(other)
##    print("##################")         

