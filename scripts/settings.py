# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:04:54 2019

@author: randerson
"""

from pathlib import Path, PurePosixPath

NR_PROCESSORS = 12

LOCAL_ROOT     = Path('U:/simulation')
LOCAL_IMEX_EXE = Path('C:/\"Program Files (x86)"/CMG/IMEX/2017.10/Win_x64/EXE/mx201710.exe')
LOCAL_REPO_EXE = Path('C:/\"Program Files (x86)"/CMG/BR/2017.10/Win_x64/EXE/report.exe')
LOCAL_PUTT_EXE = Path('C:/\"Program Files (x86)"/PuTTY/plink.exe')

REMOTE_ROOT     = PurePosixPath('/home/randerson/simulation')
REMOTE_IMEX_EXE = PurePosixPath('/mnt/software/CMG/imex/2017.10/linux_x64/exe/mx201710.exe')

SIMS_FOLDER = Path('SIMS')

DAT_ROOT = Path('U:/simulation')
DAT_FOLDER = Path('dat')
DAT_NAME = Path('main.dat')

RWD_ROOT = Path('U:/simulation')
RWD_FOLDER = Path('rwd')
RWD_NAME = Path('main.rwd')

IRF_ROOT = Path('U:/simulation')
IRF_FOLDER = Path('rwd')
IRF_NAME = Path('main.irf')

REP_ROOT = Path('U:/simulation')
REP_NAME = Path('main.rep')

INF_ROOT = Path('U:/simulation')
INF_NAME = Path('main.inf')

NPV_ROOT = Path('U:/simulation')
NPV_NAME = Path('main.eofcs.csv')

CSV_ROOT = Path('U:/simulation')
CSV_FOLD = Path('csvs')

USER = 'randerson'
CLUSTER_NAME = 'hpc02'
QUEUE_KIND = 'longas'
