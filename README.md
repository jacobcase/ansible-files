# ansible-files
My Ansible playbooks for...whatever I need.


### TODO
* Apt-Cacher-Server. Also give other Vagrant boxes the ability to use it.
* Sharded Mongo
* Secure Mongo
* Basic Firewall setup. Use Jinja, iptables persist, etc
* OpenStack........
* Postgresql with BDR
* Investigate and possibly implement pgpool II for HA
* etc, etc


### Issues
* Docker module doesn't restart container when a volume changes (may be fixed, need to invesigate)
* Cannot use default(omit) with variables that are part of a string
