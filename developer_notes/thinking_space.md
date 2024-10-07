# Thinking space
>This is where I'll be working out my current problems. 
>This file is a living document, and will be cleared with the various features as they are developed.

## Current feature: 
- Make the asteroids lumpy instead of perfectly round

What questions are there?:
- What is making the asteroids round?
  - [pygame.draw.circle()](https://www.pygame.org/docs/ref/draw.html?highlight=circle#pygame.draw.circle)
- What tools can be used to change their shape?
  - Possible solutions:
    - [pygame.draw.polygon()](https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon)
- Should those tools be standalone or included with something?

- How will this effect the hit box?

### Current discoveries
- Using polygon is a possible, but I need to find a way to have it's coordinates be
    relative to the current asteroids.

Possible solution:
pygame.surface.blit or blits
- Allows you to draw a surface or many surfaces onto another surface.
- I think I'll have to create a surface object that will be the new reference for all the other objects.
  - Then I'll tie the movements and collisions to those surfaces, and draw on them for the visuals.

pygame.draw.lines()
- has a parameter called "closed" where it will add an additional line to close between the first and last drawn.
