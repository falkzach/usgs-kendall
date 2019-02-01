import re

class kendalParser:
    """A parser class for the USGS Seasonal Mann-Kendall interactive program's output

    """

    tau_re = 'The tau correlation coefficient is\s(.*)'
    S_re = 'S =\s*(.*)'
    z_re = 'z =\s*(.*)'
    p_re = 'p =\s*(.*)'
    p_adjusted_re = 'p =\s*(.*)\sadjusted for correlation among seasons'
    trend_equation_re = 'Residual =\s+(.*)\s+\+\s+(.*)\s+\*\s+Time'

    def __init__(self, input_path):
        self.input = input_path

    def parse(self):
        with open(self.input) as f:
            content = f.read().splitlines() 
        for line in content:
            match = re.findall(self.tau_re, line)
            if(match):
                self.tau = match[0].strip()
                continue

            match = re.findall(self.S_re, line)
            if(match):
                self.S = match[0].strip()
                continue

            match = re.findall(self.z_re, line)
            if(match):
                self.z = match[0].strip()
                continue

            #NOTE: must check for p_adjust first and continue, refine regexes
            match = re.findall(self.p_adjusted_re, line)
            if(match):
                self.p_adjusted = match[0].strip()
                continue

            match = re.findall(self.p_re, line)
            if(match):
                self.p = match[0].strip()
                continue

            match = re.findall(self.trend_equation_re, line)
            if(match):
                self.trend_equation_coefficient = match[0][0].strip()
                self.trend_equation_intercept = match[0][1].strip()
                continue

    def get_data(self):
        return vars(self)


if __name__ == "__main__":
    input_path = './data/Output_example1.txt'
    # input_path = './tmp/kendal_1548994617_WY08_svol.txt'
    parser = kendalParser(input_path)
    parser.parse()
    data = parser.get_data()
    print(data)
