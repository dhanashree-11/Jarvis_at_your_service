from openai import OpenAI

#client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
 api_key="use your api key",
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Virtual assistant named Jarvis skilled in general tasks like Alexa and Google ."},
    {"role": "user", "content": "WHat is coding"}
  ]
)

print(completion.choices[0].message)
