import ollama
import json
#initialise the client
client=ollama.Client()
#define model and prompt
model="llama2"
prompt="Write a short story about a character who discovers a hidden world within their reflection."
response=client.generate(model=model, prompt=prompt)
print("response from ollama")
print(response.response)