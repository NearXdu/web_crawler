ls -l | awk '{if ($5==0) cnt++;} END {print cnt}'
