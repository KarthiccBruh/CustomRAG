from keywordGen import extract
from ollama import chat
from ollama import ChatResponse

a=extract()

response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': f'''You need to generate 10 Google searches queries in less than 20 words each, 
    Starting two queries should have these  {a.get('domain_keywords')}  {a.get('technical_skills')}  {a.get('certifications')}  {a.get('project_keywords')} ''',
    
  },
])
print(response['message']['content'])
print(response.message.content)