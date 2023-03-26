#failed

import openai
import os, sys


API_KEY = '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'


prompt = sys.argv[1]
openai.api_key = API_KEY


completions = openai.Completion.create(
# davinci-003 , davinci-002 also can be used.
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)