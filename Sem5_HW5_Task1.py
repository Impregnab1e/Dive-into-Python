def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)



# import os

# def get_file_info(file_path):
#     file_directory, file_name_with_extension = os.path.split(file_path)
#     file_name, file_extension = os.path.splitext(file_name_with_extension)

#     file_directory = file_directory.replace('\\', '/')
    
#     if file_directory and not file_directory.endswith('/'):
#         file_directory += '/'
    
#     return (file_directory, file_name, file_extension)


#1
# file_path = 'C:/Users/User/Documents/example.txt'
# print(get_file_info(file_path = 'C:/Users/User/Documents/example.txt'))
#('C:/Users/User/Documents/', 'example', '.txt')

#2
# file_path = '/home/user/data/file'
# print(get_file_info(file_path = '/home/user/data/file'))
#('/home/user/data/', '', '.file')

#3
# file_path = 'D:/myfile.txt'
# print(get_file_info(file_path = 'D:/myfile.txt'))
# ('D:/', 'myfile', '.txt')

#4
# file_path = 'C:/Projects/project1/code/script.py'
# print(get_file_info(file_path = 'C:/Projects/project1/code/script.py'))
# ('C:/Projects/project1/code/', 'script', '.py')

#5
# file_path = '/home/user/docs/my.file.with.dots.txt'
# print(get_file_info(file_path = '/home/user/docs/my.file.with.dots.txt'))
# ('/home/user/docs/', 'my.file.with.dots', '.txt')

# 6
# file_path = 'file_in_current_directory.txt'
# print(get_file_info(file_path = 'file_in_current_directory.txt'))
# ('', 'file_in_current_directory', '.txt')