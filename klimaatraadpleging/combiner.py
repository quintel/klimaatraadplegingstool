'''Combines settings into a request'''

import itertools
from .combined_setting import CombinedSetting

class Combiner:
    def __init__(self, input_mapping, kpis, basic_scenarios):
        '''Kpis is a dict, input mapping the DF, basic_sceanrios is a BasicScenarios'''
        self.kpis = kpis
        self.input_mapping = input_mapping
        self.basics = basic_scenarios

    def generate_settings(self):
        for permutation in self._generate_permutations():
            for scenario_name, scenario_settings in self.basics.generate_scenarios():
                cmb_setting = CombinedSetting(scenario_name, {}, scenario_settings, self.kpis)
                for kr_key, kr_value in permutation.items():
                    cmb_setting.add_setting(
                        kr_key,
                        kr_value,
                        self._handle_etm_settings(kr_key, kr_value)
                    )

                yield cmb_setting

    def _generate_permutations(self):
        keys, values = zip(*self._possibilities().items())
        return (dict(zip(keys, v)) for v in itertools.product(*values))

    def _possibilities(self):
        possibilities = {}
        for key, value in self.input_mapping.index:
            if key in possibilities:
                possibilities[key].append(value)
            else:
                possibilities[key] = [value]

        return possibilities

    def _handle_etm_settings(self, kr_key, kr_value):
        thing = self.input_mapping.loc[kr_key, kr_value].to_dict()

        # TODO: use multi index? instead of this ugly thing

        as_a_dict = {}

        for i in range(int(len(thing.keys()) / 2)):
            if thing[f'slider_{i}_name']:
                as_a_dict[thing[f'slider_{i}_name']] = thing[f'slider_{i}_value']

        return as_a_dict
