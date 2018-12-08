from sys import argv
from os.path import exists

script, from_file, to_file = argv

# No prompts, no intermittent storing of values, no need for close since these are str
out_file = open(to_file, "w").write(open(from_file).read())