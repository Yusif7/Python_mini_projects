Not:
shift + tab -> move a code block to the left

Find methods:
Python Console -> dir(data type name)
Description of method:
Python Console -> help(str.lower)

List Methods:
list_name.__setitem__(item_index, new_item) == list_name[item_index] = new_item
list_name.__getitem__(item_index) == list_name[item_index]

Enumerate:
Enumerate all list elements, starts from zero to last index

r - char before path:
file = open(r"C:\Users\Download\todos.txt", "r") - when we add 'r' before path , we tell to python all char inside quotes are text 

Zip method:
zip method helps us to add one object inside to another(test.py)

Write(w)/Read(r) mode on text file:
with open('test.txt', 'r') -> only for reading
with open('test.txt', 'w') -> if you do any item modification at last use 'w' mode for overwriting new content of file

Difference between match and if :
- In match case , program continue to control cases after find needed case
- In if condition program stop working after find needed con 

The writelines() method writes the items of a list to the file.
- Where the texts will be inserted depends on the file mode and stream position.
- "a":  The texts will be inserted at the current file stream position, default at the end of the file.
- "w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.

The all() function returns True if all items in an iterable are true, otherwise it returns False.

Use try-except concept for control exceptions in code. 


if __name__ == "__main__":
I mean, that means somebody is running this script directly, and that's somebody which is us.
That somebody wants these lines to be executed.
Otherwise, if I'm being imported, the file says, then I will not execute this because my name is
not Main is something else.
So that is the distinction we can make to control what we execute when the file is run directly and
what we execute when the file is run indirectly through this import statement.