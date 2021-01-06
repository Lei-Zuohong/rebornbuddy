# -*- coding: UTF-8 -*-
# Public package
import os
# Private package
import headpy.hfile as hfile


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


def get_llamalibrary():
    os.chdir('temp')
    os.system('git clone https://github.com/nt153133/LlamaLibrary.git')
    hfile.rm_folder(path='LlamaLibrary',
                    name='.git')
    hfile.copy_folder(source_path='.',
                      source_name='LlamaLibrary',
                      path='../BotBases',
                      name='LlamaLibrary')
    hfile.rm_folder(path='.',
                    name='LlamaLibrary')
    os.chdir('..')


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
