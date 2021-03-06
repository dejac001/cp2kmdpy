# Deleting files that we do not need, files generated from a previous run
import os
import glob

extension_list=["*inp*","*out","*ener","*rest*","*Hess*","*REST*","*.xyz","*.pdb"]
for name in extension_list:
    
    filelist=glob.glob(name)
    for file in filelist:
        os.remove(file)


# ### Loading modules
import numpy as np
import unyt as u
import mbuild as mb
from cp2kmdpy.molecule_optimization import Molecule_optimization # for single molecule optimization
from cp2kmdpy.md import MD # for running MD
from cp2kmdpy import runners
import setter


#Defining the molecule we want to simulate

class O2(mb.Compound): # this class builds an oxygen molecule with a bond-length given in the oxygen2 x coor (nm)
    def __init__(self):
        super(O2, self).__init__()
        
        oxygen1= mb.Particle(pos=[0.0, 0.0, 0.0], name='O')
        oxygen2= mb.Particle(pos=[0.15, 0.0, 0.0], name='O')
        self.add([oxygen2,oxygen1])
        self.add_bond((oxygen2,oxygen1))


class N2(mb.Compound): 
    def __init__(self):
        super(N2, self).__init__()

        nitrogen1= mb.Particle(pos=[0.0, 0.0, 0.0], name='N')
        nitrogen2= mb.Particle(pos=[0.2, 0.0, 0.0], name='N')
        self.add([nitrogen2,nitrogen1])
        self.add_bond((nitrogen2,nitrogen1))

#creating an instance of the MD class, also defining the parametrs of our md simulation
molecule_list=[O2(),N2()]
box=mb.box.Box(lengths=[1,1,1])
q=MD(molecules=molecule_list,box=box,cutoff=200,functional='PBE',basis_set={'O':'DZVP-MOLOPT-GTH','N':'DZVP-MOLOPT-GTH'},periodicity='XYZ',n_molecules=[2,2],traj_type='PDB',seed=1,project_name='O2_N2_mix')


#Setting temperature and ensemble, could have also been set while creating an instance of the MD class

q.temperature=273.15*u.K
q.ensemble='NVT'
q.simulation_time=10*u.fs
#Initializing q
q.md_initialization()


#generating input files
setter.md_files(q)


#running md
runners.run_md(q.input_filename,q.output_filename )


