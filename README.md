# gurobi9-linux-installer

The `gurobi9_installer.py` file is a simple script to install gurobi version 9 on a linux machine.

This script is simply the encoding of the instructions found on the [official documentation](https://www.gurobi.com/documentation/9.5/quickstart_linux/software_installation_guid.html).

To use it you have to download the archive containing Gurobi from the [official website](https://www.gurobi.com/downloads/gurobi-software/) and then launch the script passing as an argument the path of where it was downloaded.

For example, if you want to install version 9.5.2:

```bash
$ python gurobi9_installer.py /home/user/Download/gurobi9.5.2_linux64.tar.gz 
```

Gurobi is installed in the `/opt/gurobi9xx` directory (`xx` depends on the version), and environment variables are added to the end of the `.bashrc` file.
