# -*- coding: UTF-8 -*-
# Public package
import os
import re
# Private package
import headpy.hfile as hfile

# base plugins


def get_exbuddy():
    os.chdir('temp')
    os.system('git clone https://github.com/Entrax643/ExBuddy.git')
    hfile.copy_folder(source_path='ExBuddy',
                      source_name='ExBuddy',
                      path='../Plugins',
                      name='ExBuddy')
    for file in os.listdir('ExBuddy/Assembly'):
        hfile.copy_file(source_path='ExBuddy/Assembly',
                        source_name=file,
                        path='..',
                        name=file)
    hfile.rm_folder(path='.',
                    name='ExBuddy')
    os.chdir('..')

# addition botbase


def get_llamalibrary():
    os.chdir('temp')
    os.system('git clone https://github.com/nt153133/LlamaLibrary.git')
    hfile.rm_folder('LlamaLibrary/.git')
    hfile.copy_folder('./LlamaLibrary',
                      '../BotBases/LlamaLibrary')
    hfile.rm_folder('./LlamaLibrary')
    os.chdir('..')

# addition plugin for retainer in lisbeth


def get_llamalibrary_retainer():
    os.chdir('temp')
    os.system('git clone https://github.com/nt153133/LisbethVentures.git')
    os.mkdir('../Plugins/LisbethVentures')
    hfile.copy_file(source_path='LisbethVentures',
                    source_name='LisbethVentures.cs',
                    path='../Plugins/LisbethVentures',
                    name='LisbethVentures.cs')
    hfile.rm_folder(path='.',
                    name='LisbethVentures')
    os.chdir('..')

# addition profile for relicweapon


def get_relicweapon():
    os.chdir('temp')
    os.system('git clone https://github.com/Angles24/ZodiacWeapons.git')
    hfile.rm_folder(path='ZodiacWeapons',
                    name='.git')
    hfile.copy_folder(source_path='.',
                      source_name='ZodiacWeapons',
                      path='../Profiles',
                      name='ZodiacWeapons')
    hfile.copy_file(source_path='ZodiacWeapons/Plugins',
                    source_name='ExTurnInGuildLeveTag.cs',
                    path='../Plugins/ExBuddy/OrderBotTags/Behaviors',
                    name='ExTurnInGuildLeveTag.cs')
    hfile.rm_folder(path='.',
                    name='ZodiacWeapons')
    os.chdir('..')

# addition profile


def get_sodimm():
    os.chdir('temp')
    os.system('git clone https://github.com/sodimm/RebornBuddy.git')
    hfile.copy_folder(source_path='RebornBuddy/Profiles',
                      source_name='Sodimm',
                      path='../Profiles',
                      name='Sodimm')
    hfile.copy_folder(source_path='RebornBuddy/Downloads/Latest',
                      source_name='Sparrow',
                      path='../Plugins',
                      name='Sparrow')
    hfile.rm_folder(path='.',
                    name='RebornBuddy')
    os.chdir('..')

# addition profile


def get_y2krazy():
    os.chdir('temp')
    os.system('git clone https://github.com/y2krazy/Rebornbuddy-Profiles.git')
    hfile.rm_folder(path='Rebornbuddy-Profiles',
                    name='.git')
    hfile.copy_folder(source_path='.',
                      source_name='Rebornbuddy-Profiles',
                      path='../Profiles',
                      name='y2krazy')
    hfile.rm_folder(path='.',
                    name='Rebornbuddy-Profiles')
    os.chdir('..')

# addition profile for lv.70-80


def get_rbtrust():
    os.chdir('temp')
    os.system('git clone https://github.com/athlon18/RBtrust.git')
    for file in os.listdir('RBtrust/Quest Behaviors'):
        hfile.copy_file(source_path='RBtrust/Quest Behaviors',
                        source_name=file,
                        path='../Quest Behaviors',
                        name=file)
    hfile.copy_folder(source_path='RBtrust/Plugins',
                      source_name='Trust',
                      path='../Plugins',
                      name='Trust')
    os.mkdir('../Profiles/Trust')
    for file in os.listdir('RBtrust'):
        if(re.match(r'(.*)全自动(.*)', file)):
            hfile.copy_file(source_path='RBtrust',
                            source_name=file,
                            path='../Profiles/Trust',
                            name=file)
    hfile.rm_folder(path='.',
                    name='RBtrust')
    os.chdir('..')
