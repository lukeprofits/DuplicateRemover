import csv

input('\n\nThis removes duplicate lines from column 1 of "input.csv". Press enter to continue.')

lines = set()
input_lines_count = 0
# Imports from csv
with open('input.csv', 'r') as csv_file:
    csv_reader_lines = csv.reader(csv_file)
    for x in csv_reader_lines:
        input_lines_count += 1
        x = x[0]

        # Extra conditions for ASIN's
        #if len(x) == 10:
            #lines.add(x)
        #else:
            #print('not == 10!')

        lines.add(x)

csv_file.close()

#write file

# Save
with open('output.csv', 'a', newline='') as csv_write:
    csv_writer_lines = csv.writer(csv_write)
    for x in lines:
        csv_writer_lines.writerow([x])
        print(x)
csv_write.close()

print('\nInput lines:',str(input_lines_count))
print('\nOutput after duplicate removal:',str(len(lines)))
input('\n\n[  DONE!  ]\n')