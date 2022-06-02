from docx import Document
from easygui import fileopenbox
from fileinput import FileInput
import textract


def text_replacer(search, change):

    extensions = ['docx', 'txt']

    # Select file
    # Check extension for validity
    try:
        file_path = fileopenbox()

        file_path_checker = file_path.split('.')

    except AttributeError:
        print('Program exited...')

    else:
        if file_path_checker[-1] not in extensions:

            print('Sorry, this program can\'t access that file type.')

        elif file_path_checker[-1] == 'txt':

            # Open, read, overwrite keywords, save.
            with FileInput(file_path, inplace=True) as file:
                for line in file:
                    print(line.replace(search, change))

            print(
                f'All instances of {search} have been replaced with {change}!')

        else:
            print("Still working on that feature!")

            # Start file stream and create copy of document.
            document = Document(f'{file_path}')
            document.save('new_text.docx')
            # Search for keywords

            # Replace keywords with change

            # Save file


text_replacer('POSITION', 'software developer')
