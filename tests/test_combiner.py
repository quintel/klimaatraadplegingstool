import pytest
import pandas as pd
from klimaatraadpleging.basic_scenarios import BasicScenarios
from klimaatraadpleging.combined_setting import CombinedSetting
from klimaatraadpleging.combiner import Combiner

@pytest.fixture
def input_mapping():
    return pd.read_csv('config/input_mapping.csv', index_col=[0,1])

@pytest.fixture
def supply_and_savings():
    return pd.read_csv('config/supply_and_savings.csv')

@pytest.fixture
def basic_scenario():
    return pd.read_csv('config/basic_scenarios.csv')

def test_generate_settings(input_mapping, basic_scenario, supply_and_savings):
    bs = BasicScenarios(basic_scenario, supply_and_savings)

    cmb = Combiner(input_mapping, [{'key': 'costs_KPI', 'gquery': 'total_costs'}], bs)

    gen = cmb.generate_settings()

    a_setting = next(gen)
    assert isinstance(a_setting, CombinedSetting)
    assert 'total_costs' in a_setting.kpis

    # Update this test
    assert len(a_setting.as_request()['scenario']['user_values']) > 4
