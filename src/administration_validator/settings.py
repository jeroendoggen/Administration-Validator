"""
    Blackboard Grade center analyser
    A tool to analyse assignments downloaded from the Blackboard grade center
    Copyright 2013, Jeroen Doggen, jeroendoggen@gmail.com
"""

# TODO: report all students that hand in the assignment after the deadline
# TODO: ...

import os

class Settings:
    """ Contains all the tools to analyse Blackboard assignments """
    logfile = "administration_validator.log"
    script_path = os.getcwd()
    input_path = script_path
    output_path = script_path
    summary_file = 'summary.txt'  

    def __init__(self):
        pass