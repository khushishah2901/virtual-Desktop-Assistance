import google.generativeai as genai
# import os


# add your api key
genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-flash')

query = "who is the founder of ICICI Bank"
response = model.generate_content(query)
print(response.text)