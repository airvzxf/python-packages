#!/bin/bash

# Setup variables
now_utf=$(date -u +"%Y.%m.%d.%H.%M.%S.%N")
source_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/"
src_directory="${source_directory}../src/"
file_version="${source_directory}pkg_v${now_utf}.tar.gz"
file_last_version="${source_directory}pkg_last_version.tar.gz"

# Clean all
find ${src_directory} -type d -iname __pycache__ -exec rm -fr {} \;
find ${src_directory} -type f -iname *.pyc* -exec rm -fr {} \;
rm -f ${file_last_version}

# Create file versions
tar -zcf ${file_version} -C ${src_directory} ./pkg/
cp ${file_version} ${file_last_version}
