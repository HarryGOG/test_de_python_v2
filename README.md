# Test de python (Version 2)

# Project information
This project propose a quick way to present a relationship between drugs, articles and new. 
In order to achieve that, we modelize a graph network representing a link between all those entity 

# Project structure
This project has 4 subpackages :

- Common : In this subpackage, we place all the common functionnalities use by all globals functions

- Job : This subpackage provide features to prepare data and create graph

- Workflow : This subpackage provide a luigi workflow to execute the global pipeline
            1. Prepare drugs data
            2. Prepare clinical trials data
            3. Prepare Pubmed data
            4. Generate the graph and save it in a json file

- Application: This sub package provide application functionalities that we can retrieve from the create graph


# Configuration
The configuration a save in config file :
- logging.cfg : Configuration for logging
- worflow.cfg : Configuration and parameter to execute the workflow


# Docs
In the docs directory we provide project documentation realize by using sphinx library 


# Discover the list of available make commands

### construct your virtual p
- list of available commands : make info

### construct your virtual environment 
- First activate python 3.7 conda environment
- make venv


# Execute tests
- make tests

# Results 
The result are save in the target directory


# Project requirements
Add all the requirement library in requirements-dev.txt file
