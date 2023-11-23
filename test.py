import glob
import webbrowser

"""
The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, 
although results are returned in arbitrary order.
"""
files = glob.glob('files/*.txt')
# Open and show the content of txt files
for filepath in files:
    with open(filepath, 'r') as file:
        print(file.read())

user_term = input('Enter key word: ')

webbrowser.open('https://www.google.com/search?q=' + user_term)
