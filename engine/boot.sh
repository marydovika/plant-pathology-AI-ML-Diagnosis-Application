kill -9 $(lsof -t -i:5000)
echo killed pre
python plant_detection.py &
cd ..
cd gui
npm start
kill -9 $(lsof -t -i:5000)
echo killed
