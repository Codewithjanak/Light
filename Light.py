import pygame , math 

# Initialize the grid
def initialize_grid(WIDTH,HEIGHT):
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]  # Start with no light (opacity 0)
  
# Add a light source
def apply_light(grid, light_pos, light_radius, light_intensity,WIDTH,HEIGHT):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Calculate the distance from the light source
            distance = math.sqrt((x - light_pos[0])**2 + (y - light_pos[1])**2)

            # If within the light radius, calculate light effect
            if distance < light_radius:
                brightness = max(0, light_intensity * (1 - distance / light_radius))  # Linear falloff
                grid[y][x] = min(255, grid[y][x] + brightness)  # Clamp to 255
    return grid

# Draw the grid on the screen
def draw_grid(screen, grid,WIDTH,HEIGHT,PIXEL_SIZE=1):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Use the light value to set the color of the pixel
            brightness = grid[y][x]
            color = (brightness, brightness, brightness)  # Grayscale
            img = pygame.Surface((1,1),pygame.SRCALPHA)
            img.fill((0,0,0,255 - brightness))
            screen.blit(img,(x *PIXEL_SIZE,y *PIXEL_SIZE))
            #pygame.draw.rect(screen, color, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))      
            
def run (screen,WIDTH,HEIGHT,light_radius,light_intensity = 255 ):
    # Reset the grid
    grid = initialize_grid(WIDTH,HEIGHT)

        # Get mouse position and convert to grid position
    light_pos = pygame.mouse.get_pos()

        # Apply light to the grid
    grid = apply_light(grid, light_pos, light_radius, light_intensity,WIDTH,HEIGHT)

        # Draw the updated grid
    
    draw_grid(screen, grid,WIDTH,HEIGHT)    
    