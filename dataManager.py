import pandas as pd

class NADP_NTN_DataManager:
    """A data manager for the National Atmospheric Deposition Program (NADP) National Trends Network (NTN) monthly data
    http://nadp.slh.wisc.edu/data/NTN/ntnAllsites.aspx

    """

    # TODO: write complete wrapper for these parameters, extract to kendalWrapper?
    test = 2
    smoothing = 1
    output_firstline = '{} {}'.format(test, smoothing)
    output_cols = ['siteID', 'yr', 'month', '','ppt', ]
    output_col_param_index = 3


    def __init__(self, input_path):
        self.input = input_path
        self.df = pd.read_csv(self.input)

    def get_output(self):
        return self.output

    def generate_result_path(self, prefix='kendal'):
        return '{}_{}'.format(prefix, self.output)

    def generate_subset_for_site_and_param(self, site_id, param):
        self.site_id = site_id
        self.param = param
        self.output_cols[self.output_col_param_index] = param
        self.subset = self.df[(self.df['siteID'] == site_id)]     # for only these sites
        self.subset = self.subset[self.output_cols]                    # only keep these columns

    def write_subset_to_experiment_file(self, output_directory='./', prefix='', extension='txt'):
        output_directory = output_directory if output_directory.endswith('/') else output_directory + '/'
        extension = extension[1:] if extension.startswith('.') else extension
        self.output = '{}{}_{}_{}.{}'.format(output_directory, prefix, self.site_id, self.param, extension)
        f = open(self.output, 'w')
        f.write('{}{}'.format(self.output_firstline, '\n'))
        f.close()
        self.subset.to_csv(self.output, header=False, index=False, mode='a+')

if __name__ == "__main__":
    input_path = './data/Master-NTN-monthly.csv'

    dm = NADP_NTN_DataManager(input_path)
    dm.generate_subset_for_param('WY08', 'Ca')
    dm.write_subset_toexperiment_file(output_directory='./tmp')
