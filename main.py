import absl.app
import requests
import json
import os
import absl.app
import absl.flags as flags

FLAGS = flags.FLAGS

_MODEL = flags.DEFINE_string("model", "text-davinci-003", "The model to use for generating completions.")
_MAX_TOKENS = flags.DEFINE_integer("max_tokens", 4000, "The maximum number of tokens to generate.")
_TEMPERATURE = flags.DEFINE_float("temperature", 0.0, "The temperature value for controlling randomness.")

API_ENDPOINT = "https://api.openai.com/v1/completions"

def query_chatgpt(prompt: str) -> None:
    api_key = os.environ.get("OPENAI_API_KEY")

    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data: dict = {
        "model": _MODEL.value,
        "prompt": prompt,
        "max_tokens": _MAX_TOKENS.value,
        "temperature": _TEMPERATURE.value
    }

    response = requests.post(
        API_ENDPOINT, headers=headers, data=json.dumps(data))
    response_data = response.json()
    choices: list[str] = [
        choice["text"] for choice in response_data.get("choices", [])]
    output: str = "\n".join(choices)
    print(output)

def main(argv):

    while True:
        user_input: str = input("ChatGPT: ")

        if user_input == "quit()":
            print("Exiting the program...")
            break

        query_chatgpt(user_input)

if __name__ == "__main__":
    absl.app.run(main)