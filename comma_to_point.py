import os

def comma_to_point(name_file):
    """IMPORTANT: the file should be in the same directory of
           the comma_to_point.py file

    :name_file: str - name of the file including file extension
    :return: str - new name of the created file

    Creates a folder called "dot_files" where places the new files
    with a new name: file_name_dot.extension
    """
    file = open(os.path.join(os.getcwd(), name_file), 'r')

    dot_folder = "dot_files"
    new_path = os.path.join(os.getcwd(), dot_folder)

    # Crea la cartella se non c'è

    if dot_folder not in os.listdir(os.getcwd()):
        os.mkdir(new_path)

    new_name = str(name_file).replace(".txt", "_dot.txt")

    # Controlla se è già stato creato un file

    if new_name in os.listdir(new_path):
        print("--------------------------"
              "\n   File already exists!   \n"
              "--------------------------")
    else:
        new_file = open(os.path.join(new_path, new_name), 'a')

        for lines in file:
            new_file.write(lines.replace(",", "."))

        print("---------------------------"
              "\n File created successfully \n"
              "---------------------------")

    return  os.path.join(new_path, new_name)

    pass
