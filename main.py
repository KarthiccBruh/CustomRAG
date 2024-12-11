from Generator import *
inputs = {"question": "Introduction to cyber security", "max_retries": 3}
for event in graph.stream(inputs, stream_mode="values"):
    print(event)