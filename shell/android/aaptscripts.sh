#! /bin/bash

apkFile=""

# package: name='ALYb.EjGK.ovXLruH' versionCode='484' versionName='1.4.84' platformBuildVersionName=''
packageRealName=`aapt d badging ${apkFile} | awk -f "\'" '{if( $0 ~ "^package"){print $2}}' 2>/dev/null`

launchableActivity1=`aapt d bading ${apkFile} | awk -f "\'" '{if( $0 ~ "^launchable-activity"}{print $2; exit}}' 2>/dev/null`

appName=`aapt d bading ${apkFile} | awk -f "\'" '{if( $0 ~ "^application:"){print $2}}' | sed s/[[:space:]]//g`

version=`aapt d bading ${apkFile} | awk -f "\'" '{if( $0 ~ "^package"){print $6}}'`

versionCode=`aapt d bading ${apkFile} | awk -f "\'" '{if( $0 ~ "^package"){print $4}}'`

