from klimaatraadpleging.demand_installer import DemandInstaller

class InstallDemand():
    @property
    def installer(self):
        return self._installer

    @installer.setter
    def installer(self, _):
        self._installer = DemandInstaller()

    def installer_queries(self):
        return {"gqueries": self.installer.supply_queries()}

    def update_installer(self, result):
        '''Updates the queries in the installer and runs it'''
        self.installer.update_supply(result)
        self.installer.install_demand()

    def installer_user_values(self):
        return {"scenario": {"user_values": self.installer.plain_user_values()}}
