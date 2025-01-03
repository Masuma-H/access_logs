"""
Project: [system check]
Author: [Masuma Begum]
Date: [12/03/24]

Interactive data analysis program for [privacy analyzer].
"""

# 2. Imports
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/CloudWatch_Traffic_Web_Attack.csv")
#print(df)


#promp the user
def start():
        while True: #loops to this until the user get exits
                print("Welcome to the Privacy Analyzer! What would you like to do?")
                print("1. View DataSet \n 2. Analyze Suspicious Activity \n 3. Visualization \n 4. Exit")

                
        
                userInput = input(' I want to (1,2,3,4): ')

                #shows the entire database
                if userInput == '1':
                        print(' ======================= Analyze DataSet ==========================')
                        #filtered_data = df[['bytes_in', 'bytes_out', 'creation_time', 'src_ip_country_code', 'protocal']]
                        #print(filtered_data)
                        print(df.describe())
                         #displays the dataset statistics
                        print('=====================================================================')
                         


                elif userInput == '2':
                        print(' ======================= Suspicious Activity ==========================')
                        print('This shows dataset with a list of data that was marked suspicious!')
                        data = {'bytes_in', 'bytes_out', 'src_ip_country_code', 'protocol'}
                        data = pd.DataFrame(data)

                        #filter data based on parameters\
                        filtered_df = df[(df['bytes_in'] > 10000) & (df['bytes_out'] > 10000)
                        & (df['src_ip_country_code'] != 'US') & (df['protocol'] == 'HTTPS')]
                        columns = filtered_df [['bytes_in', 'bytes_out', 'src_ip_country_code', 'protocol']]
                        #print(filtered_df)
                        print(columns)
                        print('=====================================================================')

                elif userInput == '3':
                
                       filtered_df = df[(df['bytes_in'] > 10000) & (df['src_ip_country_code'] != 'US')]
                       # Group data by country and sum bytes_in
                       grouped_data = filtered_df.groupby('src_ip_country_code')['bytes_in'].sum().reset_index()
                       #Plot the bar graph
                       plt.figure(figsize=(10, 6))
                       plt.bar(grouped_data['src_ip_country_code'], grouped_data['bytes_in'], color='blue')
                       plt.xlabel('Country')
                       plt.ylabel('Total Bytes Received')
                       plt.title('Bytes Received by Server from Each Country')
                       plt.xticks(rotation=45)
                       plt.tight_layout()
                       plt.show()              
                elif userInput == "4":
                        print("Exiting the program!")
                        break
        




print(start())

  