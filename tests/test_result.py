import pytest
import json
from pathlib import Path

from klimaatraadpleging.combiner import Combiner
from klimaatraadpleging.config import Config
from klimaatraadpleging.basic_scenarios import BasicScenarios
from klimaatraadpleging.etm_session import ETMSession
from klimaatraadpleging.result import Result
from klimaatraadpleging.demand_installer import DemandInstaller


@pytest.fixture
def combiner(input_mapping, basic_scenario, supply_and_savings):
    bs = BasicScenarios(basic_scenario, supply_and_savings)
    return Combiner(input_mapping, [{'key': 'costs_KPI', 'gquery': 'total_costs'}], bs)


def mocked_response(request, _):
    print(request.text)
    if "scenario" in request.text:
        return {'gqueries': {
                    'total_costs': {'future': 1, 'present': 0.5}
                }}

    return {'gqueries':
        {query: {'future': 1, 'present': 0.5} for query in DemandInstaller().supply_queries()}
    }

def test_calculate(combiner, requests_mock):
    requests_mock.put(
        f'{Config().etengine_url}/scenarios/12345',
        json=mocked_response,
        status_code=200
    )

    requests_mock.post(
        f'{Config().etengine_url}/scenarios/',
        json={'id': 12345},
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
