from mentalmodel import mentalIllnessData
from swiftmodel import swiftData
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

def csvRead(path, selection):
    try:
        with open(path, "r", errors='ignore', encoding='utf-8') as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            entries_list = []
            # skips header
            next(csvFile)
            if selection == 1:
                for lines in csvFile:
                    entry = mentalIllnessData(*lines)
                    entries_list.append(entry)
            if selection == 2:
                for lines in csvFile:
                    entry = swiftData(*lines)
                    entries_list.append(entry)
                    
        return entries_list
    except FileNotFoundError:
        print("File Not Found. Please check file's existence or its path again.")       
        
def main():

#step 1
#clean mental health data to prevalence of depression and year
#make dataset 1
#plot dataset 1 graph

    path = "./mentalillnessdata.csv"
    entry_List = csvRead(path, 1)
    with open("mentalIllCleaned.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['Country', 'Year', 'Depressive']
        writer.writerow(header)
        for entry in entry_List:
            if entry.Entity == "United States" and int(entry.Year)>2007:
                writer.writerow([entry.Entity, entry.Year, entry.Depressive])
    df = pd.read_csv("mentalIllCleaned.csv")
    plt.title("Depression DALA By Year")
    plt.xlabel("Year")
    plt.ylabel("Years of life lost due to depression")
    plt.scatter(df['Year'], df['Depressive'])
    plt.savefig("depressionDALA.png")    

#step 2. clean taylor swift data to year and views columns
#this data should show her poularity by year
#make dataset 2
#plot dataset 2 graph

    path = "./taylor_swift_videos.csv"
    entry_List = csvRead(path, 2)
    years = []
    totals = []
    for entry in entry_List:
        thisEntry = entry.Published[0:4]
        if thisEntry not in years and int(thisEntry)>2007 and int(thisEntry)<2020:
            years.append(thisEntry)
    for year in years:
        totals.append(0)
    for entry in entry_List:
        thisEntry = entry.Published[0:4]
        i=0
        for year in years:
            if thisEntry==year:
                totals[i]=totals[i]+entry.View_Count
            else:
                i=i+1
    with open("swiftDataClean.csv", 'w', errors='ignore',encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        header = ['Year', 'Video Views']
        writer.writerow(header)
        for i in range(len(totals)):
            writer.writerow([years[i], totals[i]])
    df_2 = pd.read_csv("swiftDataClean.csv")
    plt.clf()
    plt.title("Taylor Swift popularity (as indicated by video views)")
    plt.xlabel("Year")
    plt.ylabel("Taylor Swift Video Views")
    plt.scatter(df_2['Year'], df_2['Video Views'])
    plt.savefig("TaylorSwiftChart.png")      

#step 3. merge datasets one and two
#make dataset 3
#plot dataset 3
#print and heatmap correlation
    plt.clf()
    
    # Select relevant columns
    df_selected = df[['Year', 'Depressive']]
    df_selected_2 = df_2[['Year', 'Video Views']]
    merged_df = pd.merge(df, df_2, on='Year')
    final_df = merged_df[['Year', 'Depressive', 'Video Views']]
    
    final_df.dropna()
    final_df.reindex(axis = 0)
    
    correlation_matrix = final_df.corr()
    print(correlation_matrix)
    
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Taylor Swift and Mental Depression Correlation Heatmap")
    plt.savefig("SwiftDepressionHeatMap.png")

    plt.clf()
    plt.scatter(final_df['Depressive'], final_df['Video Views'])
    plt.savefig("SwiftDepressionGraph.png")
    
main()