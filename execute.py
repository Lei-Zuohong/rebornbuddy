# -*- coding: UTF-8 -*-
# Public package

# Private package
import default as default
import headpy.hfile as hfile
import headpy.hscreen.hprint as hprint

args, argv = hfile.argv()
if(('h' in args) or ('H' in args) or ('help' in args)):
    hprint.pstar()
    hprint.ppoint('-h', 'Get help')
    hprint.ppoint('-a', 'Get all update')
    hprint.pstar()
    hprint.ppoint('-exbuddy', 'Get exbuddy update')
    hprint.ppoint('', 'A base plugin')
    hprint.ppoint('-llama', 'Get llamalibrary update')
    hprint.ppoint('', 'A support for relicweapon')
    hprint.ppoint('-relic', 'Get Relicweapon update')
    hprint.ppoint('', 'A AFK relic weapon profile')
    hprint.ppoint('-sodimm', 'Get sodimm update')
    hprint.ppoint('', 'A lot of profiles')
    hprint.ppoint('-y2krazy', 'Get y2krazy update')
    hprint.ppoint('', 'A lot of profiles')
    hprint.ppoint('-trust', 'Get truth update')
    hprint.ppoint('', 'A AFK 70-80 leveling')
    hprint.pstar()
    exit()

if(('a' in args) or ('exbuddy' in args)):
    default.get_exbuddy()
if(('a' in args) or ('llama' in args)):
    default.get_llamalibrary()
    default.get_llamalibrary_retainer()
if(('a' in args) or ('relic' in args)):
    default.get_relicweapon()
if(('a' in args) or ('sodimm' in args)):
    default.get_sodimm()
if(('a' in args) or ('y2krazy' in args)):
    default.get_y2krazy()
if(('a' in args) or ('trust' in args)):
    default.get_rbtrust()

hfile.rm_folder('./temp')
hfile.add_folder('.', 'temp')
