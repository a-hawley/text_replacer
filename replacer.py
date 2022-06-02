from easygui import fileopenbox
from pip import main


def text_replacer(search, change):

    extensions = ['docx', 'txt']

    # Select file
    file_path = fileopenbox()

    # Check extension for validity
    file_path_checker = file_path.split('.')

    if file_path_checker[1] not in extensions:

        print('Sorry, this program can\'t access that file type.')

    elif file_path_checker[1] == 'txt':

        # Open and read document
        file_text = open(file_path, mode='r').read()
        print(file_text)

    else:
        print("Still working on that feature!")

        # Search for keywords

        # Replace keywords with change

        # Save file


text_replacer(1, 1)
