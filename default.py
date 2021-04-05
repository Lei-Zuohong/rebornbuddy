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
    hfile.copy_folder('ExBuddy/ExBuddy', '../Plugins/ExBuddy')
    # for file in os.listdir('ExBuddy/Assembly'):
    #     hfile.copy_file('ExBuddy/Assembly/%s' % (file), '../%s' % (file))
    hfile.rm_folder('./ExBuddy')
    os.chdir('..')

# addition botbase


def get_llamalibrary():
    os.chdir('temp')
    os.system('git clone https://github.com/nt153133/LlamaLibrary.git')
    hfile.rm_folder('LlamaLibrary/.git')
    hfile.copy_folder('./LlamaLibrary', '../BotBases/LlamaLibrary')
    hfile.rm_folder('./LlamaLibrary')
    os.chdir('..')

# addition plugin for retainer in lisbeth


def get_llamalibrary_retainer():
    os.chdir('temp')
    os.system('git clone https://github.com/nt153133/LisbethVentures.git')
    hfile.add_folder(path='../Plugins', name='LisbethVentures')
    hfile.copy_file('LisbethVentures/LisbethVentures.cs', '../Plugins/LisbethVentures/LisbethVentures.cs')
    hfile.rm_folder('./LisbethVentures')
    os.chdir('..')

# addition profile for relicweapon


def get_relicweapon():
    os.chdir('temp')
    os.system('git clone https://github.com/Angles24/ZodiacWeapons.git')
    hfile.rm_folder('ZodiacWeapons/.git')
    hfile.copy_folder('./ZodiacWeapons',
                      '../Profiles/ZodiacWeapons')
    hfile.copy_file('ZodiacWeapons/Plugins/ExTurnInGuildLeveTag.cs',
                    '../Plugins/ExBuddy/OrderBotTags/Behaviors/ExTurnInGuildLeveTag.cs')
    hfile.rm_folder('./ZodiacWeapons')
    os.chdir('..')

# addition profile


def get_sodimm():
    os.chdir('temp')
    os.system('git clone https://github.com/sodimm/RebornBuddy.git')
    hfile.copy_folder('RebornBuddy/Profiles/Sodimm',
                      '../Profiles/Sodimm')
    hfile.copy_folder('RebornBuddy/Downloads/Latest/Sparrow',
                      '../Plugins/Sparrow')
    hfile.rm_folder('./RebornBuddy')
    os.chdir('..')

# addition profile


def get_y2krazy():
    os.chdir('temp')
    os.system('git clone https://github.com/y2krazy/Rebornbuddy-Profiles.git')
    hfile.rm_folder('Rebornbuddy-Profiles/.git')
    hfile.copy_folder('./Rebornbuddy-Profiles',
                      '../Profiles/y2krazy')
    hfile.rm_folder('./Rebornbuddy-Profiles')
    os.chdir('..')

# addition profile for lv.70-80


def get_rbtrust():
    os.chdir('temp')
    os.system('git clone https://github.com/athlon18/RBtrust.git')
    for file in os.listdir('RBtrust/Quest Behaviors'):
        hfile.copy_file('RBtrust/Quest Behaviors/%s' % (file),
                        '../Quest Behaviors/%s' % (file))
    hfile.copy_folder('RBtrust/Plugins/Trust',
                      '../Plugins/Trust')
    os.mkdir('../Profiles/Trust')
    for file in os.listdir('RBtrust'):
        if(re.match(r'(.*)全自动(.*)', file)):
            hfile.copy_file('RBtrust/%s' % (file),
                            '../Profiles/Trust/%s' % (file))
    hfile.rm_folder('./RBtrust')
    os.chdir('..')
