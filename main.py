# try except blocks

try:
    file = open('test_file.txt')

# bare except not recommended as it will ignore all errors
except FileNotFoundError:
    open('test_file.txt', mode='w')
# Useful to pass errors along to debug or warn users if needed
except KeyError as error_message:
    print(f'The key {error_message} does not exists')

# else only happens if try statement succeeds
else:
    content = file.read()
    print(content)

# Will do even if fail or pass
finally:
    file.close()
    print('file is closed')

    # Raise helps to force an error and can key in personal message
    # raise TypeError('message to print on top of error')
