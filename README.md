# BakkesmodPluginGenerator

## Instructions

1. Clone the repo to where you want your plugin source code to be located
2. Open BakkesmodPluginGenerator.py in a text editor and edit these 4 lines (they're at the top) with your new mod configuration
```python
rocket_league_folder = r"D:\SteamLibrary\steamapps\common\rocketleague"
plugin_name = "BlueprintPlugin"
python_command = "python"
alternate_bakkesmod_sdk_directory = ""
```
3. Save your changes
4. Execute BakkesmodPluginGenerator (in command prompt or etc)
```
python bakkesmodplugingenerator.py
```
5. Delete BakkesmodPluginGenerator.py

Don't run the generator more than once. If you change your mind about your plugin configuration, delete the whole thing and start from step 1

# Credit
The bakkes_patchplugin.py file is the same as the one included in the bakkesmodsdk but I included it here so that the script won't interfere with your existing bakkesmod SDK files.
