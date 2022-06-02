from easygui import fileopenbox
from pip import main


def text_replacer(search, change):

    extensions = ['doc', 'txt']

    # Select file
    file_path = fileopenbox()

    # Check extension for validity
    file_path_checker = file_path.split('.')

    if extensions[0] not in file_path_checker and extensions[1] not in file_path_checker:
        print('Sorry, this program can\'t access that file type.')
    else:

        # Open and read document
        file_text = open(file_path, mode='r').read()
        print(file_text)

        # Search for keywords

        # Replace keywords with change

        # Save file


text_replacer(1, 1)
