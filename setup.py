import os
import numpy  as np
import pandas as pd
from pandasql import sqldf

# Location of the data and the data files
data_dir = './data'
user_data_file = os.path.join(data_dir, 'sample_user_info.csv')
campaign_data_file = os.path.join(data_dir, 'sample_campaign_info.csv') 
delivery_data_file = os.path.join(data_dir, 'sample_delivery_info.csv') 

# Load the data sets
delivery_info = pd.read_csv(delivery_data_file)


query = "select count(*) from delivery_info"
print(sqldf(query))

# Load the user info
user_info = pd.read_csv(user_data_file)
query = "select count(*) as nusers from user_info"
print(sqldf(query))

# Load the campaign data 
campaign_info = pd.read_csv(campaign_data_file)
query = "select count(*) as ncampaign from campaign_info"
print(sqldf(query))

# Test arrays
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,0,0], [0,1,0],[1,1,1]])
