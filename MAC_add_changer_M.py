import random
import string
import subprocess
import optparse
import re



print('''\033[31m

███╗░░░███╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░███████╗░█████╗░██╗░░██╗
████╗░████║██║░░░██║░██║░░██╗░░██║██╔══██╗██╔════╝██╔══██╗██║░██╔╝
██╔████╔██║██║░░░██║░╚██╗████╗██╔╝███████║█████╗░░███████║█████═╝░
██║╚██╔╝██║██║░░░██║░░████╔═████║░██╔══██║██╔══╝░░██╔══██║██╔═██╗░
██║░╚═╝░██║╚██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║░░░░░██║░░██║██║░╚██╗
╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝
                    MAC Address Changer
 ''')



def get_random_mac_address():
    """Generate and return a MAC address in the format of Linux"""
    # get the hexdigits uppercased
    uppercased_hexdigits = ''.join(set(string.hexdigits.lower()))
    # 2nd character must be 0, 2, 4, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:                                                  
                mac += random.choice("02468ace")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":" 
    return mac.strip(":")
# random_mac = get_random_mac_address()
                                                                                                                                                                                                                                                                                                                                                                          


   
# this is a reader that will take a network interface and new mac address
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--interface " , dest="Network_interface" , help= "this option is for network interface")
    parser.add_option("-m" ,"-- MAC " , dest="new_MAC_Address" , help= "this option is for new mac address")
    parser.add_option("-r" , "--random " ,dest= "get_random_mac_address",action = "store_true", help = "Generate and return a MAC address")
    (option , arguments) = parser.parse_args()

    if not option.Network_interface :
         parser.error("\033[31m [-] Please specify an Interface , type --help for more information.")
        
    if not option.new_MAC_Address:
        if option.get_random_mac_address :
            option.new_MAC_Address = get_random_mac_address ()
        else:
            parser.error("\033[31m [-] Please specify a new MAC Address or type -r to get a random MAC Adderss, type --help for more information.")
    
    if not re.match(r"([0-9a-fA-F]{2}[-:]){5}[0-9a-fA-F]{2}$", option.new_MAC_Address):
        parser.error(option.new_MAC_Address + " the new mac address is not valid")

    return option




# system commands to change the mac address for network interface
def mac_changer(network_interface , new_mac_add):
    subprocess.call("ifconfig "+ network_interface  + " down", shell=True)
    subprocess.call("ifconfig "+ network_interface + " hw ether "+ new_mac_add, shell=True)
    subprocess.call("ifconfig "+ network_interface +" up" , shell=True)
    print ("\033[32m [/] changing MAC Address for " + network_interface + " to " + new_mac_add)



#filtering mac address
def check_mac_add(network_interface , new_mac_add):
    ifconfig_result = subprocess.check_output("ifconfig " +  network_interface ,shell=True).decode("UTF-8")
    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
    if mac_address[0] == new_mac_add:
        print("\033[36m [+] MAC Address has changed successfuly to :  " + new_mac_add)
    else:
         print("\033[31m [-] Mac address did not get changed .")


option = get_arguments()
mac_changer(option.Network_interface , option.new_MAC_Address)
check_mac_add(option.Network_interface , option.new_MAC_Address)








 





# if option.get_random_mac_address:
    #      get_random_mac_address()
    # else:
        #  print('[-] please use -m to specify a new MAC Address or -r to random mac address.')    
    # if option.new_mac_add:
    #     return True
    # if option.get_random_mac_address:
    #     random_mac
    # else:
    #     print('[-] please use -m to specify a new MAC Address or -r to random mac address.')