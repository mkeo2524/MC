
'''
MAP Client Plugin Step
'''
import os
import json
import llstep

DEFAULT_MODEL_LANDMARKS = (
    'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-Sacral',
    'femur-MEC-l', 'femur-LEC-l', 
    'femur-MEC-r', 'femur-LEC-r',
    'tibiafibula-MM-l', 'tibiafibula-LM-l',
    'tibiafibula-MM-r', 'tibiafibula-LM-r',
    )

config = {}
config['identifier'] = ''
config['GUI'] = 'False'
config['registration_mode'] = 'shapemodel'
config['pcs_to_fit'] = '1'
config['mweight'] = '0.1'
config['knee_corr'] = 'False'
config['knee_dof'] = 'False'
config['marker_radius'] = '5.0'
config['skin_pad'] = '5.0'
config['landmarks'] = {}
for l in DEFAULT_MODEL_LANDMARKS:
    config['landmarks'][l] = ''

data = llstep.LLStepData(config)
data.loadData()
data.updateFromConfig()
data.outputModelDict
data.LL


