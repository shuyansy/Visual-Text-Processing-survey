
import time
import openai
import json
from tqdm import tqdm
import os
import cv2
import base64
import random



def chat(image_path):
    openai.api_key=""

    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")


    # Prepare the messages
    messages = [
        {
            "role": "system",
            "content": """
            The image you will receive is composed of two parts: (1) The top section contains the original image. (2) The bottom section is generated by a model after image deblurriing. Please evaluate the model’s image deblurring capabilities based on the following two criteria:

            (1) Visual Quality (Score: 0-5): Assign a higher score if the deblurred image (the bottom section) exhibits higher viqual quality, including better clarity, lower noise, higher color accuracy and higher Edge Preservation.

            (2) Content Readability (Score: 0-5): Assign a higher score if the text and visual elements in the deblurred image (the bottom section) are clear to read and understand.

            Output the evaluation strictly in the following JSON format without any additional explanation or comments:
            {'Visual Quality: score_visual, 'Textual Fidelity': score_text, 'total_score': score_visual + score_text}
            """
        },
        {
            "role": "user",
            "content": [{
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}
            }]
        }
    ]

    # Call the OpenAI API
    
    response = openai.ChatCompletion.create(model="gpt-4o",messages=messages,temperature=0)
    # response_message = completion["choices"][0]["message"]["content"]
    return response.choices[0].message['content']

if __name__ == '__main__':
    folder = "data/docres"
    new_folder = "./evaluation_results/docres"
    image_list = os.listdir(folder)

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for i in tqdm(image_list):

        if i.replace(".png", ".json") in os.listdir(new_folder):
            continue

        save_dict = {}
        image_path = os.path.join(folder, i)
        print(f"Processing {image_path}")
        response = chat(image_path)
        print(response)
        save_dict[i] = response

        with open(os.path.join(new_folder, i.replace(".png", ".json")), "w") as f:
            json.dump(save_dict, f)
