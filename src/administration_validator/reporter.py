﻿"""
    Administration Validator
    Copyright 2013, Jeroen Doggen, jeroendoggen@gmail.com
"""

from __future__ import print_function, division  # We require Python 2.6+

import os

class Reporter():
    """ Logging class """

    def __init__(self, settings):
        self.settings = settings

    def run(self):
        """ Write statistics to files """
        self.write_summary()

     
    def write_summary(self):
        """ Write a summary of the analysis process to a logfile """
        try:
            os.chdir(self.settings.output_path)
            outfile = open(self.settings.summary_file, 'w+')
            outfile.write("Build summary:\n")
            outfile.write("--------------\n")
            outfile.write(" Total exams: ")
            outfile.write("\n Total slides: ")
            outfile.write("\n Total courses: ")
            outfile.write("\n Missing files: ")
            outfile.write("\n Bad filenames: \n")
            outfile.close()
            with open(self.settings.summary_file) as f:
                content = f.read()
                print(content)
            outfile.close()
        except OSError:
            self.exit_program("writing the summary")
     
    def exit_program(self, message):
        """ Exit the program with a message
           TODO: this should move somewhere else (needed in multiple places)
        """
        print("Error while " + message)
        print("Closing application")
        sys.exit()