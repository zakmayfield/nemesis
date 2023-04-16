file = open("sandbox/intermediate/file-io/example.txt", "w")
file.write("Hello world!")

file.close()

file = open("sandbox/intermediate/file-io/example.txt", "r")
content = file.read()

print(content)

file.close()