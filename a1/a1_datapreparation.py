

# Part 1: DATA PREPARATION

"""
Importing modules
"""

import re
import argparse
import csv


"""
Loading data and saving into different files
"""
# path /usr/local/courses/lt2316-h19/a1
# scp -P 62266 -r gusmiriasa@mltgpu.flov.gu.se:../../usr/local/courses/lt2316-h19/a1 homefolder_name

languages = ["Catalan", "Esperanto", "English", "Euskera", "French", "Galician", "Italian", "Latin", "Portuguese", "Spanish"]
mylabels = ["cat", "epo", "eng", "eus", "fra", "glg", "ita", "lat", "por", "spa"]
labels = 'y_train.txt'
all_languages = 'x_train.txt' 

def read_file(labels, all_languages, mylabels, write_y, write_x):
    with open(labels, encoding="utf8") as labels:
        with open(all_languages, encoding="utf8") as all_languages:
            for label_line, language_line in zip(labels, all_languages):
                label_line=re.sub(r'(\n)',"", label_line)
                language_line=re.sub(r'(\n)',"", language_line)
                if label_line in mylabels:
                    
                    # labels
                    file_labels = open(write_y, 'a+', encoding="utf8")
                    file_labels.write(label_line +'\n')
                    # data
                    lang100char = language_line[:100] # use only sentences up to 100 characters
                    file_all_languages = open(write_x, 'a+',encoding="utf8")
                    file_all_languages.write(lang100char+'\n')

    print("Done writing labels and languages into files.")
    file_all_languages.close()
    file_labels.close()

 #read_file(labels, all_languages,mylabels, "new_y", "new_x")


"""
Mapping labels to languages
"""
# We get them from the labels.csv file
def get_labels(filename):
       with open(filename, encoding='utf-8') as file_labels:
        csv_reader = csv.reader(file_labels, delimiter=';')
        next(csv_reader) # omits header
        print(("{:<30s} {:>20s}").format("Language name", "Language code"))
        print("---------------------------------------------------")
        for row in csv_reader:
            language = row[1]
            code = row[0]
            print(("{:<30s} {:>20s}").format(language, code))

    

"""
Terminal arguments
"""

parser = argparse.ArgumentParser(description="Creates two separate documents with labels and text in the chosen languages and saves them.")

parser.add_argument("-s", "--showall", metavar="s", dest="language_labels", type=str, help="Shows languages and corresponding language codes.")
parser.add_argument("y_file", type=str, nargs='?', help="File with language labels.")
parser.add_argument("x_file", type=str, nargs='?', help="File with language sentences.")
parser.add_argument("new_y", type=str, nargs='?', help="File with new language labels.")
parser.add_argument("new_x", type=str, nargs='?', help="File with new language sentences.")
parser.add_argument("languages", type=str, nargs='?', help="Chosen language codes.")

args = parser.parse_args()

if args.language_labels:
    get_labels(args.language_labels) # from function that gets labels from csv
    exit(1)

languages = args.languages.split(",")
read_file(args.y_file, args.x_file, languages, args.new_y, args.new_x)







