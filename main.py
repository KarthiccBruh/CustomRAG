from generator import *
inputs = {"question": "get dic method?", "max_retries": 3}
for event in graph.stream(inputs, stream_mode="values"):
    print(event)