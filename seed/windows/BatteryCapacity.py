
r'''
https://stackoverflow.com/questions/16380394/getting-battery-capacity-windows-with-python

'''

import wmi
class BatteryCapacity:
    __t = wmi.WMI(moniker = "//./root/wmi")

    @classmethod
    def get_num_batteries(cls):
        batteries = cls.__t.ExecQuery('Select * from BatteryFullChargedCapacity')
        return len(batteries)

    @classmethod
    def get_FullChargedCapacity(cls, battery_idx):
        batteries = cls.__t.ExecQuery('Select * from BatteryFullChargedCapacity')
        return batteries[battery_idx].FullChargedCapacity

    @classmethod
    def get_RemainingCapacity(cls, battery_idx):
        batteries = cls.__t.ExecQuery('Select * from BatteryStatus')
        return batteries[battery_idx].RemainingCapacity
    @classmethod
    def get_remaining_capacity_rate(cls, battery_idx):
        return (cls.get_RemainingCapacity(battery_idx)
                / float(cls.get_FullChargedCapacity(battery_idx))
                )
del wmi


def _via_wmi():
    import wmi

    c = wmi.WMI()
    t = wmi.WMI(moniker = "//./root/wmi")

    batts1 = c.CIM_Battery(Caption = 'Portable Battery')
    for i, b in enumerate(batts1):
        print('Battery %d Design Capacity: %d mWh' % (i, b.DesignCapacity or 0))


    batts2 = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts2):
        print ('Battery %d Fully Charged Capacity: %d mWh' %
              (i, b.FullChargedCapacity))

    #batts3 = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    batts3 = t.ExecQuery('Select * from BatteryStatus')
    for i, b in enumerate(batts3):
        print('\nBattery %d ***************' % i)
        print('Tag:               ' + str(b.Tag))
        print('Name:              ' + b.InstanceName)

        print('PowerOnline:       ' + str(b.PowerOnline))
        print('Discharging:       ' + str(b.Discharging))
        print('Charging:          ' + str(b.Charging))
        print('Voltage:           ' + str(b.Voltage))
        print('DischargeRate:     ' + str(b.DischargeRate))
        print('ChargeRate:        ' + str(b.ChargeRate))
        print('RemainingCapacity: ' + str(b.RemainingCapacity))
        print('Active:            ' + str(b.Active))
        print('Critical:          ' + str(b.Critical))

        for name in dir(b):
            value = getattr(b, name)
            print(f'{name} = {value!r}')

        #???len(batts1)???
        assert len(batts3) == len(batts2)
        for b2, b3 in zip(batts2, batts3):
            print('rate =', b3.RemainingCapacity / float(b2.FullChargedCapacity))


def _via_psutil():
    import psutil
    def secs2hours(secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    battery = psutil.sensors_battery()
    battery
    sbattery(percent=93, secsleft=16628, power_plugged=False)
    print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))


if __name__ == "__main__":
    print('rate =', BatteryCapacity.get_remaining_capacity_rate(0))
    _via_wmi()
    _via_psutil()

