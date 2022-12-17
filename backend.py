# TODO: flask app that listens to webhook

import meraki
import os
from dotenv import load_dotenv

load_dotenv()

org_id = '877061'
net_id = 'L_634444597505856873'

dashboard = meraki.DashboardAPI(os.environ['MERAKI_API_TOKEN'], output_log=False,print_console=False)


def get_mv_serials(net_id):
    """Searches a dashboard network and returns a list with any MV serials"""
    mv_serials = []
    response = dashboard.networks.getNetworkDevices(
        net_id
    )
    for i in response:
        if 'MV' in i['model']:
            if i['model'] == 'MV2':
                pass
            else:
                mv_serials.append(i["serial"])
    return mv_serials


def mv_current_audio_status(mv_serial):
    """returns if audio is enabled on an MV"""
    response = dashboard.camera.getDeviceCameraQualityAndRetention(
        mv_serial
    )
    return response['audioRecordingEnabled']


def mv_disable_audio(mv_serial):
    """turns off audio recording on MV by serial"""
    dashboard.camera.updateDeviceCameraQualityAndRetention(
        mv_serial,
        audioRecordingEnabled=False
    )
    response = dashboard.camera.getDeviceCameraQualityAndRetention(
        mv_serial
    )
    print("Audio has been disabled")
    return response['audioRecordingEnabled']

def mv_enable_audio(mv_serial):
    """turns on audio recording on MV by serial"""
    dashboard.camera.updateDeviceCameraQualityAndRetention(
        mv_serial,
        audioRecordingEnabled=True
    )
    response = dashboard.camera.getDeviceCameraQualityAndRetention(
        mv_serial
    )
    print("Audio has been Enabled")
    return response['audioRecordingEnabled']

# for i in mv_serials:
#     print(f"Serial number: {i}, Audio Recording is {mv_current_audio_status(i)}")
#     mv_disable_audio(i)
#     print(f"Serial number: {i}, Audio Recording is {mv_current_audio_status(i)}")

# for i in range(len(mv_serials)):
#     mv_current_audio_status(mv_serials[i])
#
