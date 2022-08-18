from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from klimaatraadpleging import generate_json

# TODO: Specify config folder here
generate_json()
