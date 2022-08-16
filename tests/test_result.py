import pytest
import json
from pathlib import Path

from klimaatraadpleging.combiner import Combiner
from klimaatraadpleging.config import Config
from klimaatraadpleging.basic_scenarios import BasicScenarios
from klimaatraadpleging.etm_session import ETMSession
from klimaatraadpleging.result import Result


@pytest.fixture
def combiner(input_mapping, basic_scenario, supply_and_savings):
    bs = BasicScenarios(basic_scenario, supply_and_savings)
    return Combiner(input_mapping, [{'key': 'costs_KPI', 'gquery': 'total_costs'}], bs)


def test_calculate(combiner, requests_mock):
    requests_mock.put(
        f'{Config().etengine_url}/scenarios/',
        json={
            'scenario': {
                'id': 12345
            },
            'gqueries': {
                'total_costs': {'future': 1, 'present': 0.5}
            }
        },
        status_code=200
    )

    result = Result(combiner, ETMSession())

    result.calculate()

    file = Path('tmp/output.json').resolve()
    file.parent.mkdir(exist_ok=True)
    result.write_to(file)

    fstream = open(file, 'r')
    as_json = json.loads(fstream.read())
    for line in as_json:
        assert line['costs_KPI'] == 1
        assert 'etm_scenario' in line

    fstream.close()

    file.unlink()
