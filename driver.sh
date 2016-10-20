#!/usr/bin/env bash
python nrp1_100.py &
python nrp1_1024.py &
python nrp1_2048.py &
python nrp1_4096.py &
python nrp1_512.py &
python nrp2_100.py &
python nrp2_1024.py &
python nrp2_2048.py &
python nrp2_4096.py &
python nrp2_512.py &
python nrp3_100.py &
python nrp3_1024.py &
python nrp3_2048.py &
python nrp3_4096.py &
python nrp3_512.py &
python nrp4_100.py &
python nrp4_1024.py &
python nrp4_2048.py &
python nrp4_4096.py &
python nrp4_512.py &


wait

echo "Finished"