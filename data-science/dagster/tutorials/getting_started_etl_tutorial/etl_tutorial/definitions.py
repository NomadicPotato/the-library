from dagster_duckdb import DuckDBResource
from etl_tutorial import assets
from etl_tutorial.schedules import weekly_update_schedule
from etl_tutorial.sensors import adhoc_request_job, adhoc_request_sensor

import dagster as dg

tutorial_assets = dg.load_assets_from_modules([assets])
tutorial_asset_checks = dg.load_asset_checks_from_modules([assets])


defs = dg.Definitions(
    assets=tutorial_assets, # load assets from the assets module
    asset_checks=tutorial_asset_checks, # load asset checks from the assets module
    schedules=[weekly_update_schedule], # run on a weekly schedule
    jobs=[adhoc_request_job], # job for adhoc requests
    sensors=[adhoc_request_sensor], # sensor for adhoc requests
    resources={"duckdb": DuckDBResource(database="data/mydb.duckdb")},
)

