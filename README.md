# Space Evaders (basic name, it will get changed quite a few times)
## A space-shooter pixel art game made in Python with Pygame

## Important
> This game is still in the very early stage of development, the pixel art isn't done at all, nor is the code, I'm just implementing the needed stuff for now

## TODO list:
- [x] Bullet projectiles shooting at a spread pattern (only thing I had to do was get a random int from the spread range with `random.randint(-spread, spread)` and added it to the X and Y pos of the bullet rect
- [ ] Gas mechanic, the next round starts only when the player has killed every enemy rocket, so that the game can be endless without the need for levels
- [ ] Small shake when destroying an enemy rocket
- [ ] Medium shake when getting hit
- [ ] Big shake when your rocket gets destroyed
- [ ] Upgrading your rocket
  - [ ] Faster bullets
  - [ ] Stronger bullets
  - [ ] Buying new / different rockets
    - [ ] Multi shooting
  - [ ] More HP
  - [ ] Less spread
  - [ ] Spawning with a certain power up
- [ ] Set gun positions for every rocket type
  - [ ] Shoot position is up/below according to the aim direction (y-/+1)
- [ ] Power ups 
  - [ ] Multi shooting
  - [ ] Faster bullets
  - [ ] Explosive bullets
  - [ ] Freezing bullets
- [ ] Pausing the game
  - [ ] Having a pause menu with a 80% opacity black background so that the game is visible behind being paused
- [ ] Multiple menus (settings, main menu, game menu, pause menu)
- [ ] Different types of enemies
- [x] Learn angle projectiles for the enemy shooting [(the video I learned with)](https://youtu.be/3DeW-7vbc50)
- [ ] Do it OOP
- [ ] Saving progress in a json db 
