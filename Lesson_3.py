import base64
import mimetypes

from anthropic import Anthropic
from helper import load_env
from IPython.display import Image


load_env()

## ------------------------------------------------------ ##
client = Anthropic()
MODEL_NAME = "claude-3-5-sonnet-20241022"

## ------------------------------------------------------ ##
messages = [
            {
            "role" : "user",
            "content" : "tell me a joke"
            }
        ]

response = client.messages.create(messages = messages, model = MODEL_NAME, max_tokens = 200)
print(response.content[0].text)

## ------------------------------------------------------ ##
messages = [
            {
            "role": "user",
            "content": [
                        {"type" : "text", "text" : "tell me a joke"},
                        ]
            }
        ]

response = client.messages.create(messages = messages, model = MODEL_NAME, max_tokens = 200)
print(response.content[0].text)

## ------------------------------------------------------ ##
messages = [
            {
            "role": "user",
            "content": [
                        {"type" : "text", "text" : "who"},
                        {"type" : "text", "text" : "made"},
                        {"type" : "text", "text" : "you?"},
                        ]
            }
        ]
response = client.messages.create(messages = messages, model = MODEL_NAME, max_tokens = 200)
print(response.content[0].text)

## ------------------------------------------------------ ##
Image(filename = 'images/food.png')

## ------------------------------------------------------ ##
with open("images/food.png", "rb") as image_file:
    binary_data = image_file.read()
    base_64_encoded_data = base64.b64encode(binary_data)
    base64_string = base_64_encoded_data.decode('utf-8')

## ------------------------------------------------------ ##
base64_string[ : 100]

## ------------------------------------------------------ ##
messages = [
            {
            "role" : "user",
            "content" : [{
                        "type" : "image",
                        "source" : {
                                    "type" : "base64",
                                    "media_type" : "image/png",
                                    "data" : base64_string
                                    },
                        },
                        {
                        "type" : "text",
                        "text" : """How many to-go containers of each type \
                                    are in this image?"""
                        }]
            }
            ]

## ------------------------------------------------------ ##
response = client.messages.create(messages = messages, model = MODEL_NAME, max_tokens = 200)
print(response.content[0].text)

## ------------------------------------------------------ ##
def create_image_message(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()

    base64_encoded_data = base64.b64encode(binary_data)
    base64_string = base64_encoded_data.decode('utf-8')

    mime_type, _ = mimetypes.guess_type(image_path)
    image_block = {
                "type" : "image",
                "source" : {
                            "type" : "base64",
                            "media_type" : mime_type,
                            "data" : base64_string
                            }
                }

    return image_block

## ------------------------------------------------------ ##
base64_string[ : 100]

## ------------------------------------------------------ ##
messages = [
            {
            "role" : "user",
            "content" : [{
                        "type" : "image",
                        "source" : {
                                    "type" : "base64",
                                    "media_type" : "image/png",
                                    "data" : base64_string
                                    },
                        },
                        {
                        "type" : "text",
                        "text" : """How many to-go containers of each type \
                                    are in this image?"""
                        }]
            }
            ]

## ------------------------------------------------------ ##
response = client.messages.create(messages = messages, model = MODEL_NAME, max_tokens = 200)
print(response.content[0].text)

## ------------------------------------------------------ ##
def create_image_message(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()

    base64_encoded_data = base64.b64encode(binary_data)
    base64_string = base64_encoded_data.decode('utf-8')

    mime_type, _ = mimetypes.guess_type(image_path)
    image_block = {
                "type" : "image",
                "source" : {
                            "type" : "base64",
                            "media_type" : mime_type,
                            "data" : base64_string
                            }
                }

    return image_block

## ------------------------------------------------------ ##
Image("images/plant.png")

## ------------------------------------------------------ ##
messages = [
            {
            "role": "user",
            "content" : [
                        create_image_message("./images/plant.png"),
                        {"type" : "text", "text" : "What species is this?"}
                        ]
            }
            ]

response = client.messages.create(model = MODEL_NAME, max_tokens = 2048, messages = messages)
print(response.content[0].text)

## ------------------------------------------------------ ##
Image(filename='images/invoice.png')

## ------------------------------------------------------ ##
messages = [
            {
            "role" : "user",
            "content" : [
                        create_image_message("./images/invoice.png"),
                        {"type" : "text",
                         "text" : """
                                    Generate a JSON object representing the contents \
                                    of this invoice.  It should include all dates, \
                                    dollar amounts, and addresses. \
                                    Only respond with the JSON itself.
                                    """
                        }
                        ]
            }
            ]

response = client.messages.create(model = MODEL_NAME, max_tokens = 2048, messages = messages)
print(response.content[0].text)

## ------------------------------------------------------ ##
response = client.messages.create(max_tokens = 1024,
                                  messages = [{"role" : "user", "content" : "write a poem"}],
                                  model = MODEL_NAME, )
print(response.content[0].text)

## ------------------------------------------------------ ##
with client.messages.stream(max_tokens = 1024,
                            messages = [{"role" : "user", "content" : "write a poem"}],
                            model = MODEL_NAME, ) as stream:
  for text in stream.text_stream:
      print(text, end = "", flush = True)
