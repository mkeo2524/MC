from trcsource.trcdata import load
from trcframe.trcframeselector import trcframeselect
from fieldwork.step import FieldworkLowerLimb2SideGenerationStep
from geom.step import FieldworkGait2392GeomStep
from muscle.step import FieldworkGait2392SomsoMuscleStep
import mayavi
import os
import json

DEFAULT_MODEL_LANDMARKS = (
    'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-Sacral',
    'femur-MEC-l', 'femur-LEC-l', 
    'femur-MEC-r', 'femur-LEC-r',
    'tibiafibula-MM-l', 'tibiafibula-LM-l',
    'tibiafibula-MM-r', 'tibiafibula-LM-r',
    )

# path to trc file
path = r'C:\Users\mkeo2\Desktop\work material\server\trcs\StaticCalibration.trc'

trcData = load(path) #load trc data

trcFrame = trcframeselect(trcData, 100) #get marker coordinates for all frames

# configuration data for fieldwork
config = {}
config['identifier'] = ''
config['GUI'] = False
config['registration_mode'] = 'shapemodel'
config['pcs_to_fit'] = '1'
config['mweight'] = '0.1'
config['knee_corr'] = False
config['knee_dof'] = True
config['marker_radius'] = '5.0'
config['skin_pad'] = '5.0'
config['landmarks'] = {}
config['landmarks'] = {
    'femur-HC-l': 'LHJC',
    'femur-HC-r': 'RHJC',
    'femur-LEC-l': 'LLFC',
    'femur-LEC-r': 'RLFC',
    'femur-MEC-l': 'LMFC',
    'femur-MEC-r': 'RMFC',
    'pelvis-LASIS': 'LASI',
    'pelvis-LPSIS': 'LPSI',
    'pelvis-RASIS': 'RASI',
    'pelvis-RPSIS': 'RPSI',
    'tibiafibula-LM-l': 'LLMAL',
    'tibiafibula-LM-r': 'RLMAL',
    'tibiafibula-MM-l': 'LMMAL',
    'tibiafibula-MM-r': 'RMMAL'
}
    
fieldworkModel = FieldworkLowerLimb2SideGenerationStep(config) # initialise fieldwork class
fieldworkModel._data.inputLandmarks = trcFrame # input landmark frames
fieldworkModel.execute() # execute plugin
lowerLimb = fieldworkModel.output(2) # gias2 lower limb
fwLandmarks = fieldworkModel.output(1) #fieldwork anatomical landmarks

config = {}
config['identifier'] = ''
config['GUI'] = False
config['scale_other_bodies'] = True
config['in_unit'] = 'mm'
config['out_unit'] = 'm'
config['osim_output_dir'] = r'C:\Users\mkeo2\Desktop\work material\server\backend\geom\osim'
config['write_osim_file'] = True
config['subject_mass'] = None
config['preserve_mass_distribution'] = False
config['adj_marker_pairs'] = {}

geomModel = FieldworkGait2392GeomStep(config) #initialise geom class
geomModel.getInput(0, lowerLimb) #input gias2 lower limb
geomModel.getInput(1, 'input tracking markers')
geomModel.getInput(-1, fwLandmarks) #input gias2 landmarks
geomModel.execute() #execute plugin

geomLowerLimb = geomModel.output(-1)
osimModel = geomModel.output(3)


config = {}
config['osim_output_dir'] = r'C:\Users\mkeo2\Desktop\work material\server\backend\muscle\osim'
config['in_unit'] = 'cm'
config['out_unit'] = 'm'
config['write_osim_file'] = True
config['update_knee_splines'] = False
config['static_vas'] = False
config['update_max_iso_forces'] = True
config['subject_height'] = '169'
config['subject_mass'] = '56'
        
muscleModel = FieldworkGait2392SomsoMuscleStep(config)
muscleModel.inputData(0, geomLowerLimb)
muscleModel.inputData(1, osimModel)
muscleModel.inputData(2, fwLandmarks)
muscleModel.execute()


    
