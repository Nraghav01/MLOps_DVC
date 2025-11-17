#This is the endpoint
import os
#We can either use "python src/data_ingestion.py" command in the terminal or add the below command in the main.py endpoint file
os.system('python src/data_ingestion.py')
#Then just write "python main.py" in the terminal to execute the main.py file
#Same for data preprocessing
os.system("python src/data_preprocessing.py") #The execute the main.py by "python main.py" in terminal and the entire pipeline will be executes (ingestion + preprocessing)
os.system("python src/feature_engineering.py") #Again entire pipeline will run if we run the main.py in terminal (ingestion + preprocessing_feature_eng)

os.system("python src/model_building.py") #Again entire pipeline will run if we run the main.py in terminal (ingestion + preprocessing_feature_eng+model_building)

os.system("python src/model_evaluation.py") #Again entire pipeline will run if we run the main.py in terminal (ingestion + preprocessing_feature_eng+model_building)
