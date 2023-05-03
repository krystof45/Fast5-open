import numpy as np
from scipy import sparse as sp
import h5py
from os import *
import fnmatch

sciezka='C:\\Users\\kryst\\Desktop\\test\\'
fasty=[x for x in listdir(r'%s'%(sciezka))if \

fnmatch.fnmatch(x,'*.fast5')]

seq_w_plikach=[]
for n in fasty:
    f = h5py.File('%s%s'%(sciezka,n),'r')

    seq_w_pliku=[]
    
    seq_2D=f.get('Analyses/Basecall_2D_000/BaseCalled_2D/Fastq')
    seq_1D_complement=f.get('Analyses/Basecall_1D_000/BaseCalled_complement/Fastq')
    seq_1D_template=f.get('Analyses/Basecall_1D_000/BaseCalled_template/Fastq')
    
    seq_2D = np.array(seq_2D)
    seq_1D_complement=np.array(seq_1D_complement)
    seq_1D_template=np.array(seq_1D_template)
    '''
    seq_2D_list=[]
    seq_2D_list.append(seq_2D)
    seq_1D_complement_list=[]
    seq_1D_complement_list.append(seq_1D_complement)
    seq_1D_template_list=[]
    seq_1D_template_list.append(seq_1D_template)
    
    new=[]
    new=str(seq_2D_list[0]).split('\n')
    print(new)

    '''
    seq_w_pliku.append( seq_2D)
    seq_w_pliku.append(seq_1D_complement)
    seq_w_pliku.append(seq_1D_template)
    
    
    
    print(seq_w_pliku)
    seq_w_plikach.append(seq_w_pliku)
    '''
    o=open('C:\\Users\\Właściciel\\Desktop\\prakt\\list.txt',87)
    o.write(seq_w_pliku)
    o.close
    '''
    
f.visit(print)
print(seq_w_pliku)


#print(f.keys())







'''
for x in b :
    print(x)
    f.get(x)

f.visititems(lambda name,obj:print(name, obj))
f.visit(print)  # to see its structure
'''

