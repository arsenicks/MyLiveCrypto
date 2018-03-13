#!/bin/bash
#License:GPLv3
# $1=Fedora Release # (example 27) $2=DATECODE (20180305) both of which is give # via commandline when starting the script. (example sudo # ./buildmedia-all.sh 27 20180305 )
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
setenforce 0

mkdir /srv/Livecds/$2 &&
mkdir /var/www/html/Testing/$2 &&
cd /srv/Livecds/$2/ &&
rm -rf /var/lib/mock/fedora-27-x86_64/root/var/lmc &&

echo "starting 64bits MyLiveCrypto Build"
mock -r fedora-27-x86_64 --old-chroot --shell "livemedia-creator --ks /fedora-kickstarts/Fedora-MyLiveCrypto.ks --no-virt --resultdir /var/lmc --project Fedora-work-mylivecrypto --make-iso --volid Fedora-mylivecrypto-27 --iso-only --iso-name Fedora-mylivecrypto-27-x86_64-1.iso --releasever 27 --title Fedora-MyLiveCrypto-live --macboot"

cp /var/lib/mock/fedora-27-x86_64/root/var/lmc/*.iso /srv/Livecds/$2/ &&
sleep 120 &&
ls /srv/Livecds/$2/ &&
rm -rf /var/lib/mock/fedora-27-x86_64/root/var/lmc &&

echo "work Done"

echo "starting Checksum"
cd /srv/Livecds/$2/
sha512sum *.iso >CHECKSUM512-$2 

#test iso qemu-kvm -m 1024 -smp 2 -cdrom ./lmc-live-workstation.iso

