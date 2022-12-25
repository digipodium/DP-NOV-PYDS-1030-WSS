def word_count(sentence):
    words = sentence.split()
    return len(words)
    
# calling
print(word_count("Hello World!"))

size = word_count("Hello World of Pain")   
print(size)

data = input("Enter a sentence: ")
size = word_count(data)
print(f'you entered {size} words')