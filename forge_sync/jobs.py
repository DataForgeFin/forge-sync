from dagster import AssetSelection, define_asset_job, ScheduleDefinition

default_job = define_asset_job("default_job", AssetSelection.groups("default"))
default_schedule = ScheduleDefinition(job=default_job, cron_schedule="0 8 * * *")
