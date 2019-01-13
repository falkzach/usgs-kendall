import time

import pandas as pd

from kendalWrapper import KendallWrapper
from kendalParser import kendalParser
from dataManager import NADP_NTN_DataManager

if __name__ == "__main__":
    timestamp = int(time.time())
    # TODO: get from input arguments
    input_path = './data/Master-NTN-monthly.csv'
    output_path = './results.txt'

    params = ['Ca', 'Mg', 'K', 'Na', 'NH4', 'NO3', 'Cl', 'SO4', 'Br', 'pH', 'conduc', 'svol',]
    site_ids = ['WY08 ','MT00 ','MT05 ','MT07 ','MT97 ','ID02','ID03',]

    cols = ['site_id', 'param', 'tau', 'S', 'Z', 'p', 'p_adjust', 'trend_eqn_coefficient', 'trend_eqn_intercept',]

    df = pd.DataFrame(columns=cols)

    dm = NADP_NTN_DataManager(input_path)
    for site_id in site_ids:
        for param in params:
            dm.generate_subset_for_site_and_param(site_id, param)
            dm.write_subset_to_experiment_file('./tmp', timestamp, 'txt')
            process = KendallWrapper(dm.get_output(), dm.generate_result_path())
            parser = kendalParser(dm.generate_result_path())
            df.append(parser.get_data(), ignore_index=True)

    df.to_csv(output_path)

