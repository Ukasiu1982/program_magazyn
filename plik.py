import sys
from files import FileHandler
from main import Magazyn

file_path_output = "out.txt"
file_path_input = sys.argv[1]


file_handler = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
file_handler.read_history()

magazyn = Magazyn(file_handler.history)
magazyn.oblicz_aktualny_stan()
nowa_komenda = sys.argv[2:]
magazyn.wykonaj_komende(nowa_komenda)
file_handler.write_history(magazyn.historia)
