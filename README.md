# confs-example

Simple example and play-ground for trying out and testing configuration systems based on
the following formats:

1. Python files
2. *.INI configuration files
3. *.Json configuration files
4. *.YAML configuration files

Exercise
========

Start by looking and the code and try running the `run.py` script to get 
familiar with the configuration and how the information gets read from the files. 

**Task**

1. Once you feel quite confident about the code, try to add a new parameter to the 
   configurations. In particular, we want to be able to customize the Mongo database name 
   via configuration files. Do the needed implementation for the different types of 
   configurations in order to include this extra parameter.

2. When you feel at ease with adding new keys to the configuration files, try to 
   increase a bit complexity by adding new sections (when possible). 
   In order to do so, imagine that  in the model specification you want to add two subsections: 
   - training, where to specify the path for saving trained models
   - prediction, where to specify the path of the model to be used in prediction steps