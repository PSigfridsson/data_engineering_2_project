# Data Engineering 2 - Project 2
 Github analytic system using a streaming framework
## Starting/using the analytic pipeline
The automation of this project is made possible with docker, cloud-init and the openstackAPI. There is currently
two proper ways to run this analytic streaming project and a manual way. Either using the start_instances.py script provided in the root folder or to provide the cloud-init file to the cloud provider when launching a VM. All three launching methods are described below.

**Note:** to access the flask website and the mongo-express UI, port 5000 respectivly port 8081 needs to be portforwarded when using SSH.

**Note:** the two docker-compose commands can sometimes fail becouse some python library could not be found. Just try to rerun the docker-compose command in this case. Or if you have started the a VM using cloud-init and provied the _cloud-cfg.yaml_ as config file you can write this command to restart the VM and try to run the cloud-init file again: "cloud-init clean --logs --reboot". You can check the status of the cloud-init by writing "cloud-init status".

### Start a SNIC VM by python script
The start_instances.py script, located at the root folder, starts a VM on SNIC. To use this correctly you would need to change the key of the VM (line 83) and you need to download a OpenStack RC file (v3) to get the API Access to the OpenStack. This file needs to be sourced before calling the start_instances.py. After these steps you can run the start_instances.py script to start a VM that automatically gets contextualized and lanches all the needed docker services for the system.
### Providing the cloud-init file at SNIC VM launch
Another solution is to provide the cloud-init configuration file _cloud-cfg.yaml_ (located in the root folder) to the cloud provider when launching a VM. This has been tested with the medium and large flavor on SNIC.
### Manual start using docker and docker-compose
This step requires that the following packages are installed on the machine:
* git
* python3
* python3-pip
* docker
* docker-compose

It is recommended to use the two methods above, but to start the system using the docker-compose we run the following commands:

* git clone https://github.com/PSigfridsson/data_engineering_2_project.git

Step into the repo and execute the following commands:

* sudo docker-compose -f data_engineering_2_project/base-services-config.yaml up -d

Now, wait until the base service pulsar is correctly up and running before adding pulsar functions. Takes approximately 2-3 minutes.

* sudo docker exec -i data_engineering_2_project_pulsar_1 bin/pulsar-admin functions create --py unittestciSplit.py --classname unittestciSplit.unittestciSplit --inputs persistent://public/default/q3-q4-topic --tenant public --namespace default
* sudo docker exec -i data_engineering_2_project_pulsar_1 bin/pulsar-admin functions create --py topicSplit.py --classname topicSplit.topicSplit --inputs persistent://public/default/Maintopic --tenant public --namespace default
* sudo docker exec -i data_engineering_2_project_pulsar_1 bin/pulsar-admin functions create --py languageCounter.py --classname languageCounter.languageCounter --inputs persistent://public/default/q1-topic --tenant public --namespace default
* sudo docker exec -i data_engineering_2_project_pulsar_1 bin/pulsar-admin functions create --py unittestCounter.py --classname unittestCounter.unittestCounter --inputs persistent://public/default/q3-output --tenant public --namespace default
* sudo docker exec -i data_engineering_2_project_pulsar_1 bin/pulsar-admin functions create --py unittestciCounter.py --classname unittestciCounter.unittestciCounter --inputs persistent://public/default/q4-output --tenant public --namespace default
* sudo docker exec -i data_engineering_2_project_pulsar_1 bin/pulsar-admin functions create --py commitsCounter.py --classname commitsCounter.commitsCounter --inputs persistent://public/default/q2-topic --tenant public --namespace default

Now, start the services for the producer and the consumers.

* sudo docker-compose -f data_engineering_2_project/pulsar-consumers-producer-config.yaml up -d
