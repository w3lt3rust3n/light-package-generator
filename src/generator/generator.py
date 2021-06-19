import os
from sh import mkdir
import subprocess
# from posixpath import dirname

# \033[32m -> Green
# \033[31m -> Red

class Generator:
    SCRIPTS_DIR = ".lpg/scripts"

    def __init__(self, lang, path):
        self.lang = lang
        self.path = path

    def __launch_script(self):
        project_name = input("Set a project name : ")       
        home = os.getenv("HOME")
        script_path = home + "/" + self.SCRIPTS_DIR + "/lpg-" + self.lang + "-init.sh"
       
        print("Attempting to launch script at {}".format(script_path))

        try:
            subprocess.call([script_path, self.path, project_name])
        except subprocess.CalledProcessError:
            print("Error while executing script, no file !")

    def project_generator(self):
        print("Check if directory exists...")
        if os.path.exists(self.path):
            print("\033[32mYes\033[0m")
            Generator.__launch_script(self)
        else:
            print("\033[31mNo\033[0m")
            print("Creating project directory... ")
            try:
                mkdir(self.path)
            except mkdir.ErrorReturnCode_2:
                print("Error while creating project directory")
            
            if os.path.exists(self.path):
                print("\033[32mSuccess\033[0m")
                Generator.__launch_script(self)
            else:
                print("\033[31mNo\033[0m")
                print("Error, exiting program")
                return False
            