
r'''
fix:
    avoid using "getmac.exe" since "getmac.exe" happens to be unsupported.
original:
    https://inc0x0.com/2019/02/changing-mac-address-windows-python-script/
        https://github.com/inc0x0/change-mac
see:
    "all internet query.txt"
'''

############################################################
##########################fix###############################
FIXED = True
from subprocess import Popen, PIPE
import subprocess
import locale
def run_cmd_and_get_stdout(cmd):
    encoding = locale.getpreferredencoding(False)
    r = subprocess.run(cmd, stdout=PIPE, universal_newlines=True, check=True)
    #bug: return r.stdout.decode(encoding)
    assert type(r.stdout) is str # since universal_newlines=True??
    return r.stdout

    #https://stackoverflow.com/questions/33435110/subprocess-popen-stdout
    #bufsize=1?
    with Popen(cmd, stdout=PIPE, universal_newlines=True, check=True) as process:
        bs = b''.join(process.stdout)
        return bs.decode(encoding)
        if 0:
            for line in io.TextIOWrapper(process.stdout, encoding=encoding):
                print(line, end='')
        else:
            for line in process.stdout: # b'\n', b'\r\n', b'\r' are recognized as newline
                print(line, end='')

def parse_wmic_get_value_to_dicts(wmic_get_value_output):
    'parse output of "wmic <cmd> <args...> get <args...> /value" to [dict]'
    dicts = []
    maybe_parts = wmic_get_value_output.split('\n\n\n')
    for maybe_part in maybe_parts:
        if not maybe_part or maybe_part.isspace(): continue
        part = maybe_part; del maybe_part
        d = {}; dicts.append(d)
        maybe_lines = part.split('\n')
        for maybe_line in maybe_lines:
            if not maybe_line or maybe_line.isspace(): continue
            line = maybe_line; del maybe_line
            i = line.find('=')
            if i < 0:
                print(wmic_get_value_output)
                print(repr(line))
                raise Exception('not output of "wmic ... get ... /value"')
            key = line[:i]
            value = line[i+1:]
            assert key.strip() == key
            assert key not in d
            d[key] = value
    #rint(dicts)
    #rint(maybe_parts)
    return dicts

def guid2maybe_interface_name(guid):
    'guid -> ""|interface_name'
    if not guid.startswith('{'):
        guid = '{' + guid
    if not guid.endswith('}'):
        guid = guid + '}'
    guid = guid.upper()

    #wmic nic where "NetConnectionID<>''" get NetConnectionID , GUID
    cmd = "wmic nic where NetConnectionID<>'' get NetConnectionID , GUID /value".split()
    #r = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8')
    r = run_cmd_and_get_stdout(cmd)
    dicts = parse_wmic_get_value_to_dicts(r)
    for d in dicts:
        if d['GUID'].upper() == guid:
            maybe_interface_name = d['NetConnectionID']
            assert maybe_interface_name
            break
    else:
        maybe_interface_name = ''
    return maybe_interface_name

def list_all_interfaces_guid():
    #wmic nic where "NetConnectionID<>''" get NetConnectionID , GUID , MACAddress /value
    #bug?: cmd = 'wmic nic where NetConnectionID<>"" get NetConnectionID , GUID , MACAddress /value'.split()
    cmd = "wmic nic where NetConnectionID<>'' get NetConnectionID , GUID , MACAddress /value".split()
    #cmd = "wmic nic get NetConnectionID , GUID , MACAddress /value".split()
    #r = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8')
    try:
        r = run_cmd_and_get_stdout(cmd)
    except:
        print(cmd)
        raise
    dicts = parse_wmic_get_value_to_dicts(r)
    for d in dicts:
        #rint(d)
        if not d['NetConnectionID']: continue
        print(sorted(d.items()))
    return True

############################################################
############################################################


import winreg
import itertools
import re
import sys
import argparse
import subprocess
import ctypes

REG_KEY_PATH_INTERFACES = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"


def get_reg_value(name, reg_key_path):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key_path) as registry_key:
            value, regtype = winreg.QueryValueEx(registry_key, name)
            return value
    except OSError:
        return None


def set_reg_value(name, value, reg_key_path):
    try:
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, reg_key_path):
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key_path, 0, winreg.KEY_WRITE) as current_key:
                winreg.SetValueEx(current_key, name, 0, winreg.REG_SZ, value)
        return True
    except OSError:
        return False


def del_reg_value(name, reg_key_path):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key_path, 0, winreg.KEY_WRITE) as registry_key:
            winreg.DeleteValue(registry_key, name)
            return True
    except OSError:
        return False


if not FIXED:
    def list_all_interfaces_guid():
        try:
            r = subprocess.run(["getmac", "/fo", "list", "/V"], capture_output=True)
            print(r.stdout.decode('utf-8'))
            return True
        except:
            return False


def san_mac(mac):
    mac1 = re.sub('[^a-fA-F\d]', '', mac)
    if len(mac1) != 12:
        print("Invalid MAC supplied")
        sys.exit()
    return mac1


def san_guid(net_cfg_instance_id):
    m = re.search('[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', net_cfg_instance_id)
    if m:
        return m.group(0)
    else:
        print("Invalid GUID supplied")
        sys.exit()


def set_mac_value(mac, guid):
    guid = san_guid(guid)
    guid = "{" + guid + "}"
    mac = san_mac(mac)
    try:
        subkeys = []
        # get the path names of all subkeys which are interfaces
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_KEY_PATH_INTERFACES) as registry_key:
            for i in itertools.count(start=0, step=1):
                try:
                    subkey_name = winreg.EnumKey(registry_key, i)
                    if len(subkey_name) == 4:
                        subkeys.append(subkey_name)
                except OSError:
                    break
        # loop through all interfaces and check which is the correct to edit
        for interface in subkeys:
            tmp_path = REG_KEY_PATH_INTERFACES + "\\" + interface
            net_cfg_instance_id = get_reg_value("NetCfgInstanceId", tmp_path)
            if net_cfg_instance_id == guid:
                if set_reg_value("NetworkAddress", mac, tmp_path):
                    print("MAC of " + str(guid) + " changed to " + str(mac))
                    return True
                else:
                    return False
        return False
    except OSError:
        return None


def restart_network_interface(guid):
    guid = san_guid(guid)
    if not FIXED:
        # parse interface name out of guid
        r = subprocess.run(["getmac", "/fo", "csv", "/V"], capture_output=True).stdout.decode('utf-8')
        r = r.split(",")
        interface_name = ""
        for i, j in enumerate(r):
            if guid in j:
                interface_name = r[i - 3].split("\r\n")[1]
    else:
        maybe_interface_name = guid2maybe_interface_name(guid)
        ##########
        interface_name = maybe_interface_name
    if len(interface_name) == 0:
        print("Could not find interface name, you need to restart the network interface on your own."
              "\r\nUse this command:")
        print('netsh interface set interface name="<insert interface name>" admin="enabled"')
        sys.exit()
    # trigger restart of networks interface
    cmd1 = 'netsh interface set interface name=' + interface_name + ' admin="disabled"'
    subprocess.run(cmd1)
    cmd2 = 'netsh interface set interface name=' + interface_name + ' admin="enabled"'
    subprocess.run(cmd2)


def remove_mac_value(guid):
    guid = san_guid(guid)
    guid = "{" + guid + "}"
    try:
        subkeys = []
        # get the path names of all subkeys which are interfaces
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_KEY_PATH_INTERFACES) as registry_key:
            for i in itertools.count(start=0, step=1):
                try:
                    subkey_name = winreg.EnumKey(registry_key, i)
                    if len(subkey_name) == 4:
                        subkeys.append(subkey_name)
                except OSError:
                    break
        # loop through all interfaces and check which is the correct to remove
        for interface in subkeys:
            tmp_path = REG_KEY_PATH_INTERFACES + "\\" + interface
            net_cfg_instance_id = get_reg_value("NetCfgInstanceId", tmp_path)
            if net_cfg_instance_id == guid:
                if del_reg_value("NetworkAddress", tmp_path):
                    print("Resetted MAC of " + str(guid) + " to default.")
                    return True
                else:
                    return False
        return False
    except OSError:
        return None


if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Program needs administrative privileges.")
        sys.exit()

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='A small script to change MAC addresses in Windows',
                                     epilog='Note:\nWiFi Connections might need a 02 as first octet, e.g. 02:xx:xx:xx:xx:xx'
                                            '\n\nExample usage:\n'+sys.argv[0]+' -l'
                                            '\n'+sys.argv[0]+' -i CA8D7884-4754-4E6D-B637-D411533ECBBA -m 00:0C:29:FE:8B:77'
                                            '\n'+sys.argv[0]+' -i CA8D7884-4754-4E6D-B637-D411533ECBBA -m 00:0C:29:FE:8B:77 -f'
                                            '\n'+sys.argv[0]+' -i CA8D7884-4754-4E6D-B637-D411533ECBBA -r'
                                            '\n'+sys.argv[0]+' -i CA8D7884-4754-4E6D-B637-D411533ECBBA -f'
                                            '\n'+sys.argv[0]+' -i CA8D7884-4754-4E6D-B637-D411533ECBBA -r -f')
    parser.add_argument("-l", "--list", action="store_true", help="list all network interfaces")
    parser.add_argument("-r", "--reset", action="store_true",
                        help="reset MAC address of the provided network interface to default")
    parser.add_argument('-i', "--interface", action='store',
                        help='provide an interface GUID (part of the "Transport Name"),'
                             ' e.g. CA8D7884-4754-4E6D-B637-D411533ECBBA')
    parser.add_argument('-m', "--mac", action='store', help='provide a valid MAC address, e.g. 00:0C:29:FE:8B:77. Might need 02 as the first octet for Wifi.')
    parser.add_argument("-f", "--force", action="store_true", help="force restart network interface")

    args = parser.parse_args()

    if args.list:
        list_all_interfaces_guid()
    elif args.mac and args.interface and args.force:
        set_mac_value(args.mac, args.interface)
        restart_network_interface(args.interface)
    elif args.mac and args.interface:
        set_mac_value(args.mac, args.interface)
        print("You might need to restart your network interface to complete the MAC change. Use -i and -f for that")
    elif args.reset and args.interface and args.force:
        remove_mac_value(args.interface)
        restart_network_interface(args.interface)
    elif args.reset and args.interface:
        remove_mac_value(args.interface)
        print("You might need to restart your network interface to complete the MAC change back to the default MAC. Use -i and -f for that.")
    elif args.force and args.interface:
        restart_network_interface(args.interface)
    else:
        print("Invalid command, try -h or --help.")
