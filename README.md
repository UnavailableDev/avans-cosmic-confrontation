# python-eindopdrachten-23-24-seger-sars-joshua-regnier
python-eindopdrachten-23-24-seger-sars-joshua-regnier created by GitHub Classroom


- Save data
	- Per schip:
		- x, y, horizontaal/verticaal
		- waar geraakt
		- ability available/ already used
		- Cooldown applied from EMP (3 turns)
		- (type)
	- geschoten grid positions
		- Boolean shot/not shot
	- nickname
- Functional tasks
	- [ ] Render grid status
	- [x] Render ships
	- [ ] Save game state to file
	- [ ] Load game state from file
	- [ ] Move ship
	- [ ] Shoot Grid position
		- [ ] Check if ship is on position
	- [x] Menu
	- [ ] Abilities:
		- [ ] 
- GUI
	- Main menu
		- [ ] New game
		- [ ] Continue
		- [ ] Previous games
		- [ ] Nickname config
	- In game
		- [x] Grid
		- [ ] Abilities
		- [ ] End turn
		- [ ] Quit


# TODO:
## sprint 1
- [ ] Pygame @Seger
	- [x] grid (GameBoard class)
	- [x] menu
- [ ] Base class Ship @Joshua
	- [x] Implemented without abilities


## sprint 2
- [x] Render ships

## sprint 3
- [x] Bug fix: ship rendering @Joshua
- [ ] Validate ship movements @Seger
- [ ] Save/Load JSON @Seger
- [ ] Custom nicknames @Seger
- [x] Shoot position @Joshua
- [x] State machine which turn @Joshua
- [x] win/loss condition @Joshua
- [ ] Dynamic board size between 8-16 (always a square shape)
- [ ] Make abilities
- [~] Make AI @Joshua
- [x] Init state where the player (and AI) place their ships on the grid
- [x] fix AI wasting a turn?
- [ ] ability for player to place their own ships


## Feature request:
- [ ] reduce windows size, or dynamically change it correctly
- [ ] Show ship head/tail for recognition
