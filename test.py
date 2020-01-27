from bson_lazy import load

data = b'qwertyuiop' * 100000000

answer = load(data)
json = answer.json()
answer.printi(1)