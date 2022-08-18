'''Represent a full setting as we can send it to the ETM'''

class CombinedSetting:
    def __init__(self, etm_scenario_name, kr_setting, etm_setting, kpi_settings):
        '''
        They are all dicts -
        TODO: please give them a default of being empty!!
        '''
        self.etm_scenario_name = etm_scenario_name
        self.kr_setting = kr_setting
        self.etm_setting = etm_setting
        self.kpis = {key['gquery']: {'key': key['key'], 'value': None} for key in kpi_settings}
        self.etm_scenario_id = None

    def as_json(self):
        '''Returns a dict that can be dumped by json'''
        return (
            self.kr_setting |
            {'etm_scenario': self.etm_scenario_name} |
            {val['key']: val['value'] for val in self.kpis.values()}
        )

    def as_request(self, with_queries=False):
        # This will change as we'll do two gquery requests :)
        if with_queries:
            return self._user_values_for_request() | self._gqueries_for_request()

        return self._user_values_for_request()

    def update_kpis(self, result):
        '''Update the KPI dict'''
        for query, outcome in result.items():
            self.kpis[query]['value'] = outcome['future']

    def add_setting(self, kr_key, kr_value, etm_settings):
        '''Add the settings for one klimaatraadpleging input to all settings'''
        if kr_key in self.kr_setting:
            raise KeyError(f'Settings for {kr_key} are already present')

        self.kr_setting[kr_key] = kr_value
        self.etm_setting.update(etm_settings)

    def _user_values_for_request(self):
        return {"scenario": {"user_values": self.etm_setting}}

    def _gqueries_for_request(self):
        return {"gqueries": list(self.kpis.keys())}
