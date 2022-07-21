import os
import pathlib
import re
import sys


def check(is_valid: bool, error_msg: str) -> None:
    if not is_valid:
        print(error_msg)
        exit(0)


n_args = len(sys.argv) - 1

check(os.geteuid() != 0, 'Do not run this script with administrator privileges.')
check(n_args == 1, 'Wrong number of arguments: {} instead of {}.'.format(n_args, 1))

archive_path = pathlib.PosixPath(sys.argv[1])

check(archive_path.exists(), 'File "{}" not found.'.format(archive_path))
check(archive_path.is_file(), 'The input path must point to a file not a folder.')

archive_name = archive_path.name

check(re.match(r'gurobi9\.[0-9]+\.[0-9]+_linux64.tar.gz', archive_name),
    'The file must have the following format: gurobi9.x.x_linux64.tar.gz.')

minor_ver, patch_ver = map(lambda x: x[1:], re.findall(r'\.[0-9]+', archive_name))

print('You need to enter the root password to install gurobi in the /opt folder.')
os.system('sudo tar xfz {} -C /opt/'.format(archive_path))

print('Gurobi installed.')

with open(pathlib.Path.home() / '.bashrc', 'a') as bashrc:
    bashrc.write('\n# Rows added by gurobi9_installer\n')
    bashrc.write('export GUROBI_HOME="/opt/gurobi9{}/linux64"\n'.format(minor_ver + patch_ver))
    bashrc.write('export PATH="${PATH}:${GUROBI_HOME}/bin"\n')

    if 'LD_LIBRARY_PATH' in os.environ:
        bashrc.write('export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${GUROBI_HOME}/lib"\n')
    else:
        bashrc.write('export LD_LIBRARY_PATH="${GUROBI_HOME}/lib"\n')

print('Environment variables added.')
print('Done.')
