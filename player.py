from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle(),2 )
    # in the player class
    def triangle(self):
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.forward() * self.radius
        b = self.position - self.forward() * self.radius - right
        c = self.position - self.forward() * self.radius + right
        return [a, b, c]
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt
    def forward(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt, -1)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
    def move(self, dt, direction=1):
        self.position += self.forward() * PLAYER_SPEED * dt * direction
    
    def shoot(self):
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
        