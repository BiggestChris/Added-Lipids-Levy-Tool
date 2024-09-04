# Script to host ChatGPT functions - taken from other Inversity projects

from openai import OpenAI
from dotenv import load_dotenv
from requests.exceptions import RequestException


load_dotenv()

client = OpenAI()


def comprehend_data(input_data):

    try:
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", 
                    "content": f"""You are a regulatory judge - with the task of determining whether the recipe has been given an 'unnecessary'
                    addition of extra fat - most likely in the form of excess butter, oil, cream etc. The key here is 'excess' there are 
                    food items which depend on these in order to be made - for example, a cake will have butter as a key ingredient. However,
                    there are many items that food producers add unnecessary fats in order to enhance the taste but at the cost of adding
                    significant calories. For example, Domino's pizza is notorious for adding extra oil to its sauce and butter to its crust.
                    Your job is to read the recipe given to you - from scratch approximate the macronutrients for the ingredients and add them up.
                    Then think through whether all of those ingredients would be necessary to make the food item at home. Then for those items
                    that are 'fatty' (so again - oils, butters, creams) think through again whether that's necessary and how many 'unnecessary' calories
                    it has added. You will apply a levy based on those unnecessary fatty calories in increments of £1 per 250 calories - so if an extra 250 calories a levy of £1, for
                    and extra 500 calories a levy of £2, an extra 750 calories would be a levy of £3 and so on.
                    Please output to a user the following (in the following format with the headings in bold):
                    <strong>Recipe</strong>: 'the outcome of what they are making - e.g. cake, pizza'
                    <strong>Unnecessary lipids</strong>: 'the extra fat-based foods discussed above'
                    <strong>Excess calories</strong>: 'the excess calories from the unnecessary lipids'
                    <strong>Levy</strong>: 'the levy that is being applied as a result'
                    Then on a new paragraph:
                    <strong>Suggestions</strong>: 'suggestions on how the recipe could be improved to reduce lipids/calories and ultimately the levy'
                    """},
                    {"role": "user",
                    "content": input_data }
                ]
            )

        output = completion.choices[0].message.content

        # print(output)

        return output
    
    except RequestException:
        raise RequestException