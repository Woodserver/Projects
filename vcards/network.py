import subprocess
import platform

print("""!!!!! Results for CR-MC-NR9681-01 !!!!!                                
           /
           /                           
         O                                    
        /|\                                   
        / \ """)                                 

def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False
camera_ips = (94,90,51,43)

if __name__ == '__main__':
    for last_octet in camera_ips:
        current_ip_address = [f'10.10.10.{last_octet}']
        for each in current_ip_address:
            if ping_ip(each):
             print(f"10.10.10.{last_octet} is UP")
            else:
                print(f"10.10.10.{last_octet} is DOWN")