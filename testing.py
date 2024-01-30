import os
import subprocess

api = "kaggle datasets download -d mlg-ulb/creditcardfraud"
path = os.getcwd()
def download_data():
    
            output_dir = (os.path.join(path,'kaggle_data')) # Use the unzip directory as the output directory
            os.makedirs(output_dir, exist_ok=True)

            download_command = api
            subprocess.run(download_command, shell=True, check=True, cwd=output_dir)  # Set the current working directory
            print("Dataset downloaded success")
            
# def unzip_data():
    

download_data()
    