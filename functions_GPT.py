# Script to host ChatGPT functions - taken from other Inversity projects

from openai import OpenAI
from dotenv import load_dotenv
from requests.exceptions import RequestException


load_dotenv()

client = OpenAI()


def comprehend_data(input_data, mark_scheme):

    try:
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", 
                    "content": f"""This is meant to be a guide for people learning to code on their GitHub. Can you please read the file
                    that you will be given and compare to the mark scheme. You can find a markscheme here {mark_scheme}. Please then write
                    a short paragraph with feedback and guidance on whether it can be submitted to Inversity (it DOES NOT need to be at production level
                    to be ready to submit, just at proof of concept stage). Keep the total paragraph short, not more than 4 sentences.
                    So please put it in the format of 'Stage: (Then fill in what stage it is at as per the markscheme).' and then on a new line a paragraph with
                    'Feedback: (Then provide encouraging and specific feedback here on how to improve).' and then on another new line 'Status: (Mark as 'Ready to submit' unless they user has
                    written less than 100 lines of code across the repo). 
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