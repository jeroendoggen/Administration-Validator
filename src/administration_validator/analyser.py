"""
    Blackboard Grade center analyser: unzipper
    A tool to analyse assignments downloaded from the Blackboard grade center
    Copyright 2013, Jeroen Doggen, jeroendoggen@gmail.com
"""

from __future__ import print_function, division  # We require Python 2.6+

from administration_validator.logger import Logger

class Analyser():
    """ Timer to check the speed of the tool itself (benchmarking) """
    txt_files_list = []
    studentnames_list = []

    def __init__(self, settings, logger, reporter):
        self.settings = settings
        self.logger = logger
        self.reporter = reporter

    def run(self):
        self.check_file("dummy filename")

    def check_file(self, filename):
        """ Check if a file exists """
        pass
