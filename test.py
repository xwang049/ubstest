# import ast
data = b'[\n    { generations: 10, colony: "1000"\n    },\n    { generations: 50, colony: "1000"\n    }\n]'
decode_data = data.decode('utf-8')
print(decode_data)
print(decode_data[1:-1])
list1 = decode_data[1:-1].split(", ")
print(list1)
print(type(list1))
