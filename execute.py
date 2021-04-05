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
    hprint.ppoint('-llamalibrary', 'Get llamalibrary update')
    hprint.ppoint('', 'A support for relicweapon')
    hprint.pstar()
    exit()

if(('a' in args) or ('exbuddy' in args)):
    default.get_exbuddy()
if(('a' in args) or ('llamalibrary' in args)):
    default.get_llamalibrary()
    default.get_llamalibrary_retainer()
# default.get_relicweapon()
# default.get_sodimm()
# default.get_y2krazy()
# default.get_rbtrust()

hfile.rm_folder('./temp')
hfile.add_folder('.', 'temp')
