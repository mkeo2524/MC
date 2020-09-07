from trcsource.trcdata import load
from trcframe.trcframeselector import trcframeselect
from fieldwork import llstep
import os
import json

DEFAULT_MODEL_LANDMARKS = (
    'pelvis-LASIS', 'pelvis-RASIS', 'pelvis-Sacral',
    'femur-MEC-l', 'femur-LEC-l', 
    'femur-MEC-r', 'femur-LEC-r',
    'tibiafibula-MM-l', 'tibiafibula-LM-l',
    'tibiafibula-MM-r', 'tibiafibula-LM-r',
    )

path = r'C:\Users\mkeo2\Desktop\work material\server\P8Static01.trc'
frame = 100
tester = load(path)
test = trcframeselect(tester, frame)

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

data = llstep.LLStepData(config, test)
data.loadData()
data.updateFromConfig()
data._preprocessLandmarks()
data.outputModelDict
data.LL
print(data)


