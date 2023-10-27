filenames = ['gl1.txt', 'gl2.txt']
with open('filenames', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)