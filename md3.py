myString = 'Dolphins and Whales'
print(myString)
print(myString.lower())
print(myString.upper())
print(myString)
number = '123-456-7890'
print(number.isnumeric())

movie = "2001: A SPACE ODYSSEY"
book = "A Thousand Splendid Sharks"
poem = 'sammy lived in a pretty town'

print("Testing islower():")
print(movie.islower())
print(book.islower())
print(poem.islower())

print("Testing isupper():")
print(movie.isupper())
print(book.isupper())
print(poem.isupper())

print("Testing len():")
print(len(movie))
print(len(book))
print(len(poem))


balloon = "Sammy has a balloon."
print(balloon)
balloonWords = balloon.split()
print(balloonWords)
print(balloonWords[2])

print("Working with Google search")
gSearch = "https://www.google.com/search?sourceq=pretty+flowers&oq=pretty+flowers"
print(gSearch)
gSearchPhrases = gSearch.split("/")
print(gSearchPhrases)
searchPhrases = gSearchPhrases[3].split('?')
print(searchPhrases)
searchWords = searchPhrases[1].split('=')
print(searchWords)
searchFor = searchWords[2].split('+')
print(searchFor)

print("Work with .join()")
print(".".join(searchFor))
print(", ".join(reversed(searchFor)))
    

