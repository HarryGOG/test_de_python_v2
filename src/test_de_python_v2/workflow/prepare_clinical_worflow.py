
import luigi
import pandas as pd
from test_de_python_v2.job.prepare_clinical_trials_data import prepare_clinical
from test_de_python_v2.workflow.prepare_drugs_workflow import PrepareDrugs



class PrepareClinical(luigi.Task):
    '''
      Generate a luigi worflow that generate a clinical trial data well formated and save the results
      Paarameters are in the config file
      '''


    path_clinical_file = luigi.Parameter()
    output_clinical_file = luigi.Parameter()

    def requires(self):
        return PrepareDrugs()


    def output(self):
        return luigi.LocalTarget(self.output_clinical_file)

    def run(self):

        with self.output().temporary_path() as output_path:
            df = pd.read_csv(self.path_clinical_file).fillna('')
            clinical_prepare = prepare_clinical(df)

            clinical_prepare.to_csv(output_path)

