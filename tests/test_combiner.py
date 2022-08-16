from klimaatraadpleging.basic_scenarios import BasicScenarios
from klimaatraadpleging.combined_setting import CombinedSetting
from klimaatraadpleging.combiner import Combiner

def test_generate_settings(input_mapping, basic_scenario, supply_and_savings):
    bs = BasicScenarios(basic_scenario, supply_and_savings)

    cmb = Combiner(input_mapping, [{'key': 'costs_KPI', 'gquery': 'total_costs'}], bs)

    gen = cmb.generate_settings()

    a_setting = next(gen)
    assert isinstance(a_setting, CombinedSetting)
    assert 'total_costs' in a_setting.kpis

    # Update this test
    assert len(a_setting.as_request()['scenario']['user_values']) > 4
