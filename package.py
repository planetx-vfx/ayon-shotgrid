name = "shotgrid"
title = "Shotgrid"
_version = "0.6.10"
_dev = "+dev2"
version = _version + _dev
client_dir = "ayon_shotgrid"

services = {
    "ShotgridLeecher": {
        "image": f"ynput/ayon-shotgrid-leecher:{_version}"},
    "ShotgridProcessor": {
        "image": f"ynput/ayon-shotgrid-processor:{_version}"},
    "ShotgridTransmitter": {
        "image": f"ynput/ayon-shotgrid-transmitter:{_version}"},
}
ayon_required_addons = {
    "core": ">=0.3.0",
}
ayon_compatible_addons = {}
