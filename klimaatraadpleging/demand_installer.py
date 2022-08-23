from collections import defaultdict

class DemandInstaller():
    #  @Joris, fill in the supply queries here after the keywords of your choice.
    # You can add as many supply queries as you like, with as many custom keywords
    QUERIES = {
        'heat': 'total_heat_supply',
        'hydrogen': 'total_hydrogen_supply',
        'biomass': 'total_biomass_supply',
        'electricity': 'total_electricity_supply'
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
        # You can use the keywords for the queries you defined on line 6 in the
        # following way:
        if self.supply.heat > 300:
            self.sliders['my_slider_name_one'] = 100
            self.sliders['my_slider_name_two'] = 200
            # The sliders are defaulting to 0, so you can use += directly without checking first
            self.sliders['my_slider_name_three'] += 1

        # Or you can use the 'any' keyword to safely check if the value is bigger than 0
        if self.supply.hydrogen.any():
            self.sliders['hydrogen_based_heatpump'] = 100

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
        '''Abusing this for 'other' ints'''
        return self.value < other

    def __le__(self, other):
        '''Abusing this for 'other' ints'''
        return self.value <= other

    def __eq__(self, other):
        '''Abusing this for 'other' ints'''
        return self.value == other

    def __ne__(self, other):
        '''Abusing this for 'other' ints'''
        return self.value != other

    def __gt__(self, other):
        '''Abusing this for 'other' ints'''
        return self.value > other

    def __ge__(self, other):
        '''Abusing this for 'other' ints'''
        return self.value >= other