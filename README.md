# logging-example

Simple example and play-ground for trying out and testing logging configuration

Exercise
========

Start by looking and the code and try running the `run.py` script to get 
familiar with the kind of logs that gets generated. The logging behaviour is 
controlled using the `logging.yaml` provided. 

1. Try to change the logging level for the root logger (and/or the handler) 
   to investigate the behaviour. After playing a bit around, reset the 
   `logging.yaml` to its original form using 
   
        $ git checkout logging.yaml

   Why when you set the logging level of the handler to `DEBUG`, you don't 
   get the `DEBUG` logs as you would expect? Try to fix the file such that you 
   can get the `DEBUG` logs, as expected. 

2. Sometimes we want to increase the logging only in certain modules, 
   submodules and/or classes. In this exercise, you have to set the 
   logging.yaml file such that you only get DEBUG logs in the `stats` 
   submodules, whereas all the rest is set to INFO.
    
3. However, you soon realize that the DEBUG logs outputs too many things 
   sometimes. You therefore realize that a better choice for your need 
   would be to keep the level at INFO when things get outputted to the 
   console, while emitting the DEBUG logs (of the process module) to 
   a dedicated file.
   
4. Since the file will be processed by a dedicated tool (e.g. Logstash),
   the output in the file should conform to the following format:
   
    ` %(asctime)s - %(levelname)s - [%(name)s] - [%(module)s] - %(funcName)s() - %(message)s` 
   
    where dates follow this format
   
    ` %Y-%m-%d %H:%M:%S `