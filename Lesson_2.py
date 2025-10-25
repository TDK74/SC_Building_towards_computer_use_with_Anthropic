from anthropic import Anthropic
from helper import load_env


load_env()

## ------------------------------------------------------ ##
client = Anthropic()

## ------------------------------------------------------ ##
MODEL_NAME = "claude-3-5-sonnet-20241022"

## ------------------------------------------------------ ##
response = client.messages.create(model = MODEL_NAME, max_tokens = 1000,
                                  messages = [
                                            {"role" : "user",
                                             "content" : "Write a haiku about Anthropic"}
                                            ]
                                )

print(response.content[0].text)
## ------------------------------------------------------ ##
response    # print()

## ------------------------------------------------------ ##
response = client.messages.create(model = MODEL_NAME, max_tokens = 1000,
                                  messages = [
                                            {"role" : "user",
                                             "content" : "Hello! Only speak to me in Spanish"},
                                            {"role" : "assistant",
                                             "content" : "Hola!"},
                                            {"role" : "user",
                                             "content" : "How are you?"}
                                            ]
                                )

print(response.content[0].text)

## ------------------------------------------------------ ##
print("Simple Chatbot (type 'quit' to exit)")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    messages.append({"role" : "user", "content" : user_input})

    try:
        response = client.messages.create(model = MODEL_NAME, max_tokens = 200,
                                          messages = messages)

        asst_message = response.content[0].text
        print("Assistant:", asst_message)
        messages.append({"role" : "assistant", "content" : asst_message})

    except Exception as e:
        print(f"An error occurred: {e}")

## ------------------------------------------------------ ##
response = client.messages.create(model = MODEL_NAME, max_tokens = 1000,
                                  messages = [
                                            {"role" : "user",
                                             "content" : "Write a short poem about pigs"},
                                            {"role" : "assistant",
                                             "content" : "Oink"}
                                            ]
                                )

print(response.content[0].text)

## ------------------------------------------------------ ##
response = client.messages.create(model = MODEL_NAME, max_tokens = 100,
                                  messages = [
                                            {"role" : "user",
                                             "content" : "Write me an essay on LLMs"},
                                            ]
                                )

print(response.content[0].text)

## ------------------------------------------------------ ##
response    # print()

## ------------------------------------------------------ ##
prompt = """
        Generate a numbered, ordered list of technical topics
        I should learn if I want to work on LLMs
        """
response = client.messages.create(model = MODEL_NAME, max_tokens = 500,
                                  messages = [{"role" : "user", "content" : prompt}],
                                )

print(response.content[0].text)

## ------------------------------------------------------ ##
prompt = """
        Generate a numbered, ordered list of technical topics
        I should learn if I want to work on LLMs
        """
response = client.messages.create(model = MODEL_NAME, max_tokens = 500, stop_sequences = ["4."],
                                  messages = [{"role" : "user", "content" : prompt}],
                                )

print(response.content[0].text)

## ------------------------------------------------------ ##
response    # print()

## ------------------------------------------------------ ##
def demonstrate_temperature():
    temperatures = [0, 1]

    for temperature in temperatures:
        print(f"Prompting Claude three times with temperature of {temperature}")
        print("================")

        for i in range(3):
            response = client.messages.create(model = MODEL_NAME, max_tokens = 100,
                                        messages = [{"role" : "user",
                                                    "content" : f"Prompt {i+1}: Come up with "
                                                                f"a name for an alien planet. "
                                                                f"Respond with a single word."}],
                                        temperature = temperature
                                        )

            print(f"Response {i+1}: {response.content[0].text}")

## ------------------------------------------------------ ##
demonstrate_temperature()
