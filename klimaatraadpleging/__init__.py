import pandas as pd

from klimaatraadpleging.etm_session import ETMSession
from klimaatraadpleging.basic_scenarios import BasicScenarios
from klimaatraadpleging.result import Result
from klimaatraadpleging.combiner import Combiner


def generate_json():
    result = Result(
        Combiner(
            pd.read_csv('config/input_mapping.csv', index_col=[0,1]),
            [{'key': 'costs_KPI', 'gquery': 'total_costs'}], # Replace this with KPI config
            BasicScenarios(
                pd.read_csv('config/basic_scenarios.csv', index_col=0),
                pd.read_csv('config/supply_and_savings.csv', index_col=0)
            )
        ),
        ETMSession()
    )

    result.calculate()
    result.write_to('output/output.json')
