import os
import pandas as pd

class NADP_NTN_DataManager:
    """A data manager for the National Atmospheric Deposition Program (NADP) National Trends Network (NTN) monthly data
    http://nadp.slh.wisc.edu/data/NTN/ntnAllsites.aspx

    """

    # TODO: write complete wrapper for these parameters, extract to kendalWrapper?
    test = 2
    smoothing = 1
    output_firstline = '{} {}'.format(test, smoothing)
    output_cols = ['yr', 'month', '','ppt', ]
    output_col_param_index = 2


    def __init__(self, input_path):
        self.input = input_path
        self.df = pd.read_csv(self.input)

    def get_output(self):
        return self.output

    def get_results_output(self):
        return self.results_output

    def generate_result_path(self, prefix='kendal'):
        path = os.path.dirname(self.output)
        fname = os.path.basename(self.output)
        self.results_output = '{}/{}_{}'.format(path, prefix, fname)

    def generate_subset_for_site_and_param(self, site_id, param):
        self.site_id = site_id
        self.param = param
        self.output_cols[self.output_col_param_index] = param
        self.subset = self.df[(self.df['siteID'] == site_id)]     # for only these sites
        self.subset = self.subset[self.output_cols]               # only keep these columns

    # TODO: operater as parameter?
    def filter_subset_by_parameter_threshold(self, parmater, threshold):
        self.subset = self.subset[(self.subset[parameter] >= threshold)]

    def write_subset_to_experiment_file(self, output_directory='./', prefix='', extension='txt'):
        output_directory = output_directory if output_directory.endswith('/') else output_directory + '/' # ensure directory ends with /
        extension = extension[1:] if extension.startswith('.') else extension # prune leading '.' from extensions

        self.output = '{}{}_{}_{}.{}'.format(output_directory, prefix, self.site_id, self.param, extension)
        f = open(self.output, 'w')
        f.write('{}{}'.format(self.output_firstline, '\n'))
        f.close()
        self.subset.to_csv(self.output, header=False, index=False, mode='a+')

        # set result path for the subset
        self.generate_result_path()

if __name__ == "__main__":
    input_path = './data/NTN-All-m.csv'
    dm = NADP_NTN_DataManager(input_path)
    dm.generate_subset_for_site_and_param('WY08', 'Ca')
    dm.write_subset_to_experiment_file()
