#!/bin/bash

# SFTP server details

HOST="192.168.146.90"

USERNAME="suresh"

# PASSWORD="your_sftp_password"

REMOTE_DIR="/home/suresh/Downloads/backedup"

LOCAL_DIR="/home/pi/BVPro/videos"

# Log file to record transfer status
LOG_FILE="/home/pi/BVPro/sftp_transfer_log.txt"

# Connect to the SFTP server and transfer files

sftp -oBatchMode=yes -b - "$USERNAME@$HOST" <<EOF >$LOG_FILE

cd $REMOTE_DIR

put $LOCAL_DIR/VID-20230925-WA0008.mp4

quit

EOF

# Check if the transfer was successful

if grep -q "Transfer complete" "$LOG_FILE"; then

    echo "File transfer was successful!"

else

    echo "File transfer failed. Check the log file for details."

fi
