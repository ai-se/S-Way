python pom3a.py &> pom3a.log &
python pom3b.py &> pom3b.log &
python pom3c.py &> pom3c.log &
python pom3d.py &> pom3d.log &
python xomo_flight.py &> xomo_flight.log &
python xomo_ground.py &> xomo_ground.log &
python xomo_osp.py &> xomo_osp.log &
python xomo_osp2.py &> xomo_osp2.log &

wait

echo "Finished"
