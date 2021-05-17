"""
Source:
	Create new volume - YES
	Delete volume on Instance Delete - YES
	Image: Ubuntu 20.04 - 2021.03.23

Flavor:
	ssc.medium

Network:
	UPPMAX 2020/1-3 Internal IPv4 Network

Security Groups:
	- default: UPPMAX 2020/1-3 default security group
	- DE-II_13-docker-swarm - 5a715cc4-1de1-4242-bd38-7948c093a1f1

Key Pair
	- DE-II_13

Configuration:
	- cloud-cfg.yml

Floating ip:
	- ADD
"""

"""
Make sure that the following is installed (Ubuntu 20.04):
	- sudo add-apt-repository cloud-archive:wallaby
    - sudo apt install nova-compute
    - sudo apt install python3-openstackclient
"""

import time, os, sys, random
import inspect
from os import environ as env

from novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

server_name = "project_group_13_vm"+str(random.randint(1000,9999))
flavor = "ssc.medium" 
private_net = "UPPMAX 2020/1-3 Internal IPv4 Network"
floating_ip_pool_name = None
floating_ip = None
image_name = "Ubuntu 20.04 - 2021.03.23"

loader = loading.get_plugin_loader('password')

auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                project_domain_id=env['OS_PROJECT_DOMAIN_ID'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'])

sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)
print ("user authorization completed.")

image = nova.glance.find_image(image_name)

flavor = nova.flavors.find(name=flavor)

if private_net != None:
    net = nova.neutron.find_network(private_net)
    nics = [{'net-id': net.id}]
else:
    sys.exit("private-net not defined.")

cfg_file_path =  os.getcwd()+'/cloud-cfg.yml'
if os.path.isfile(cfg_file_path):
    userdata = open(cfg_file_path)
else:
    sys.exit("cloud-cfg.yml is not in current working directory")

secgroups = ['default', 'DE-II_13-docker-swarm']

print ("Creating instance ... ")

instance = nova.servers.create(name=server_name, image=image, flavor=flavor, key_name='DE-II_13',userdata=userdata, nics=nics, security_groups=secgroups)
inst_status = instance.status

print ("waiting for 10 seconds.. ")
time.sleep(10)

while inst_status == 'BUILD':
    print ("Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more...")
    time.sleep(5)
    instance = nova.servers.get(instance.id)
    inst_status = instance.status

print ("Instance: "+ instance.name +" is in " + inst_status + " state")