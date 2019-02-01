import time

import pandas as pd

from kendalWrapper import KendallWrapper
from kendalParser import kendalParser
from dataManager import NADP_NTN_DataManager

if __name__ == "__main__":
    timestamp = int(time.time())
    # TODO: get from input arguments
    input_path = './data/NTN-All-m.csv'
    output_path = './results.txt'

    params = ['Ca', 'Mg', 'K', 'Na', 'NH4', 'NO3', 'Cl', 'SO4', 'Br', 'pH', 'conduc', 'svol',]
    site_ids = ['WY08', 'MT00', 'MT05', 'MT07', 'MT97', 'ID02', 'ID03',]

    cols = ['site_id', 'param', 'tau', 'S', 'Z', 'p', 'p_adjust', 'trend_eqn_coefficient', 'trend_eqn_intercept',]

    # TODO: filter on these criteria, generate seperate results
    filter_param_to_threshold = {'Criteria1': 75, 'Criteria2': 90, 'Criteria3': 75}

    dm = NADP_NTN_DataManager(input_path)
    df = pd.DataFrame(columns=cols)

    for site_id in site_ids:
        for param in params:
            dm.generate_subset_for_site_and_param(site_id, param)
            # TODO: apply filter to subset
            dm.write_subset_to_experiment_file('./tmp', timestamp, 'txt')
            process = KendallWrapper(dm.get_output(), dm.get_results_output())
            parser = kendalParser(dm.get_results_output())
            df.append(parser.get_data(), ignore_index=True)
            print(parser.get_data())

    # TODO: change output path to include filtered
    df.to_csv(output_path)
