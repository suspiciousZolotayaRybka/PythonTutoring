def get_word(char):
    word_list = ['apple', 'banana', 'cat', 'dog', 'elephant', 
             'fox', 'goat', 'horse', 'ice cream', 'jungle', 
             'koala', 'lion', 'monkey', 'nest', 'orange', 
             'penguin', 'queen', 'rabbit', 'snake', 'tiger', 
             'umbrella', 'violet', 'whale', 'xylophone', 
             'yak', 'zebra']
    for word in word_list:
        if word[0] == char:
            return word

def main():
    print("Please enter input.")
    print("I will tell you a word for each character in your input.")
    user_input = input("=>")

    for char in user_input:
        word = get_word(char.lower())
        print(char + word[1:])
main()
