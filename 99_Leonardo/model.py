import pandas as pd

#Read the model.csv file
model =pd.read_csv('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\99_Leonardo\\00_Datasets\\data_model.csv',sep=';')

print('Dataframe details-----------------------------------------------------------------------------')
print(model.info()) 

#show all the data
print('Origianl data-------------------------------------------------------------------------------')
print(model.to_string())

#Remove Columns Trash
print("Print the new dataset without Trash Column---------------------------------------------------")
model = model.drop(columns="Trash")
print(model.to_string())

#Remove Rows that contain NaN values
print("Print the new dataset without NaN rows in columns ID-----------------------------------------")
model = model.dropna(subset=['ID', 'Type'])
print(model.to_string())

#Removing duplciated rows drom this dataframes
model.drop_duplicates(inplace = True)
print("Print the new dataset without duplicated rows-----------------------------------------------")
print(model.to_string())

#Remove the row that contains Model 4 in color column
model = model[model['Color'].str.contains("Model") == False]
print("Remove the row that contains Model 4 in color column-----------------------------------------------")
print(model.to_string())

#Replacing , to .
model['Price'] = model['Price'].str.replace(',','.')
print("Replacing , to .-------------------------------------------------")
print(model.to_string())

#Convert column Price from string to Decimal
model['Price'] = pd.to_numeric(model['Price'],errors='coerce')
print("Convert column Price from string to Decimal-------------------------------------------------")
print(model.to_string())

#Replace Non Numerical values in column Price
model.Price =pd.to_numeric(model.Price, errors ='coerce').fillna(0).astype('float')
print("Print the new dataset without duplicated rows-----------------------------------------------")
print(model.to_string())

#Renaming column Data to Date
mode = model.rename(columns = {'Data':'Date'}, inplace = True)
print("Renaming column Data to Date-----------------------------------------------")
print(model.to_string())

print('Dataframe details-----------------------------------------------------------------------------')
print(model.info()) 

#Converting string to date in Column Data
model['Date'] = model['Date'].astype('datetime64[ns]')
print("Converting string to date in Column Date-----------------------------------------------")
print(model.to_string())

print('Dataframe details-----------------------------------------------------------------------------')
print(model.info()) 
