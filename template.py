import logging
import os
from pathlib import Path


list_of_files=[
    '.github/.workflows/.gitkeep', # for pushing file to github
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evalutaion.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utlis/__init__.py',
    'src/utlis/utlis.py',
    'src/logger/logging.py',
    'src/exception/expection',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt', # for production
    'requirements_dev.txt', # for devlopement 
    'setup.py',
    'setup.config',
    'pyproject.toml',
    'tox.ini',
    'experiment/experminents.ipynb' 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating Directory {filedir} for file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file