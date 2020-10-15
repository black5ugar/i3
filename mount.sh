#!/bin/expect

set timeout 30

# show the disks
spawn udisksctl mount -b /dev/sdb1

expect "Password:"

send "your password\r"

interact

spawn udisksctl mount -b /dev/sdb2

expect "Password:"

send "your password\r"

interact


