## PySettings
easy-to-use settings module for python projects

## Prerequisites
* Python 2.7

## Install
* just put PySettings folder on your package folder. 

## Usage
from you code, from PySettings import SettingsManager, and then call SettingsManager.getSettings() to have a SettingsObject instance. 
From SettingsObject you can retrieve all configurations you need. 

## Configuration
Define as examples getters in SettingsObject, according to your configuration file. 
## Configuration Optional
default path is ./settings.txt. You can call SettingsManager.getSettings("./myPersonalSettingsFileName.bla")

