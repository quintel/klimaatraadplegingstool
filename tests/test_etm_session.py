import pytest

from klimaatraadpleging.combined_setting import CombinedSetting
from klimaatraadpleging.etm_session import ETMSession
from klimaatraadpleging.config import Config


@pytest.fixture
def setting():
    return CombinedSetting(
        'high_demand',
        {},
        {'slider_one': 10, 'slider_two': 20},
        [{'key': 'costs_kpi', 'gquery': 'total_costs'}]
    )

def test_calculate_kpis(setting, requests_mock):

    requests_mock.put(
        f'{Config().etengine_url}/scenarios/12345',
        json={
            'gqueries': {
                'total_costs': {'future': 1, 'present': 0.5}
            }
        },
        status_code=200
    )

    requests_mock.post(
        f'{Config().etengine_url}/scenarios/',
        json={'id': 12345},
        status_code=200
    )


    assert not setting.etm_scenario_id
    assert not setting.kpis['total_costs']['value']

    session = ETMSession()
    session.calculate_kpis(setting)

    assert setting.kpis['total_costs']['value'] == 1
    assert setting.etm_scenario_id == 12345
