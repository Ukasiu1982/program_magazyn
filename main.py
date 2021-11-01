import os

from files import FileHandler

BASE_FOLDER = 'pliki'
FILE_INPUT = 'in.txt'
FILE_OUTPUT = 'out_2.txt'

file_path_input = os.path.join(FOLDER, FILE_INPUT)
file_path_output = os.path.join(FOLDER, FILE_OUTPUT)


history = []

file_handler = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
file_handler.read_history()
print(file_handler.history)

file_handler.write_history()

# read_history(file_path=file_path)
#
# print(history)
#
#
# write_history('history.txt')