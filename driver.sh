#!/usr/bin/env bash
python monrp1_8192.py &
python monrp2_8192.py &
python monrp3_8192.py &
python monrp4_8192.py &
python pom3a_8192.py &
python pom3b_8192.py &
python pom3c_8192.py &
python pom3d_8192.py &
python xomo_all_8192.py &
python xomo_flight_8192.py &
python xomo_ground_8192.py &
python xomo_osp2_8192.py &
python xomo_osp_8192.py &

wait

echo "Finished"