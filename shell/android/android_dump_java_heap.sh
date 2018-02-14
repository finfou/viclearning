#!/bin/bash

ADB=${ANDROID_HOME}/platform-tools/adb
HPROF_CONV=${ANDROID_HOME}/platform-tools/hprof-conv

function droid_hd() {
	PACKAGE_NAME=$1
	TIME=$(date +"%Y%m%d_%H%M%S")
	FILE_NAME="${PACKAGE_NAME}-${TIME}-heap.hprof"
	PATH_IN_PHONE="/data/local/tmp/${FILE_NAME}"

	${ADB} shell rm ${PATH_IN_PHONE} 2> /dev/null

	echo "Cause GC for ${PACKAGE_NAME}"
	${ADB} shell pkill -l 10 ${PACKAGE_NAME}

	echo "> dump heap for ${PACKAGE_NAME}"
	${ADB} shell "am dumpheap ${PACKAGE_NAME} ${PATH_IN_PHONE}"
	if [[ $? != 0 ]]; then
		echo 
		${ADB} devices
		echo "run command:"
		echo "export ANDROID_SERIAL="
		return
	fi

	sleep 3

	echo "> list heap for ${PATH_IN_PHONE}"
	${ADB} shell ls -lh ${PATH_IN_PHONE}

	echo "> pull to computer"
	${ADB} pull ${PATH_IN_PHONE} ./
	
	echo "> delete device copy"
	${ADB} shell rm ${PATH_IN_PHONE}

	echo "> hprof-conv it"
	${HPROF_CONV} -z ${FILE_NAME} droid-${FILE_NAME}

	echo "> remove tmp hprof"
	mv -f droid-${FILE_NAME} ${FILE_NAME}
	ls -lh ${FILE_NAME}
	echo "Done! file: ${FILE_NAME}"
}
