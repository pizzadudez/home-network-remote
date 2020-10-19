"""
Get and set access to master volume example.
"""
from __future__ import print_function
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


def main():
    print("volume.GetMute(): %s" % volume.GetMute())
    print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())
    print("volume.GetVolumeRange(): (%s, %s, %s)" % volume.GetVolumeRange())
    # print("volume.SetMasterVolumeLevel()")
    # volume.SetMasterVolumeLevel(-20.0, None)
    # print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())


def set_volume_percent(volume_percent):
    volume.SetMasterVolumeLevelScalar(volume_percent / 100, None)


if __name__ == "__main__":
    main()