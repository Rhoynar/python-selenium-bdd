from framework.webapp import webapp


class Dashboard():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Dashboard()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def verify_status(self, row):
        # Ex:
        # status = self.driver.find_element_by_id('dashboard-status-component').text
        # assert row in status, "{} not present in status component".format(row)
        print('Verifying dashboard status..')

    def verify_refresh(self):
        # Ex:
        # refresh = self.driver.find_element_by_id('dashboard-status-refresh-btn')
        # refresh.click()
        print('Verifying dashboard refresh component..')

    def verify_battery_status(self):
        # Ex:
        # battery = self.driver.find_element_by_id('dashboard-battery-status-component').text
        # assert battery is not None
        print('Verifying Battery status..')

    def verify_battery_refresh(self):
        # Ex:
        # refresh = self.driver.find_element_by_id('dashboard-battery-refresh-btn')
        # refresh.click()
        print('Verifying battery refresh..')

    def verify_gps_setting(self, row):
        # Ex:
        # status = self.driver.find_element_by_id('gps-setting-component').text
        # assert row in status, "{} not present in GPS component".format(row)
        print('Verifying GPS setting..')


dashboard = Dashboard.get_instance()
