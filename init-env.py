from modules import launch_utils

with launch_utils.startup_timer.subcategory("prepare environment"):
    launch_utils.prepare_environment()
