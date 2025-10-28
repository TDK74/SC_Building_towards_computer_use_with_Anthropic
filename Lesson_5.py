import time

from anthropic import Anthropic
from helper import load_env


load_env()

## ------------------------------------------------------ ##
client = Anthropic()
MODEL_NAME = "claude-3-5-sonnet-20241022"

## ------------------------------------------------------ ##
with open('files/frankestein.txt', 'r') as file:
    book_content = file.read()

## ------------------------------------------------------ ##
len(book_content)

## ------------------------------------------------------ ##
book_content[1000 : 2000]    # print()

## ------------------------------------------------------ ##
def make_non_cached_api_call():
    messages = [
                {
                "role" : "user",
                "content" : [
                            {
                            "type" : "text",
                            "text" : "<book>" + book_content + "</book>"
                            },
                            {
                            "type" : "text",
                            "text" : "What happens in chapter 3?"
                            }
                            ]
                }
                ]

    start_time = time.time()
    response = client.messages.create(model = MODEL_NAME, max_tokens = 500, messages = messages, )
    end_time = time.time()

    return response, end_time - start_time

## ------------------------------------------------------ ##
non_cached_response, non_cached_time = make_non_cached_api_call()
print(f"Non-cached time: {non_cached_time:.2f} seconds")

print("\nOutput (non-cached):  ")
print(non_cached_response.content)

## ------------------------------------------------------ ##
non_cached_response.usage   # print()

## ------------------------------------------------------ ##
def make_cached_api_call():
    messages = [
                {
                "role" : "user",
                "content" : [
                            {
                            "type" : "text",
                            "text" : "<book>" + book_content + "</book>",
                            "cache_control" : {"type" : "ephemeral"}
                            },
                            {
                            "type" : "text",
                            "text" : "What happens in chapter 5?"
                            }
                            ]
                }
                ]

    start_time = time.time()
    response = client.messages.create(model = MODEL_NAME, max_tokens = 500, messages = messages, )
    end_time = time.time()

    return response, end_time - start_time

## ------------------------------------------------------ ##
response1, duration1 = make_cached_api_call()

## ------------------------------------------------------ ##
response1   # print()

## ------------------------------------------------------ ##
response2, duration2 = make_cached_api_call()

## ------------------------------------------------------ ##
response2.usage   # print()

## ------------------------------------------------------ ##
duration2   # print()

## ------------------------------------------------------ ##
messages = [
            {
            "role" : "user",
            "content" : [
                        {
                        "type" : "text",
                        "text" : "Hello, can you tell me more about the solar system",
                        "cache_control" : {"type" : "ephemeral"}
                        }
                        ]
            },
            {
            "role" : "assistant",
            "content" : "Certainly! The solar system is the collection of celestial bodies that "
                        "orbit our Sun. It consists of eight planets, numerous moons, asteroids, "
                        "comets, and other objects. The planets, in order from closest to farthest "
                        "from the Sun, are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, "
                        "and Neptune. Each planet has its own unique characteristics and features. "
                        "Is there a specific aspect of the solar system you'd like to "
                        "know more about?"
            },
            {
            "role" : "user",
            "content" : [
                        {
                        "type" : "text",
                        "text" : "Tell me more about Mars.",
                        "cache_control" : {"type" : "ephemeral"}
                        }
                        ]
            }
            ]

## ------------------------------------------------------ ##
messages = [
            {
            "role" : "user",
            "content" : [
                        {
                        "type" : "text",
                        "text" : "Hello, can you tell me more about the solar system",
                        }
                        ]
            },
            {
            "role" : "assistant",
            "content" : "Certainly! The solar system is the collection of celestial bodies that "
                        "orbit our Sun. It consists of eight planets, numerous moons, asteroids, "
                        "comets, and other objects. The planets, in order from closest to farthest "
                        "from the Sun, are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, "
                        "and Neptune. Each planet has its own unique characteristics and features. "
                        "Is there a specific aspect of the solar system you'd like to "
                        "know more about?"
            },
            {
            "role" : "user",
            "content" : [
                        {
                        "type" : "text",
                        "text" : "Tell me more about Mars.",
                        "cache_control" : {"type" : "ephemeral"}
                        }
                        ]
            },
            {
            "role" : "assistant",
            "content" : "I'd love to tell you about Mars.  Mars is...."
            },
            {
            "role" : "user",
            "content" : [
                        {
                        "type" : "text",
                        "text" : "That's really neat.  Tell me about Pluto!",
                        "cache_control" : {"type" : "ephemeral"}
                        }
                        ]
            },
            ]
