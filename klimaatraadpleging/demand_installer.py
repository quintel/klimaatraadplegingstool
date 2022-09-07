from collections import defaultdict

class DemandInstaller():
    #  @Joris, fill in the supply queries here after the keywords of your choice.
    # You can add as many supply queries as you like, with as many custom keywords
    QUERIES = {
        'electricity_curtailed': 'electricity_curtailed',
        'hydrogen_export': 'hydrogen_prod_to_export_in_sankey',
        #'unused_heat': 'energy_heat_unused_steam_hot_water_in_collective_heat_network_mekko',
        'geothermal_heat': 'energy_heat_well_geothermal_in_collective_heat_network_mekko',
        'industrial_heat': 'energy_heat_industry_residual_heat_in_collective_heat_network_mekko',
        'desired_local_biomass_production': 'max_demand_dry_biomass',
        'desired_biomass_production_import': 'max_demand_biogenic_waste',
        'desired_biomass_production_extra_import': 'max_demand_oily_biomass',#work around for max biomass slider biogenic waste
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

        if self.supply.electricity_curtailed > 50: #if curtailment is bigger than 50 PJ create electrification
            self.sliders["transport_bus_using_compressed_natural_gas_share"] = 0
            self.sliders["transport_bus_using_diesel_mix_share"] = 0
            self.sliders["transport_bus_using_electricity_share"] = 100
            self.sliders["transport_bus_using_gasoline_mix_share"] = 0
            self.sliders["transport_bus_using_hydrogen_share"] = 0
            self.sliders["transport_bus_using_lng_share"] = 0
            self.sliders["transport_car_using_compressed_natural_gas_share"] = 0
            self.sliders["transport_car_using_diesel_mix_share"] = 0
            self.sliders["transport_car_using_electricity_share"] = 100
            self.sliders["transport_car_using_gasoline_mix_share"] = 0
            self.sliders["transport_car_using_hydrogen_share"] = 0
            self.sliders["transport_car_using_lpg_share"] = 0
            self.sliders["transport_motorcycle_using_electricity_share"] = 100
            self.sliders["transport_motorcycle_using_gasoline_mix_share"] = 0
            self.sliders["transport_passenger_train_using_coal_share"] = 0
            self.sliders["transport_passenger_train_using_diesel_mix_share"] = 0
            self.sliders["transport_passenger_train_using_electricity_share"] = 100
            self.sliders["transport_passenger_train_using_hydrogen_share"] = 0

        if self.supply.electricity_curtailed > 100:
            self.sliders["transport_freight_train_using_diesel_mix_share"] = 0
            self.sliders["transport_freight_train_using_electricity_share"] = 100
            self.sliders["transport_freight_train_using_hydrogen_share"] = 0
            self.sliders["transport_van_using_compressed_natural_gas_share"] = 0
            self.sliders["transport_van_using_diesel_mix_share"] = 0
            self.sliders["transport_van_using_electricity_share"] = 100
            self.sliders["transport_van_using_gasoline_mix_share"] = 0
            self.sliders["transport_van_using_hydrogen_share"] = 0
            self.sliders["transport_van_using_lpg_share"] = 0
            self.sliders["households_heater_combined_hydrogen_share"] = 0
            self.sliders["households_heater_combined_network_gas_share"] = 50.0 #reduced to increase heat pumps
            self.sliders["households_heater_district_heating_steam_hot_water_share"] = 0
            self.sliders["households_heater_electricity_share"] = 0
            self.sliders["households_heater_heatpump_air_water_electricity_share"] = 50.0
            self.sliders["households_heater_heatpump_ground_water_electricity_share"] = 0
            self.sliders["households_heater_heatpump_pvt_electricity_share"] = 0
            self.sliders["households_heater_hybrid_heatpump_air_water_electricity_share"] = 0
            self.sliders["households_heater_hybrid_hydrogen_heatpump_air_water_electricity_share"] = 0
            self.sliders["households_heater_network_gas_share"] = 0
            self.sliders["households_heater_wood_pellets_share"] = 0
            self.sliders["buildings_space_heater_collective_heatpump_water_water_ts_electricity_share"] = 25.0
            self.sliders["buildings_space_heater_combined_hydrogen_share"] = 0.0
            self.sliders["buildings_space_heater_district_heating_steam_hot_water_share"] = 0
            self.sliders["buildings_space_heater_electricity_share"] = 0.0
            self.sliders["buildings_space_heater_heatpump_air_water_electricity_share"] = 25.0
            self.sliders["buildings_space_heater_heatpump_air_water_network_gas_share"] = 0.0
            self.sliders["buildings_space_heater_hybrid_heatpump_air_water_electricity_share"] = 0.0
            self.sliders["buildings_space_heater_hybrid_hydrogen_heatpump_air_water_electricity_share"] = 0.0
            self.sliders["buildings_space_heater_network_gas_share"] = 50.0
            self.sliders["buildings_space_heater_wood_pellets_share"] = 0.0
            self.sliders["capacity_of_energy_hydrogen_flexibility_p2g_electricity"] = 10000

        if self.supply.electricity_curtailed > 150:
            self.sliders["industry_final_demand_for_other_food_steam_hot_water_share"] = 0
            self.sliders["industry_other_food_burner_coal_share"] = 0
            self.sliders["industry_other_food_burner_crude_oil_share"] = 0
            self.sliders["industry_other_food_burner_hydrogen_share"] = 0
            self.sliders["industry_other_food_burner_network_gas_share"] = 0
            self.sliders["industry_other_food_burner_wood_pellets_share"] = 0
            self.sliders["industry_other_food_heater_electricity_share"] = 100
            self.sliders["industry_final_demand_for_other_paper_steam_hot_water_share"] = 0
            self.sliders["industry_other_paper_burner_coal_share"] = 0
            self.sliders["industry_other_paper_burner_crude_oil_share"] = 0
            self.sliders["industry_other_paper_burner_hydrogen_share"] = 0
            self.sliders["industry_other_paper_burner_network_gas_share"] = 0
            self.sliders["industry_other_paper_burner_wood_pellets_share"] = 0
            self.sliders["industry_other_paper_heater_electricity_share"] = 100
            self.sliders["capacity_of_energy_hydrogen_flexibility_p2g_electricity"] = 20000

        if self.supply.electricity_curtailed > 200:
            self.sliders["capacity_of_energy_hydrogen_flexibility_p2g_electricity"] = 30000

        #hydrogen
        if self.supply.hydrogen_export > 0:
            self.sliders["industry_chemicals_fertilizers_burner_coal_share"] = 0
            self.sliders["industry_chemicals_fertilizers_burner_crude_oil_share"] = 0
            self.sliders["industry_chemicals_fertilizers_burner_hydrogen_share"] = 100
            self.sliders["industry_chemicals_fertilizers_burner_network_gas_share"] = 0
            self.sliders["industry_chemicals_fertilizers_burner_wood_pellets_share"] = 0
            self.sliders["industry_chemicals_fertilizers_hydrogen_network_share"] = 100
            self.sliders["industry_chemicals_fertilizers_steam_methane_reformer_hydrogen_share"] = 0
            self.sliders["industry_final_demand_for_chemical_fertilizers_steam_hot_water_share"] = 0

        if self.supply.hydrogen_export > 75:
            self.sliders["industry_steel_blastfurnace_bof_share"] = 0
            self.sliders["industry_steel_cyclonefurnace_bof_share"] = 0
            self.sliders["industry_steel_dri_hydrogen_share"] = 100
            self.sliders["industry_steel_dri_network_gas_share"] = 0
            self.sliders["industry_steel_scrap_hbi_eaf_share"] = 0

        if self.supply.hydrogen_export > 150:
            self.sliders["industry_chemicals_other_burner_coal_share"] = 0
            self.sliders["industry_chemicals_other_burner_crude_oil_share"] = 0
            self.sliders["industry_chemicals_other_burner_hydrogen_share"] = 100
            self.sliders["industry_chemicals_other_burner_network_gas_share"] = 0
            self.sliders["industry_chemicals_other_burner_wood_pellets_share"] = 0
            self.sliders["industry_chemicals_other_heater_electricity_share"] = 0
            self.sliders["industry_chemicals_other_heatpump_water_water_electricity_share"] = 0
            self.sliders["industry_chemicals_other_network_gas_non_energetic_share"] = 0
            self.sliders["industry_chemicals_other_steam_recompression_electricity_share"] = 0
            self.sliders["industry_final_demand_for_chemical_other_steam_hot_water_share"] = 0

        if self.supply.hydrogen_export > 300:
            self.sliders["industry_chemicals_refineries_burner_coal_share"] = 0
            self.sliders["industry_chemicals_refineries_burner_crude_oil_share"] = 0
            self.sliders["industry_chemicals_refineries_burner_hydrogen_share"] = 100
            self.sliders["industry_chemicals_refineries_burner_network_gas_share"] = 0
            self.sliders["industry_chemicals_refineries_burner_wood_pellets_share"] = 0
            self.sliders["industry_final_demand_for_chemical_refineries_steam_hot_water_share"] = 0

        if self.supply.hydrogen_export > 450:
            self.sliders["industry_chemicals_other_coal_non_energetic_share"] = 0
            self.sliders["industry_chemicals_other_crude_oil_non_energetic_share"] = 0
            self.sliders["industry_chemicals_other_hydrogen_non_energetic_share"] = 100
            self.sliders["industry_chemicals_other_wood_pellets_non_energetic_share"] = 0

        if self.supply.hydrogen_export > 800:
            self.sliders["transport_truck_using_compressed_natural_gas_share"] = 0
            self.sliders["transport_truck_using_diesel_mix_share"] = 0
            self.sliders["transport_truck_using_electricity_share"] = 0
            self.sliders["transport_truck_using_gasoline_mix_share"] = 0
            self.sliders["transport_truck_using_hydrogen_share"] = 100
            self.sliders["transport_truck_using_lng_mix_share"] = 0

        if self.supply.hydrogen_export > 900:
            self.sliders["households_heater_combined_hydrogen_share"] = 25
            self.sliders["households_heater_combined_network_gas_share"] -= 25

        if self.supply.hydrogen_export > 950:
            self.sliders["buildings_space_heater_combined_hydrogen_share"] = 25
            self.sliders["buildings_space_heater_network_gas_share"] -= 25

        #heat

        if self.supply.geothermal_heat + self.supply.industrial_heat > 25000000000: #25 PJ = 25000000000 MJ
            self.sliders["households_heater_district_heating_steam_hot_water_share"] = 25
            self.sliders["households_heater_combined_network_gas_share"] -= 25

        if self.supply.geothermal_heat + self.supply.industrial_heat > 50000000000: # 50 PJ = 50000000000 MJ
            self.sliders["buildings_space_heater_district_heating_steam_hot_water_share"] = 25
            self.sliders["buildings_space_heater_network_gas_share"] -= 25

        #biomass

        if self.supply.desired_local_biomass_production + self.supply.desired_biomass_production_import + self.supply.desired_biomass_production_extra_import > 50:
            self.sliders["agriculture_burner_network_gas_share"] = 80
            self.sliders["agriculture_burner_wood_pellets_share"] = 20
            self.sliders["industry_aggregated_other_industry_network_gas_share"] = 80
            self.sliders["industry_aggregated_other_industry_wood_pellets_share"] = 20

        if self.supply.desired_local_biomass_production + self.supply.desired_biomass_production_import + self.supply.desired_biomass_production_extra_import > 100:
            self.sliders["agriculture_burner_network_gas_share"] -= 20
            self.sliders["agriculture_burner_wood_pellets_share"] += 20
            self.sliders["industry_aggregated_other_industry_network_gas_share"] -= 20
            self.sliders["industry_aggregated_other_industry_wood_pellets_share"] += 20

        if self.supply.desired_local_biomass_production + self.supply.desired_biomass_production_import + self.supply.desired_biomass_production_extra_import > 150:
            self.sliders["agriculture_burner_network_gas_share"] -= 20
            self.sliders["agriculture_burner_wood_pellets_share"] += 20
            self.sliders["industry_aggregated_other_industry_network_gas_share"] -= 20
            self.sliders["industry_aggregated_other_industry_wood_pellets_share"] += 20

        if self.supply.desired_local_biomass_production + self.supply.desired_biomass_production_import + self.supply.desired_biomass_production_extra_import > 200:
            self.sliders["agriculture_burner_network_gas_share"] -= 20
            self.sliders["agriculture_burner_wood_pellets_share"] += 20
            self.sliders["industry_aggregated_other_industry_network_gas_share"] -= 20
            self.sliders["industry_aggregated_other_industry_wood_pellets_share"] += 20

        if self.supply.desired_local_biomass_production + self.supply.desired_biomass_production_import + self.supply.desired_biomass_production_extra_import > 250:
            self.sliders["agriculture_burner_network_gas_share"] -= 20
            self.sliders["agriculture_burner_wood_pellets_share"] += 20
            self.sliders["industry_aggregated_other_industry_network_gas_share"] -= 20
            self.sliders["industry_aggregated_other_industry_wood_pellets_share"] += 20



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
