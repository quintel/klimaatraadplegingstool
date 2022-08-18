from .heat_demand import HeatDemand
from .kpis import KPIS


class ETMScenario(KPIS, HeatDemand):
    def __init__(self, name, user_values, kpis):
        self.name = name
        self.id = None
        self.user_values = user_values
        self.kpis = kpis

    def as_json(self):
        '''Returns a dict that can be dumped by json'''
        return (
            {'etm_scenario': self.name} | self.kpis
        )

    def update(self, user_values):
        '''Update the user_values with new ones'''
        self.user_values.update(user_values)

    def scenario_object(self):
        '''Return user values in ETE request format'''
        return {"scenario": {"user_values": self.user_values}}
