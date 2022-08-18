class KPIS():
    @property
    def kpis(self):
        return self._kpis

    @kpis.setter
    def kpis(self, data):
        self._kpis = {key['gquery']: {'key': key['key'], 'value': None} for key in data}

    @kpis.getter
    def kpis(self):
        return {val['key']: val['value'] for val in self._kpis.values()}

    def update_kpis(self, result):
        '''Update the KPIs based on parsed ETE response'''
        for query, outcome in result.items():
            self._kpis[query]['value'] = outcome['future']

    def kpi_queries(self):
        '''Return KPIS in ETE request format'''
        return {"gqueries": list(self._kpis.keys())}
