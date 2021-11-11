import os
import sys
import pandas as pd
import re

def masking(file_name, table_name):
    """
    Input: Filename to read in pandas
    :return:
    """
    regex_find = r"(?<=.)[^@\n](?=[^@\n]*?@)"
    regex_subst = r'*'
    column_name = 'header4'

    #Read the file in pandas
    df = pd.read_csv(file_name)

    #Print the df without any changes
    print(df.head())

    #Make the required changes
    df[column_name] = df[column_name].apply(regex_repl, args=(regex_find, regex_subst,))

    #print the file after changes
    print(df.head())

    #Execute the regex on pandas columns

def regex_repl(column_name, regex, subst):
    result = re.sub(regex, subst, column_name, 0, re.MULTILINE)
    return result

masking("s3_file.csv", "table_name")

regex = r"(?<=.)[^@\n](?=[^@\n]*?@)"
test_str = ("john.doe@example.en.com")
subst = "*"

#regex_test(regex, test_str, subst)

def hashing(file_name, table_name):
    pass

hashing()

def encryption():
    pass

encryption()
