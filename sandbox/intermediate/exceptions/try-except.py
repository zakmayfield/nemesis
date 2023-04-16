# try & except is a way to handle code that might blow up

try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("An error occurred")