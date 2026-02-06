import google.generativeai as genai

genai.configure(api_key = "AIzaSyDb6qujZUCPHVgrpB0yet4S7oR4fcKKqJQ")

for m in genai.list_models():
    print(m.name)