from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import pytest
import pandas as pd

@pytest.fixture
def input_mapping():
    return pd.read_csv('config/input_mapping.csv', index_col=[0,1])

@pytest.fixture
def supply_and_savings():
    return pd.read_csv('config/supply_and_savings.csv')

@pytest.fixture
def basic_scenario():
    return pd.read_csv('config/basic_scenarios.csv')
