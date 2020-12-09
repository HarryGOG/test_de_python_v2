import luigi
import pandas as pd
from test_de_python_v2.job.prepare_drugs_data import prepare_drugs




class PrepareDrugs(luigi.Task):
    '''
      Generate a luigi worflow that generate a clinical drugs data well formated and save the results
      Parameters are in the config file
      '''


    path_drugs_file = luigi.Parameter()
    output_drugs_file = luigi.Parameter()


    def output(self):
        return luigi.LocalTarget(self.output_drugs_file)

    def run(self):

        with self.output().temporary_path() as output_path:
            df = pd.read_csv(self.path_drugs_file).fillna('')
            drugs_prepare = prepare_drugs(df)

            drugs_prepare.to_csv(output_path)

