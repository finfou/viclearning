#! /bin/bash

apkFile=""

# package: name='ALYb.EjGK.ovXLruH' versionCode='484' versionName='1.4.84' platformBuildVersionName=''
packageRealName=`aapt d badging ${apkFile} | awk -f "\'" '{if( $0 ~ "^package"){print $2}}' 2>/dev/null`
