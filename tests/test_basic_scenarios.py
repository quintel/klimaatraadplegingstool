import pandas as pd
import pytest

from klimaatraadpleging.basic_scenarios import BasicScenarios

@pytest.fixture
def supply_and_savings():
    return pd.read_csv('config/supply_and_savings.csv', index_col='input')

@pytest.fixture
def basic_scenario():
    return pd.read_csv('config/basic_scenarios.csv', index_col='input')

def test_sceanrios(basic_scenario, supply_and_savings):
    basics = BasicScenarios(basic_scenario, supply_and_savings)

    assert isinstance(basics.scenarios, dict)
    assert len(basics.scenarios.keys()) == 3


def test_generate(basic_scenario, supply_and_savings):
    basics = BasicScenarios(basic_scenario, supply_and_savings)

    gen = basics.generate_scenarios()

    scen, sett = next(gen)
    assert scen in basic_scenario.columns
    assert len(sett) > 2
    assert all(key in sett for key in basic_scenario.index.to_list() + supply_and_savings.index.to_list())
