try:
    file = open("sample1.txt", 'r')
    reading_file = file.read()
    print(reading_file)
    file.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
finally:
    print('Thank you...')