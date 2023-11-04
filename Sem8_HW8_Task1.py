import os


def calculate_size(path):
    total_size = 0

    if os.path.isfile(path):
        return os.path.getsize(path)

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    return total_size


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            results.append({
                'Path': dir_path,
                'Type': 'Directory',
                'Size': calculate_size(dir_path)
            })

        for file in files:
            file_path = os.path.join(root, file)
            results.append({
                'Path': file_path,
                'Type': 'File',
                'Size': os.path.getsize(file_path)
            })

    return results


directory = 'geekbrains'
results = traverse_directory(directory)
for result in results:
    print(result)
