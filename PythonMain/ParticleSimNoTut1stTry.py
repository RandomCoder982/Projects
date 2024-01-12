import pygame
import math
pygame.init()

width, height =  800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("OOP Testing")

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (100, 149, 237)
red = (188, 39, 50)
darkGrey = (80, 78, 81)

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text, textColor):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.textColor = textColor

    def draw(self, surface):
        # Draw the button
        surface.blit(self.image, self.rect.topleft)

        # Render and draw the text with black color
        text_surface = self.font.render(self.text, True, self.textColor)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

class Particle:
    g = .1
    timeStep = .1

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.xVel = 0
        self.yVel = 0


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def attraction(self, other):
        x = other.x
        y = other.y
        
        dstX = x - self.x
        dstY = y - self.y

        dst = math.sqrt(dstY**2 + dstX**2)
        force = self.g * self.mass * other.mass / dst**2
        
        theta = math.atan2(dstY, dstX) 
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def updatePositions(self, particles):
        total_fx = total_fy = 0
		
        for particle in particles:
            if self == particle:
                continue

            fx, fy = self.attraction(particle)
            total_fx += fx
            total_fy += fy

        self.xVel += total_fx / self.mass * self.timeStep
        self.yVel += total_fy / self.mass * self.timeStep

        self.x += self.xVel * self.timeStep
        self.y += self.yVel * self.timeStep

# button = Button(300, 200, 200, 300, white, "Blah blah blahbl bjlsfdhsibnvsfhivhdfvbhdfvib vib !", black)

# allSprites = pygame.sprite.Group()
# allSprites.add(button)

def main():
    run = True
    clock = pygame.time.Clock()
    clock.tick(60)

    partic = Particle(width/2, height/2, 15, darkGrey, 50)
    secon = Particle(width/3, height/2, 50, blue, 10)
    particles = [partic, secon]

    while run:
        screen.fill(black)
    
         
        for particle in particles:
            particle.updatePositions(particles)
            particle.draw(screen)

        # allSprites.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if button.rect.collidepoint(event.pos):
            #         print("Button Clicked!")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()
    
    pygame.quit()

main()
    

    

   