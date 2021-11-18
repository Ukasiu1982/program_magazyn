import sys
from files import FileHandler
from main import Magazyn

file_path_output = "out.txt"
file_path_input = sys.argv[1]
file_path_products = sys.argv[2:]

historia = FileHandler(file_path_read=file_path_input, file_path_write=file_path_output)
historia.read_history()


magazyn = Magazyn(historia.history)
magazyn.oblicz_aktualny_stan()
magazyn.stan_magazynu(file_path_products)
