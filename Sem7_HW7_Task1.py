import os

def batch_rename_files(directory, desired_name, num_digits, source_extension, destination_extension, name_range=None):
    try:
        file_list = os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return

    file_count = 1

    for file_name in file_list:
        if file_name.endswith(f".{source_extension}"):
            original_file_path = os.path.join(directory, file_name)
            if name_range is not None:
                start, end = name_range
                base_name = file_name[start - 1:end]
            else:
                base_name = ""
            new_file_name = f"{desired_name}{str(file_count).zfill(num_digits)}.{destination_extension}"
            new_file_path = os.path.join(directory, new_file_name)
            os.rename(original_file_path, new_file_path)
            file_count += 1

    print(f"Renamed {file_count - 1} files in '{directory}'.")


batch_rename_files("E:\\Учеба\\Учусь\\Dive into Python", "pythonbook", 3, "txt", "png", (1, 4))