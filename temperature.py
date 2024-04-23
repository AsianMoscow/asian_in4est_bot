import clr
import os

hwtypes = ['Mainboard','SuperIO','CPU','RAM','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']

def initialize_openhardwaremonitor():
    file = rf'{os.getcwd()}\OpenHardwareMonitorLib.dll'
    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle

def fetch_stats(handle):
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)
        for j in i.SubHardware:
            j.Update()
            for subsensor in j.Sensors:
                parse_sensor(subsensor)

def parse_sensor(sensor):
    if sensor.Value:
        if str(sensor.SensorType) == 'Temperature':
            result = u'{} {} Temperature Sensor #{} {} - {}\u00B0C'\
                    .format(hwtypes[sensor.Hardware.HardwareType],
                            sensor.Hardware.Name, sensor.Index,
                            sensor.Name, sensor.Value
                    )
            print(result)

if __name__ == "__main__":
    print("OpenHardwareMonitor:")
    HardwareHandle = initialize_openhardwaremonitor()
    fetch_stats(HardwareHandle)