import os
import os
import sys
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

global path_1
global path_2
global df_1
global df_2
global column_names_list_1
global column_names_list_2
global column_1
global column_1_1
global column_2
global column_2_2

def print_all_files(source_path):
    # Scan the directory and get
    # an iterator of os.DirEntry objects
    # corresponding to entries in it
    obj = os.scandir()

    # List all files and directories in the specified path
    # print("Files and Directories in '% s':" % source_path)
    dir_list = []
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            dir_list.append(entry.name)
    print(*dir_list, sep='\n')



def print_and_return_all_files_second_method(source_path):
   
    dir_list = os.listdir(source_path)
    print("Files and directories in '", source_path, "' :")
    # prints all files
    print(dir_list)
    return dir_list



def print_and_return_all_files_innumerated(source_path):
   
    dir_list = os.listdir(source_path)
    print("Files and directories in '", source_path, "' :")
    # prints all files
    for file in dir_list:
        print(str(dir_list.index(file)) + "-" + file)
    return dir_list



def choose_datasets(source_path):
    global path_1
    global path_2
    print('''Which datasets would you like to compare?
              Press number of index for dataset 1 first,
              followed by index for dataset 2.''')
    dir_list = print_and_return_all_files_innumerated(source_path)
    path_1 = "./Drew_folder/Drew_Data/" + dir_list[int(input())]
    path_2 = "./Drew_folder/Drew_Data/" + dir_list[int(input())]
    return path_1, path_2

def print_paths():
    print("The paths are: ")
    print("Path 1: " + path_1)
    print("Path 2: " + path_2)


def create_and_print_dataframes():
    global path_1
    global path_2
    global df_1
    global df_2

    df_1 = pd.read_csv(path_1)
    df_2 = pd.read_csv(path_2)

    print("The Dataframes are: ")
    print(df_1)
    print(df_2)



def create_column_names_from_dataframes():
    global df_1
    global df_2
    global column_names_list_1
    global column_names_list_2

    column_names_list_1 = list(df_1.columns.tolist())
    column_names_list_2 = list(df_2.columns.tolist())

    return column_names_list_1, column_names_list_2



def choose_column_names_to_analyze():
    global column_names_list_1
    global column_names_list_2
    global column_1
    global column_1_1
    global column_2
    global column_2_2

    create_column_names_from_dataframes()

    print("The options for the first dataframe are: \n")
    for name in column_names_list_1:
        print(str(column_names_list_1.index(name)) + "- " + name)
    print("\n")
    column_1 = input("Which column would you like to (specific join) in table 1? ")
    column_1_1 = input("Which column would you like to (specific join) in table 1? ")
    print("The options for the second dataframe are: \n")
    for name in column_names_list_2:
        print(str(column_names_list_2.index(name)) + "- " + name)
    print("\n")
    column_2 = input("Which first column would you like to join in table 2? ")
    column_2_2 = input("Which second column would you like to join in table 2? ")
    return column_1, column_1_1, column_2, column_2_2


def print_column_names_to_analyze_lists():
    global column_names_list_1
    global column_names_list_2

    print("The columns in dataframe 1 are: \n")
    for name in column_names_list_1:
        print(str(column_names_list_1.index(name)) + "- " + name)

    print("\n")

    print("The columns in dataframe 2 are: \n")
    for name in column_names_list_2:
        print(str(column_names_list_2.index(name)) + "- " + name)

    print("\n")

def print_column_names_to_analyze():
    global column_1
    global column_1_1
    global column_2
    global column_2_2

    print("The first column of dataframe 1 is: ")
    print(column_1)
    print("The second column of dataframe 1 is: ")
    print(column_1_1)
    print("The first column of dataframe 2 is: ")
    print(column_2)
    print("The second column of dataframe 2 is: ")
    print(column_2_2)
    

def OG_heatmap():
    
    # Load the first dataset
    path = 'Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States(1).csv'
    df = pd.read_csv(path)


    # Load the second dataset
    path2 = 'annual_gold_rate.csv'

    # Create the dataframe for second dataset
    df_2 = pd.read_csv(path2)

    # Rename columns
    df_2 = df_2.rename(columns={'Date': 'YEAR'})


    # Select relevant columns
    df_selected = df[['ESTIMATE', 'YEAR']]
    df_selected_2 = df_2[['YEAR', 'USD']]

    # Merge Dataframes on common columns for analysis
    merged_df = pd.merge(df, df_2, on='YEAR')
    final_df = merged_df[['ESTIMATE', 'YEAR', 'USD']]

    # Filling blank entries for continuity
    final_df.dropna()
    final_df.reindex(axis = 0)


    # print(final_df.head())  # View the first few rows
    # print(merged_df.info())  # Inspect data types and non-null counts
    # print(merged_df.describe())  # View summary statistics
    # Compute the correlation matrix
    correlation_matrix = final_df.corr()
    print(correlation_matrix)
    # Plot the heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()