import signac
import os
from subprocess import call
def write_inp(N,L,T,fileout="iodine.py"):
        file = """

from cssi_cp2k.classes import SIM as sim

mySim = sim.SIM()

mySim.GLOBAL.RUN_TYPE = "MD"
mySim.GLOBAL.PROJECT  = "iodine-liquid"
mySim.GLOBAL.IO_LEVEL = "LOW"


#FORCE EVAL SECTION
mySim.FORCE_EVAL.METHOD='QUICKSTEP'
mySim.FORCE_EVAL.STRESS_TENSOR='ANALYTICAL';

mySim.FORCE_EVAL.DFT.BASIS_SET_FILE_NAME='/home/siepmann/singh891/cp2k-6.1.0/data/BASIS_MOLOPT'
mySim.FORCE_EVAL.DFT.POTENTIAL_FILE_NAME='/home/siepmann/singh891/cp2k-6.1.0/data/GTH_POTENTIALS'
mySim.FORCE_EVAL.DFT.CHARGE=0
mySim.FORCE_EVAL.DFT.MULTIPLICITY=1
mySim.FORCE_EVAL.DFT.MGRID.CUTOFF=600
mySim.FORCE_EVAL.DFT.MGRID.REL_CUTOFF=60
mySim.FORCE_EVAL.DFT.MGRID.NGRIDS=4
mySim.FORCE_EVAL.DFT.QS.METHOD='GPW'
mySim.FORCE_EVAL.DFT.QS.EPS_DEFAULT=1E-10
mySim.FORCE_EVAL.DFT.QS.EXTRAPOLATION='ASPC'
mySim.FORCE_EVAL.DFT.POISSON.PERIODIC="XYZ"
mySim.FORCE_EVAL.DFT.PRINT.E_DENSITY_CUBE.SECTION_PARAMETERS="OFF"
mySim.FORCE_EVAL.DFT.SCF.SCF_GUESS='ATOMIC'
mySim.FORCE_EVAL.DFT.SCF.MAX_SCF=30
mySim.FORCE_EVAL.DFT.SCF.EPS_SCF=1E-6

mySim.FORCE_EVAL.DFT.SCF.OT.SECTION_PARAMETERS=".TRUE."
mySim.FORCE_EVAL.DFT.SCF.OT.PRECONDITIONER="FULL_SINGLE_INVERSE"
mySim.FORCE_EVAL.DFT.SCF.OT.MINIMIZER="DIIS"
mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.SECTION_PARAMETERS='.TRUE.'

mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.MAX_SCF=10
mySim.FORCE_EVAL.DFT.SCF.OUTER_SCF.EPS_SCF=1e-6
mySim.FORCE_EVAL.DFT.SCF.PRINT.RESTART.SECTION_PARAMETERS='OFF'
mySim.FORCE_EVAL.DFT.SCF.PRINT.DM_RESTART_WRITE='.TRUE.'

mySim.FORCE_EVAL.DFT.XC.XC_FUNCTIONAL.SECTION_PARAMETERS='BLYP'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.POTENTIAL_TYPE='PAIR_POTENTIAL'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.TYPE='DFTD3'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.PARAMETER_FILE_NAME='dftd3.dat'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.REFERENCE_FUNCTIONAL='BLYP'
mySim.FORCE_EVAL.DFT.XC.VDW_POTENTIAL.PAIR_POTENTIAL.R_CUTOFF=11

mySim.FORCE_EVAL.SUBSYS.init_atoms(1);
mySim.FORCE_EVAL.SUBSYS.KIND[1].SECTION_PARAMETERS='I';

mySim.FORCE_EVAL.SUBSYS.COORD.DEFAULT_KEYWORD='iodine.xyz'
mySim.FORCE_EVAL.SUBSYS.KIND[1].SECTION_PARAMETERS='I'
mySim.FORCE_EVAL.SUBSYS.KIND[1].BASIS_SET='DZVP-MOLOPT-SR-GTH'
mySim.FORCE_EVAL.SUBSYS.KIND[1].POTENTIAL='GTH-BLYP-q7'
mySim.FORCE_EVAL.SUBSYS.CELL.ABC='{} {} {}'

#MOTION SECTION
mySim.MOTION.GEO_OPT.OPTIMIZER='BFGS'
mySim.MOTION.GEO_OPT.MAX_ITER=100
mySim.MOTION.GEO_OPT.MAX_DR=0.003


mySim.MOTION.MD.ENSEMBLE = "NVT"
mySim.MOTION.MD.STEPS  = 1000000
mySim.MOTION.MD.TIMESTEP = 0.5
mySim.MOTION.MD.TEMPERATURE = {}
mySim.MOTION.MD.THERMOSTAT.TYPE = "NOSE"
mySim.MOTION.MD.THERMOSTAT.REGION = "MASSIVE"
mySim.MOTION.MD.THERMOSTAT.NOSE.LENGTH = 3
mySim.MOTION.MD.THERMOSTAT.NOSE.YOSHIDA = 3
mySim.MOTION.MD.THERMOSTAT.NOSE.TIMECON = 1000.0
mySim.MOTION.MD.THERMOSTAT.NOSE.MTS = 2


#mySim.MOTION.MD.PRINT.ENERGY.EACH.MD = 20
#mySim.MOTION.MD.PRINT.PROGRAM_RUN_INFO.EACH.MD = 20
#mySim.MOTION.MD.AVERAGES.SECTION_PARAMETERS= ".falbmbjse."


mySim.MOTION.PRINT.STRESS.SECTION_PARAMETERS='ON'
mySim.MOTION.PRINT.TRAJECTORY.EACH.MD=10
mySim.MOTION.PRINT.VELOCITIES.SECTION_PARAMETERS='OFF'
mySim.MOTION.PRINT.FORCES.SECTION_PARAMETERS="OFF"
mySim.MOTION.PRINT.RESTART_HISTORY.SECTION_PARAMETERS="ON"
mySim.MOTION.PRINT.RESTART_HISTORY.EACH.MD=500
mySim.MOTION.PRINT.RESTART.SECTION_PARAMETERS="ON"
mySim.MOTION.PRINT.RESTART.BACKUP_COPIES=3
mySim.MOTION.PRINT.RESTART.EACH.MD=1

mySim.write_changeLog(fn="iodine-changeLog.out")
mySim.write_errorLog()
mySim.write_inputFile(fn="md.inp")


""".format(L,L,L,T)

        with open(fileout,"w") as out:
                out.write(file)


proj = signac.get_project()

def write_job_inp(job):

    # State point values stored as: Temp
        T = job.statepoint()['Temp']
        N = job.statepoint()['N']
        L = 10*job.statepoint()['L']
        #print(type(N))

        write_inp(N,L,T,fileout=job.fn("iodine.py"))
        #import box.py
        #python box.py



for job in proj:
        write_job_inp(job)



for job in proj:
        home  = job.workspace()
        print("HOME: {}".format(home))
        os.chdir(home)
        call(["python", "iodine.py"])
