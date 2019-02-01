import os
import time

import pandas as pd

from kendalWrapper import KendallWrapper
from kendalParser import kendalParser
from dataManager import NADP_NTN_DataManager

if __name__ == "__main__":
    timestamp = int(time.time())
    # TODO: get from input arguments
    input_path = './data/NTN-All-m.csv'
    temp_directory = './tmp'
    output_directory = './results'
    output_file = 'results.txt'

    # ensure the output directorys exists
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    params = ['Ca', 'Mg', 'K', 'Na', 'NH4', 'NO3', 'Cl', 'SO4', 'Br', 'pH', 'conduc', 'svol',]
    site_ids = ['WY08', 'MT00', 'MT05', 'MT07', 'MT97', 'ID02', 'ID03',]

    output_columns = ['site_id', 'param', 'tau', 'S', 'z', 'p', 'p_adjusted', 'trend_equation_coefficient', 'trend_equation_intercept','input',]

    # TODO: filter on these criteria, generate seperate results
    filter_param_to_threshold = {'Criteria1': 75, 'Criteria2': 90, 'Criteria3': 75}

    dm = NADP_NTN_DataManager(input_path)
    df = pd.DataFrame(columns=output_columns)
    df_filtered = pd.DataFrame(columns=output_columns)

    for site_id in site_ids:
        for param in params:
            # generate and store a subset of the dataset
            dm.generate_subset_for_site_and_param(site_id, param)
            dm.write_subset_to_experiment_file(temp_directory, timestamp, 'txt')

            # run the Seasonal Kendall
            process = KendallWrapper(dm.get_output(), dm.get_results_output())
            try:
                # TODO: results file written out but exceptions thrown, catch them and do nothing
                process.run()
            except:
                pass

            # parse results and add to dataframe
            parser = kendalParser(dm.get_results_output())
            parser.parse()
            results = parser.get_data()
            results['site_id'] = site_id
            results['param'] = param
            df = df.append(results, ignore_index=True)

            #
            # repeat with filtered data
            #

            # generate and store a filtered set of the dataset
            dm.generate_filtered_subset_for_site_and_param(site_id, param, filter_param_to_threshold)
            dm.write_subset_to_experiment_file(temp_directory, '{}_{}'.format(timestamp, 'filtered'), 'txt')

            # run the Seasonal Kendall
            process = KendallWrapper(dm.get_output(), dm.get_results_output())
            try:
                # TODO: results file written out but exceptions thrown, catch them and do nothing
                process.run()
            except:
                pass

            # parse results and add to dataframe
            parser = kendalParser(dm.get_results_output())
            parser.parse()
            results = parser.get_data()
            results['site_id'] = site_id
            results['param'] = param
            df_filtered = df_filtered.append(results, ignore_index=True)

    # write results out to csv
    df.to_csv('{}/{}_{}'.format(output_directory, timestamp, output_file))
    df_filtered.to_csv('{}/{}_filtered_{}'.format(output_directory, timestamp, output_file))
