#!/usr/bin/env python3
import fileinput
from pathlib import Path
import os
import colorama
from colorama import Fore, Back, Style 
from __main__ import *;
########################
# Edit only what is in this comment block
#
# STEP 1:
# Download and install Bakkesmod
#
# STEP 2: Your rocket league folder. 
#   • To find it:
#      Steam Library -> Right click Rocket League -> 
#      Local Files tab -> Browse Local Files...
#   • Copy and paste that directory here: (keep the r before the quote)
#
rocket_league_folder = r"D:\SteamLibrary\steamapps\common\rocketleague"
# 
# STEP 3: Your plugin name.
#   • Replace the name below with your plugin name (No Spaces!!)
#
plugin_name = "MyAwesomePlugin"
#
# STEP 4: Your python path
#   • This is the thing you type in a command prompt to run python
#      (usually just "python" without the quotes)
#
python_command = "python"
#
# STEP 5: Alternate Bakkesmodsdk Directory(optional)
#   • If you'd like your bakkesmod plugin to refer to an alternate
#      sdk directory, put it between the quotes below:
#   • The path should point to the folder with "include" and "lib" folders
#
alternate_bakkesmod_sdk_directory = ""
#######################

colorama.init()
class BlueprintProperties:
    def __init__(self, project_name, rocketleague_folder, bakkesmod_sdk_directory):
        self.name = project_name
        self.sdk_dir = bakkesmod_sdk_directory
        self.rl_dir = rocketleague_folder
    
class PluginProperties:
    def __init__(self, plugin_name, rocketleague_folder, bakkesmod_sdk_directory):
        self.name = plugin_name
        self.sdk_dir = bakkesmod_sdk_directory
        self.rl_dir = rocketleague_folder

def replace_all_occurrances_in_files(root_path, file_list, 
                                     text_to_search, replacement_text):
    print ("Replacing in " + str(len(file_list)) + " files.")
    num_of_changes = 0
    num_of_files_changed = 0

    for index in range(len(file_list)):
        if (file_list[index].is_file()):
            num_of_files_changed += 1
            print("Working on " + str(file_list[index]))
            with fileinput.FileInput(file_list[index], inplace=True) as file:
                for line in file:
                    num_of_changes += line.count(text_to_search)
                    print(line.replace(text_to_search, replacement_text), end='')
        else:
            error_list.append("Unable to locate file: " + str(file_list[index]))
    print(Fore.GREEN + str(num_of_changes) +  " changes made in " + str(num_of_files_changed) + " files.")
    print(Style.RESET_ALL) 

def replace_in_file(root_path, file_name, text_to_search, text_to_replace):
    num_of_changes = 0
    num_of_files_changed = 0
    path_to_file = root_path.joinpath(file_name)
    if (path_to_file.is_file()):
        num_of_files_changed += 1
        with fileinput.FileInput(path_to_file, inplace=True) as file:
            for line in file:
                num_of_changes += line.count(text_to_search)
                print(line.replace(text_to_search, replacement_text), end='')
    else:
        error_list.append("Unable to locate file: " + str(path_to_file))
    print(Fore.GREEN + str(num_of_changes) +  " changes made in " + str(num_of_files_changed) + " files.")
    print(Style.RESET_ALL) 

error_list = []
data_folder = Path(os.getcwd())
bakkes_patch_plugin_name = "bakkes_patchplugin.py"
pp = PluginProperties(plugin_name, rocket_league_folder, alternate_bakkesmod_sdk_directory)
bp = BlueprintProperties("SpeedometerPlugin", "D:\\SteamLibrary\\steamapps\\common\\rocketleague", r"C:\Users\Caleb\VisualStudioProjects\BakkesModSDK")
files_to_replace = [data_folder.joinpath(bp.name).joinpath(bp.name + ".sln"), 
                    data_folder.joinpath(bp.name).joinpath(bp.name).
                    joinpath(bp.name + ".cpp"),
                    data_folder.joinpath(bp.name).joinpath(bp.name).
                    joinpath(bp.name + ".h"),
                    data_folder.joinpath(bp.name).joinpath(bp.name).
                    joinpath(bp.name + ".vcxproj"),
                    data_folder.joinpath(bp.name).joinpath(bp.name).
                    joinpath(bp.name + ".vcxproj.filters")]

#replace_all_occurrances_in_files(data_folder, files_to_replace, bp.name, pp.name)
replace_in_file_(bakkes_patch_script_path, bakkes_patch_plugin_name, bp.sdk_dir, pp.sdk_dir)
if (len(error_list) > 0):
    print(Back.WHITE + Fore.RED + "\nThe operation completed with errors:");
    for index in range(len(error_list)):
        print (Fore.RED + error_list[index])
    print(Style.RESET_ALL)    