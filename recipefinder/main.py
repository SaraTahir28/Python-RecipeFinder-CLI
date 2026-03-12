import os

import requests
from dotenv import load_dotenv

load_dotenv()

def view_file_contents(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            file_contents = f.read()
            print(file_contents)
    else: print(f"{filename} does not exist or is empty.\n")

#save recipes to a file
def save_to_file(recipes, filename):
    with open(filename, 'w') as f:
        for recipe in recipes:
            f.write(f"Recipe: {recipe['recipe']['label']}\n")
            f.write(f"URL: {recipe['recipe']['uri']}\n")
            f.write("\n")  # Adding a newline for better readability

#mark a recipe as a favourite (repeats until 'done' is inputted to allow saving multiple recipes)
def mark_favorite(recipes):
    favorites = []
    for index, recipe in enumerate(recipes):
        print(f"{index + 1}. {recipe['recipe']['label']}")
    while True:
        choice = input("Enter the number of the recipe to mark as favorite (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(recipes):
                favorites.append(recipes[choice - 1])
            else:
                print("Invalid choice. Please try again.")
        else:
             print("Invalid input. Please enter a number or 'done'.")
    return favorites

#save a list of favourites, separate to recent results
def save_favorites(favorites, filename):
    with open(filename, 'a') as f:
        for recipe in favorites:
            f.write(f"Favorite Recipe: {recipe['recipe']['label']}\n")
            f.write(f"URL: {recipe['recipe']['uri']}\n")
            f.write("\n")

#clear recipes in files
def clear_file_contents():
    print("\nWhich file do you want to clear?")
    print("1. favorites.txt")
    print("2. recipes.txt")

    file = input("\nEnter 1 or 2: ")

    if file == "1":
        open('favorites.txt', 'w').close()
        print('Recipes have been erased from favorites.txt\n')
    elif file == "2":
        open('recipes.txt', 'w').close()
        print('Recipes have been erased from recipes.txt\n')
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        return

#recipe search using ingredient:

def recipe_search(ingredient, diet):
    app_id = os.getenv('APP_ID')
    app_key = os.getenv('APP_KEY')
    app_user = os.getenv('APP_USER')

    url = "https://api.edamam.com/api/recipes/v2"

    params = {
        "type": "public",   # MUST be included
        "q": ingredient,
        "app_id": app_id,
        "app_key": app_key,
        "diet": diet
    }

    headers = {
        "Edamam-Account-User": app_user,
        "Accept": "application/json"
    }

    result = requests.get(url, params=params, headers=headers)

    print("Status:", result.status_code)

    if result.status_code != 200:
        print("API Error:", result.text)
        return []

    data = result.json()
    return data.get("hits", [])




#user input and printing results from recipe search:
def run():
    #retrieves user input for ingredient and diet type to search using more customisable parameters.
    #.lower() method transforms input to avoid case-sensitivity of API searching.
    ingredient = input('Enter an ingredient:\n').lower()
    diet = input('Enter a Diet: (available options: balanced, high-fiber, high-protein, low_carb, low-fat, low-sodium)\n').lower()
    results = recipe_search(ingredient, diet)
    #printing of results
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

    #saving search results to file and printing
    save_to_file(results, 'recipes.txt')
    print("Results saved to recipes.txt")

    #saving to favourites and printing confirmation
    favorites = mark_favorite(results)
    if favorites:
        save_favorites(favorites, 'favorites.txt')
    print("Favorite recipes saved to favorites.txt")

#start menu with options to recipe search and view recent search results and favourites
def main():
    while True:
        print('\nWelcome to Recipe Finder')
        print('1. Search for a new recipe')
        print('2. View recent search results')
        print('3. View favorites')
        print('4. Clear saved recipes')
        print('5. Exit')

        selection = input('\nPlease select an option: ')

        #recipe search
        if selection == '1':
            run()

        #prints contents of text file containing recent search results
        elif selection == '2':
            view_file_contents('recipes.txt')


        #prints contents of text file containing favorite results
        elif selection == '3':
            view_file_contents('favorites.txt')

        #calls function to clear file contents
        elif selection == '4':
            clear_file_contents()

        #program exit
        elif selection == '5':
            print('You have exited the program.')
            break

        #guides user input
        else:
            print('\nPlease choose an option presented below.')

if __name__ == "__main__":
    main()