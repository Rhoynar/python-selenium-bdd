from behave import given, when, then
from pages.dashboard import dashboard


@then(u'Dashboard Status shows correct values for row "{row}"')
def step_impl_dashboard_status(context, row):
    dashboard.verify_status(row)


@then(u'Clicking on Status Refresh should refresh status component')
def step_impl_status_refresh(context):
    dashboard.verify_refresh()


@then(u'Dashboard Battery shows Battery or AC Power with correct icon.')
def step_impl_battery_status(context):
    dashboard.verify_battery_status()


@then(u'Clicking on Battery Refresh should refresh battery component')
def step_impl_battery_refresh(context):
    dashboard.verify_battery_refresh()


@then(u'Dashboard Detector Settings shows correct values for row "{row}"')
def step_impl_detector_settings(context, row):
    dashboard.veify_detector_setting(row)


@then(u'Dashboard GPS shows correct values for row "{row}"')
def step_impl_gps_settings(context, row):
    dashboard.verify_gps_setting(row)
