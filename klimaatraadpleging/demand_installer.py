from collections import defaultdict

class DemandInstaller():
    #  @Joris, fill in the supply queries here after the keywords of your choice.
    # You can add as many supply queries as you like, with as many custom keywords
    QUERIES = {
        'heat': 'co2_sheet_total_final_energy_demand',
        # 'hydrogen': 'gquery_key',
    }

    def __init__(self) -> None:
        self.supply = Supply(self.QUERIES)
        self.sliders = defaultdict(lambda: 0)

    def supply_queries(self):
        return self.supply.gqueries()

    def update_supply(self, result):
        for query, outcome in result.items():
            self.supply.update(query, outcome['future'])

    def plain_user_values(self):
        return dict(self.sliders)

    def install_demand(self):
        '''
        Assumes the queries for supply are done already.
        @Joris, here you can add your if else statments
        '''
        # Some commented examples:
        # You can use the keywords for the queries you defined on line 6 in the
        # following way:
        # if self.supply.heat > 100:
        #     self.sliders['buildings_space_heater_district_heating_steam_hot_water_share'] = self.supply.heat / 3
        #     self.sliders['households_heater_district_heating_steam_hot_water_share'] = self.supply.heat / 3
        #     # The sliders are defaulting to 0, so you can use += directly without checking first
        #     self.sliders['my_slider_name_three'] = self.supply.heat / 3

        #     # Met een loopje - volgordelijk
        #     options = ['slider_1', 'slider_2', 'slider_3']
        #     heat_left = self.supply.heat
        #     for option in options:
        #         if not heat_left: break

        #         slider_setting = 10

        #         self.sliders[option] = slider_setting
        #         heat_left -= slider_setting


        # elif self.supply.heat > 50:
        #     self.sliders['buildings_space_heater_district_heating_steam_hot_water_share'] = 0.5

        # # Or you can use the 'any' keyword to safely check if the value is bigger than 0
        # if self.supply.hydrogen.any():
        #    self.sliders['households_insulation_level_apartments'] = 35

        # DO NOT FORGET: share groups need to be balanced by you. ETEngine is not going to
        # do it for you and will complain.


class Supply():
    def __init__(self, queries):
        self.queries = queries

    @property
    def queries(self):
        return self._queries

    @queries.setter
    def queries(self, values):
        self._queries = {name: Query(gquery) for name, gquery in values.items()}

    def __getattr__(self, query_name):
        return self._queries[query_name]

    def update(self, gquery, value):
        for query in self.queries.values():
            if query.gquery == gquery:
                query.value = value
                return

        raise KeyError(f'Gquery {gquery} could not be updated')

    def gqueries(self):
        return [query.gquery for query in self._queries.values()]

class Query():
    def __init__(self, gquery):
        self.gquery = gquery
        self.value = None

    def any(self):
        return not self.value is None and self.value > 0

    def __repr__(self):
        return repr(self.value)

    def __lt__(self, other):
        return self.value < self._value_for(other)

    def __le__(self, other):
        return self.value <= self._value_for(other)

    def __eq__(self, other):
        return self.value == self._value_for(other)

    def __ne__(self, other):
        return self.value != self._value_for(other)

    def __gt__(self, other):
        return self.value > self._value_for(other)

    def __ge__(self, other):
        return self.value >= self._value_for(other)

    def __mul__(self, other):
        return self.value * self._value_for(other)

    def __rmul__(self, other):
        return self.value * self._value_for(other)

    def __div__(self, other):
        return self.value / self._value_for(other)

    def __rdiv__(self, other):
        return self._value_for(other) / self.value

    def __add__(self, other):
        return self.value + self._value_for(other)

    def __radd__(self, other):
        return self.value + self._value_for(other)

    def __sub__(self, other):
        return self.value - self._value_for(other)

    def __rsub__(self, other):
        return self._value_for(other) - self.value

    def _value_for(self, other):
        '''Check if other is a Query of a float/int, return the value'''
        try:
            return other.value
        except AttributeError:
            return other
