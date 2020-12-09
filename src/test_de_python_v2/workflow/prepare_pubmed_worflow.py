
import luigi
import pandas as pd
from test_de_python_v2.job.prepare_pubmed_data import prepare_pubmed
from test_de_python_v2.workflow.prepare_clinical_worflow import PrepareClinical



class PreparePubmed(luigi.Task):
    '''
      Generate a luigi worflow that generate a pubmed data well formated and save the results
      Parameters are in the config file
      '''

    path_pubmed_file_csv = luigi.Parameter()
    path_pubmed_file_json = luigi.Parameter()
    output_pubmed_file = luigi.Parameter()

    def requires(self):
        return PrepareClinical()


    def output(self):
        return luigi.LocalTarget(self.output_pubmed_file)

    def run(self):

        with self.output().temporary_path() as output_path:
            df_json = pd.read_json(self.path_pubmed_file_json).fillna('')
            df_csv = pd.read_csv(self.path_pubmed_file_csv).fillna('')
            pubmed_prepare = prepare_pubmed(df_csv, df_json)

            pubmed_prepare.to_csv(output_path)

