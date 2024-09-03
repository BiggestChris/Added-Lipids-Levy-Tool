from functions_GPT import comprehend_data

new_recipe = input("Please insert recipe here: ")

answer = comprehend_data(new_recipe)

print(answer)