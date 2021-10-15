import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


slash = '\\' if os.name == 'nt' else '/'


# remove unwanted string from a filename
def remove_string():
    renamed_files = 0
    # piece of string that is going to be removed
    unwanted_string = input(
        'Type or paste piece of text you want to remove from file name\n--> ')

    exclude_prefixes = ('__', '.')
    for root, dirs, files in os.walk(full_path):
        # exclude all files starting with exclude_prefixes
        files = [f for f in files if not f[0].startswith(exclude_prefixes)]
        # exclude all dirs starting with exclude_prefixes
        dirs[:] = [d for d in dirs if not d.startswith(
            exclude_prefixes)]
        # print(os.path.join(root.split('/')[-1]))
        for file in files:
            # print(os.path.join(file))
            file_name = os.path.join(file)
            if unwanted_string in file_name:
                renamed_file_name = file_name.replace(unwanted_string, "")
                os.rename(root + slash + file,
                          root + slash + renamed_file_name)

                print(
                    f'--> File "{file_name}"\n\tis renamed to\n\t"'
                    f'{renamed_file_name}"\n')
                renamed_files += 1

    overall = f'Total renamed items: {renamed_files}'
    print(overall)


# add string at the beginning of the filename
def add_string_at_start():
    renamed_files = 0

    filetype = input(
        'Type the exact file extension you want to add string to\n(example: '
        'mp3, jpg, '
        'txt, pdf, html... )\n--> ')
    # piece of string that is going to be added
    add_string = input(
        'Type or paste piece of text you want to add at the filename '
        'beginning\n--> ')

    exclude_prefixes = ('__', '.')
    for root, dirs, files in os.walk(full_path):
        files = [f for f in files if not f[0].startswith(exclude_prefixes)]
        dirs[:] = [d for d in dirs if not d.startswith(
            exclude_prefixes)]
        for file in files:
            file_name = os.path.join(file)

            if file_name.endswith(f'.{filetype}'):
                renamed_file_name = add_string + file_name
                os.rename(root + slash + file, root + slash + renamed_file_name)

                print(
                    f'--> File "{file_name}"\n\tis renamed to\n\t"'
                    f'{renamed_file_name}"\n')
                renamed_files += 1

    overall = f'Total renamed items: {renamed_files}'
    print(overall)


# index specific files in a directory
def index_file():
    renamed_files = 0

    filetype = input(
        'Type the exact file extension you want to index\n(example: mp3, jpg, '
        'txt, pdf, html... )\n--> ')

    exclude_prefixes = ('__', '.')
    for root, dirs, files in os.walk(full_path):
        files = [f for f in files if not f[0].startswith(exclude_prefixes)]
        dirs[:] = [d for d in dirs if not d.startswith(
            exclude_prefixes)]
        file_index = 1
        for file in files:
            file_name = os.path.join(file)
            if file_name.endswith(f'.{filetype}'):
                index_number = str(file_index).zfill(2) + ' - '
                os.rename(root + slash + file, root +
                          slash + index_number + file_name)
                print(
                    f'--> File "{file_name}"\n\tis indexed as\n\t"'
                    f'{index_number}{file_name}"\n')

                renamed_files += 1
                file_index += 1

    overall = f'Total indexed files: {renamed_files}'
    print(overall)


# delete files with given file type
def delete_file():
    deleted_files = 0

    filetype = input(
        'Type the exact file extension for files you want to delete\n('
        'example: mp3, jpg, txt, pdf, html...)\n--> ')

    exclude_prefixes = ('__', '.')
    for root, dirs, files in os.walk(full_path):
        files = [f for f in files if not f[0].startswith(exclude_prefixes)]
        dirs[:] = [d for d in dirs if not d.startswith(
            exclude_prefixes)]
        for file in files:
            if file.endswith(f'.{filetype}'):
                os.remove(os.path.join(root + slash, file))

                print(f'--> Deleted file "{file}"\n')
                deleted_files += 1

    overall = f'Total deleted items: {deleted_files}'
    print(overall)


clear()

print('Choose an option:')
features = [
    '1. Index files (add numbers at the beginning of each file of filetype '
    'you choose)',
    '2. Remove specific text from filename',
    '3. Add text at the beginning of the filename',
    '4. Delete files with specific filetypes of your choice']
for i in range(len(features)):
    print(features[i])
option = int(input('--> '))

# get the directory where the python script is located
full_path = os.path.dirname(os.path.realpath(__file__)) + slash

if option == 1:
    index_file()
elif option == 2:
    remove_string()
elif option == 3:
    add_string_at_start()
elif option == 4:
    delete_file()
else:
    print('You didn\'t choose any of the given options.')
