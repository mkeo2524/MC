import os
from trcsource.trcdata import load
from trcframe.trcframeselector import trcframeselect
from zipoutput import output_zip
from model import run

# path to trc file
path = os.environ('TRC_FILE') \
    if os.environ('TRC_FILE') else r'C:\Users\mkeo2\Desktop\MC\server\trcs\StaticCalibration.trc'
osim_out_dir = os.environ('OSIM_OUTPUT_DIR') \
    if os.environ('OSIM_OUTPUT_DIR') else r'C:\Users\mkeo2\Desktop\MC\server\backend\geom\osim'

path = r'C:\Users\mkeo2\Desktop\MC\server\trcs\StaticCalibration.trc'
osim_out_dir = r'C:\Users\mkeo2\Desktop\MC\server\backend\geom\osim'
trcData = load(path)  # load trc data
trcFrame = trcframeselect(trcData, 100)  # get marker coordinates for all frames

# configuration data for fieldwork
landmarks = {
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

generation_config = {'identifier': '', 'GUI': False, 'registration_mode': 'shapemodel', 'pcs_to_fit': '1',
                     'mweight': '0.1',
                     'knee_corr': False, 'knee_dof': True, 'marker_radius': '5.0', 'skin_pad': '5.0',
                     'landmarks': landmarks}

geometry_config = {'identifier': '', 'GUI': False, 'scale_other_bodies': True, 'in_unit': 'mm', 'out_unit': 'm',
                   'osim_output_dir': osim_out_dir,
                   'write_osim_file': True, 'subject_mass': None, 'preserve_mass_distribution': False,
                   'adj_marker_pairs': {}}

muscle_config = {'osim_output_dir': osim_out_dir, 'in_unit': 'cm',
                 'out_unit': 'm', 'write_osim_file': True, 'update_knee_splines': False, 'static_vas': False,
                 'update_max_iso_forces': True, 'subject_height': '169', 'subject_mass': '56'}


if __name__ == "__main__":
    run(trcFrame, generation_config, geometry_config, muscle_config)
    output_zip()

