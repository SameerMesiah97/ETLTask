from datetime import datetime


def is_valid_date(date):
    is_valid = None

    try:
        datetime_object = datetime.strptime(date, '%d %B %Y')
        is_valid = True
    # Catches invalid date entries i.e. 81 April 2000 or a non-date string.
    except ValueError:
        is_valid = False

    return is_valid


import csv


def transform_csv(file):
    # Create new file to store clean data
    clean_file = open("clean_file.csv", 'w', newline='')
    csv_writer = csv.writer(clean_file, delimiter=',')

    # Column headings for new file
    headers = ["index", "stream", "sub1", "sub1_r", "sub2", "sub2_r", "sub3", "sub3_r", "cgt_r",
               "general_english_r", "birth_date", "island_rank", "district_rank"]

    # Add headings to new file.
    csv_writer.writerow(headers)

    try:
        with open(file, newline='') as file:
            csv_reader = csv.reader(file, delimiter=",")
            csv_reader.__next__()

            for row in csv_reader:
                # Remove rows with missing entries
                if '-' not in row:

                    # Remove students who were absent for all the exams.
                    if not (row[4] == row[6] == row[8] == row[9] == row[10] == 'Absent'):
                        birth_date = [' '.join(row[11:14])]

                        # Remove rows with invalid date related entries.
                        if is_valid_date(' '.join(row[11:14])):
                            # Copy all valid rows to new file.
                            csv_writer.writerow(row[:2] + row[3:11] + birth_date + row[15:17])

            print("clean_file.csv created in main folder")
    except FileNotFoundError as errmsg:
        print(errmsg)
    finally:
        clean_file.close()

transform_csv('al_results_original.csv')
