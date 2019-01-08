import pexpect

class KendallWrapper:
    """A wrapper class for the USGS Seasonal Mann-Kendall interactive program

    The purpose of this class is to make the task of running many tests automatable
    Requires an input file, an output file and a smoothness coefficient, which defaults to 0.5
    """
    KENDALL = './Kendall-new'

    def __init__(self, input_path, output_path, smoothness_coefficient='0.5'):
        self.input = input_path
        self.output = output_path
        self.smoothness = smoothness_coefficient

    def run(self):
        c = pexpect.spawnu(self.KENDALL)

        c.expect('Enter filename for input data -->')
        c.sendline('{}'.format(self.input))

        c.expect('Enter filename for output -->')
        c.sendline('{}'.format(self.output))

        c.expect('Enter smoothness coefficient f -->')
        c.sendline('{}'.format(self.smoothness))

        c.expect('Press Enter to Continue.')
        c.sendline('')


if __name__ == "__main__":
    input_path = './data/Input_example1.txt'
    output_path = './results/test_out.txt'
    process = KendallWrapper(input_path, output_path)
    process.run()
