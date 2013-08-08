# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:54:05 2013

@author: testa
"""

#!/usr/bin/python
import subprocess
import sys
import time
import re
import web
import os
import string
sys.path.insert(0, 'lib')
import pyomxplayer
import osonsql



def playlistmake():
        global outputlist
        global play_list
        global omxinfo
        itemlist = []
        path=''
        if path.startswith('..'):
            path = ''
        for item in os.listdir(os.path.join(MEDIA_RDIR,path)):
            if os.path.isfile(os.path.join(MEDIA_RDIR,path,item)):
                fname = os.path.splitext(item)[0]
                fname = re.sub('[^a-zA-Z0-9\[\]\(\)\{\}]+',' ',fname)
                fname = re.sub('\s+',' ',fname)
                fname = string.capwords(fname.strip())
                singletuple = (os.path.join(path,item),fname,'file')
            else:
                fname = re.sub('[^a-zA-Z0-9\']+',' ',item)
                fname = re.sub('\s+',' ',fname)
                fname = string.capwords(fname.strip())
                singletuple = (os.path.join(path,item),fname,'dir')
            itemlist.append(singletuple)
        itemlist = [f for f in itemlist if not os.path.split(f[0])[1].startswith('.')]
        itemlist = [f for f in itemlist if os.path.splitext(f[0])[1].lower() in PLAYABLE_TYPES or f[2]=='dir']
        list.sort(itemlist, key=lambda alpha: alpha[1])
        list.sort(itemlist, key=lambda dirs: dirs[2])
        outputlist=[]
        play_list['toplist'] = []
        for line in itemlist:
            jsonbdbcon = jsonbsql.connect("sqlite", "db/full.db")
            sqlqname = ['acc']
            sqlqeq = [' = ']
            sqlqvalue = [posti.acc]
            sqlqxor = ['AND']
            aoute = jsonbsql.select("sqlite", jsonbdbcon, "passwd", sqlqname, sqlqeq, sqlqvalue, sqlqxor)
            try:
              thevariable
            except NameError:
               print "well, it WASN'T defined after all!"
            else:
               print "sure, it was defined."
            if line[1] not in play_list['filename']:
                play_list['toplist'].append(str(len(play_list['id'])))
                play_list['id'].append(str(len(play_list['id'])))
                play_list['path'].append(line[0])
                play_list['filename'].append(line[1])
                play_list['format'].append(line[2])
                omxinfo =  pyomxplayer.OMXPlayerinfo(os.path.join(MEDIA_RDIR,re.escape(line[0])))
                play_list['length'].append(omxinfo.movielength)
            else:
                play_list['toplist'].append(str(play_list['filename'].index(line[1])))
            outputlist.append('{\"id\":\"'+str(play_list['filename'].index(line[1]))+'\",\"modul\":\"playlist\",\"path\":\"'+line[0]+'\", \"nam\":\"'+line[1]+'\", \"type\":\"'+line[2]+'\", \"lengt\":\"'+str(play_list['length'][play_list['filename'].index(line[1])])+'\"}')



def playlistread():
    sqlqname = ['acc']
    sqlqeq = [' = ']
    sqlqvalue = [posti.acc]
    sqlqxor = ['AND']
    passc = jsonbsql.select("sqlite", jsonbdbcon, "passwd", sqlqname, sqlqeq, sqlqvalue, sqlqxor)