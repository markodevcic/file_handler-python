import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# remove unwanted string from a filename
def remove_string_from_filename():
    global renamed_files
    # piece of string that is going to be removed from filename
    unwanted_string = input(
        'Type or paste piece of text you want to remove from file name\n--> ')

    for root, subdirectories, files in os.walk(path):
        # print(os.path.join(root.split('/')[-1]))
        for index, file in enumerate(files):
            # print(os.path.join(file))
            file_name = os.path.join(file)
            if unwanted_string in file_name:
                renamed_file_name = file_name.replace(unwanted_string, "")
                os.rename(root + '/' + file, root + '/' + renamed_file_name)

                print(
                    f'--> File "{file_name}"\n\tis renamed to\n\t"{renamed_file_name}"\n')
                renamed_files += 1

    overall = f'Total renamed items: {renamed_files}'
    print(overall)


# index specific files in a directory
def index_file():
    global renamed_files
    global file_index

    filetype = input(
        'Type the exact file extension you want to index\n(example: mp3, jpg, txt, pdf, html... )\n--> ')

    for root, subdirectories, files in os.walk(path):
        for index, file in enumerate(files):
            file_name = os.path.join(file)
            if file_name.endswith(f'.{filetype}'):
                index_number = str(file_index).zfill(2) + ' - '
                os.rename(root + '/' + file, root +
                          '/' + index_number + file_name)
                print(
                    f'--> File "{file_name}"\n\tis indexed as\n\t"{index_number}{file_name}"\n')

                renamed_files += 1
                file_index += 1

    overall = f'Total indexed files: {renamed_files}'
    print(overall)


# delete files with given file type
def delete_file():
    global deleted_files

    filetype = input(
        'Type the exact file extension for files you want to delete\n(example: mp3, jpg, txt, pdf, html...)\n--> ')

    for root, subdirectories, files in os.walk(path):
        for index, file in enumerate(files):
            if file.endswith(f'.{filetype}'):
                os.remove(os.path.join(root + '/', file))

                print(f'--> Deleted file "{file}"\n')
                deleted_files += 1

    overall = f'Total deleted items: {deleted_files}'
    print(overall)


# list directory without hidden files
def listdir_nohidden(path):
    for file in os.listdir(path):
        if not file.startswith('.'):
            yield file


clear()

print('Choose an option:')
option = int(input('1. Index files (add numbers at the beginning of each file of filetype you choose)\n2. Remove specific text from filename\n3. Delete files with specific filetypes of your choice\n--> '))

# get the directory where the python script is located
path = os.path.dirname(os.path.realpath(__file__)) + '/'
# convert a function to a list
files = list(listdir_nohidden(path))
# for indexing specific file types in a directory
file_index = 1
# number of overall deleted and renamed files
deleted_files = 0
renamed_files = 0

if option == 1:
    index_file()
elif option == 2:
    remove_string_from_filename()
elif option == 3:
    delete_file()
else:
    print('You didn\'t choose any of the given options.')
