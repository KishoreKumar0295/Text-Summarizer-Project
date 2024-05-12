import os
from pathlib import Path # There is a difference bitween the files paths in Windos or Mac Or linux so we are using this library
import logging

#Below it will be used for the logging information with time and msg
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

#Here we are going to implement the project Structure
project_name="TextSummarizer"
list_of_files=[
    '.github/workflows/.gitkeep/',
    f'src/{project_name}/__init__.py',# __init__ it will work as constructor it will make this folder as a local package, when we want to import this files and packages 
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config//configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'param.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirement.txt',
    'setup.py',
    'research/trials.ipynb'

]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath) # it will create automatically folders and subfolders

    if filedir !="": # if the folder is not empty then it will create otherwise it won't create
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating derectory:{filedir} for the file {filename}")
    

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f: # here we are opening the file in write mode
            pass
            logging.info(f"Creating empty file: {filepath}")
    

    else:
        logging.info(f"{filename} is already exists")
