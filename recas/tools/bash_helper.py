import os
import urllib.request
import csv

def mkdir(dirName):
    try:
        folder = os.path.join("corpora",dirName)
        os.mkdir(folder)
    except FileExistsError:
        print("Directory " , dirName ,  " already exists!")


def download_file(url, corpus_dir, file_name):
    target_file = os.path.join("corpora", corpus_dir, file_name)
    if not os.path.exists(target_file):
        with urllib.request.urlopen(url) as response, open(target_file, 'wb') as out_file:
            data = response.read() # a `bytes` object
            out_file.write(data)
    else:
        print("File already exists!")

def read_tsv(corpus_dir, file_name):
    target_file = os.path.join("corpora", corpus_dir, file_name)

    corpora = []
    with open(target_file) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            corpora.append(line)

    return corpora

def write_tsv(list_to_store, corpus_dir, file_name):
    target_file = os.path.join("corpora", corpus_dir, file_name)
    with open(target_file, 'w', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        for row in list_to_store:
            tsv_output.writerow(row)
