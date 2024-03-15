cd path/tic-tac-toe-game

docker build --tag tic-tac-toe-game .

docker run tic-tac-toe-game

docker run -ti --rm \
       -e DISPLAY=$DISPLAY \
       -v /tmp/.X11-unix:/tmp/.X11-unix \
       firefox



docker rm tic-tac-toe-game
