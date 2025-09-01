import pygame
import random
import math
import sys

# --- Constants ---
WIDTH, HEIGHT = 1280, 720
FPS = 60
PLAYER_SIZE = 40
PLAYER_SPEED = 5
PLAYER_HEALTH = 100
BULLET_SPEED = 12
BULLET_SIZE = 8
BULLET_DAMAGE = 25
ENEMY_COUNT = 20
ENEMY_SIZE = 38
ENEMY_SPEED = 2.5
ENEMY_HEALTH = 80
ZONE_SHRINK_TIME = 10  # seconds
ZONE_SHRINK_AMOUNT = 120  # pixels
ZONE_MIN_RADIUS = 180
LOOT_COUNT = 30
LOOT_SIZE = 28
HEALTH_PACK_AMOUNT = 40
AMMO_PACK_AMOUNT = 10
MAX_AMMO = 60
MAX_HEALTH = 100
FONT_NAME = "arial"
GAME_TITLE = "Battle Royale 2D"

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (60, 220, 60)
RED = (220, 60, 60)
BLUE = (60, 60, 220)
YELLOW = (220, 220, 60)
GRAY = (120, 120, 120)
DARK_GRAY = (40, 40, 40)
ORANGE = (255, 140, 0)
CYAN = (0, 255, 255)
PURPLE = (180, 60, 220)

# --- Assets ---
def load_assets():
    assets = {}
    assets['player'] = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
    pygame.draw.circle(assets['player'], BLUE, (PLAYER_SIZE//2, PLAYER_SIZE//2), PLAYER_SIZE//2)
    pygame.draw.rect(assets['player'], WHITE, (PLAYER_SIZE//2-4, 0, 8, PLAYER_SIZE//2))
    assets['enemy'] = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE), pygame.SRCALPHA)
    pygame.draw.circle(assets['enemy'], RED, (ENEMY_SIZE//2, ENEMY_SIZE//2), ENEMY_SIZE//2)
    pygame.draw.rect(assets['enemy'], BLACK, (ENEMY_SIZE//2-4, 0, 8, ENEMY_SIZE//2))
    assets['bullet'] = pygame.Surface((BULLET_SIZE, BULLET_SIZE), pygame.SRCALPHA)
    pygame.draw.circle(assets['bullet'], YELLOW, (BULLET_SIZE//2, BULLET_SIZE//2), BULLET_SIZE//2)
    assets['health_pack'] = pygame.Surface((LOOT_SIZE, LOOT_SIZE), pygame.SRCALPHA)
    pygame.draw.rect(assets['health_pack'], GREEN, (0, 0, LOOT_SIZE, LOOT_SIZE))
    pygame.draw.rect(assets['health_pack'], WHITE, (LOOT_SIZE//4, LOOT_SIZE//2-4, LOOT_SIZE//2, 8))
    pygame.draw.rect(assets['health_pack'], WHITE, (LOOT_SIZE//2-4, LOOT_SIZE//4, 8, LOOT_SIZE//2))
    assets['ammo_pack'] = pygame.Surface((LOOT_SIZE, LOOT_SIZE), pygame.SRCALPHA)
    pygame.draw.rect(assets['ammo_pack'], ORANGE, (0, 0, LOOT_SIZE, LOOT_SIZE))
    pygame.draw.rect(assets['ammo_pack'], BLACK, (LOOT_SIZE//4, LOOT_SIZE//2-4, LOOT_SIZE//2, 8))
    return assets

# --- Utility Functions ---
def clamp(val, minv, maxv):
    return max(minv, min(val, maxv))

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def angle_to(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])

def random_pos_in_circle(center, radius):
    angle = random.uniform(0, 2*math.pi)
    r = radius * math.sqrt(random.uniform(0, 1))
    x = center[0] + r * math.cos(angle)
    y = center[1] + r * math.sin(angle)
    return (int(x), int(y))

# --- Classes ---
class Player:
    def __init__(self, pos):
        self.x, self.y = pos
        self.health = PLAYER_HEALTH
        self.ammo = 30
        self.alive = True
        self.angle = 0
        self.reload_cooldown = 0
        self.shoot_cooldown = 0

    def move(self, dx, dy, zone):
        nx = clamp(self.x + dx, zone.x - zone.radius + PLAYER_SIZE//2, zone.x + zone.radius - PLAYER_SIZE//2)
        ny = clamp(self.y + dy, zone.y - zone.radius + PLAYER_SIZE//2, zone.y + zone.radius - PLAYER_SIZE//2)
        self.x, self.y = nx, ny

    def update(self, dt, zone):
        if self.reload_cooldown > 0:
            self.reload_cooldown -= dt
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
        # Zone damage
        if distance((self.x, self.y), (zone.x, zone.y)) > zone.radius:
            self.health -= 10 * dt
            if self.health <= 0:
                self.alive = False

    def shoot(self, target):
        if self.ammo > 0 and self.shoot_cooldown <= 0:
            self.ammo -= 1
            self.shoot_cooldown = 0.18
            ang = angle_to((self.x, self.y), target)
            return Bullet((self.x, self.y), ang, BULLET_SPEED, BULLET_DAMAGE, 'player')
        return None

    def reload(self):
        if self.reload_cooldown <= 0 and self.ammo < MAX_AMMO:
            self.ammo = MAX_AMMO
            self.reload_cooldown = 1.2

    def draw(self, surf, assets):
        rotated = pygame.transform.rotate(assets['player'], -math.degrees(self.angle))
        rect = rotated.get_rect(center=(self.x, self.y))
        surf.blit(rotated, rect.topleft)

class Enemy:
    def __init__(self, pos):
        self.x, self.y = pos
        self.health = ENEMY_HEALTH
        self.alive = True
        self.angle = 0
        self.shoot_cooldown = random.uniform(0.5, 1.5)
        self.target = None

    def update(self, dt, player, zone):
        if not self.alive:
            return
        # Move towards player if in zone
        if distance((self.x, self.y), (zone.x, zone.y)) > zone.radius:
            # Move to zone center
            ang = angle_to((self.x, self.y), (zone.x, zone.y))
            self.x += math.cos(ang) * ENEMY_SPEED * dt * 60
            self.y += math.sin(ang) * ENEMY_SPEED * dt * 60
        else:
            ang = angle_to((self.x, self.y), (player.x, player.y))
            self.x += math.cos(ang) * ENEMY_SPEED * dt * 60
            self.y += math.sin(ang) * ENEMY_SPEED * dt * 60
            self.angle = ang
        # Zone damage
        if distance((self.x, self.y), (zone.x, zone.y)) > zone.radius:
            self.health -= 10 * dt
            if self.health <= 0:
                self.alive = False
        # Shooting
        self.shoot_cooldown -= dt
        if self.shoot_cooldown <= 0 and distance((self.x, self.y), (player.x, player.y)) < 400:
            self.shoot_cooldown = random.uniform(0.7, 1.5)
            return Bullet((self.x, self.y), self.angle, BULLET_SPEED-2, BULLET_DAMAGE-10, 'enemy')
        return None

    def draw(self, surf, assets):
        rotated = pygame.transform.rotate(assets['enemy'], -math.degrees(self.angle))
        rect = rotated.get_rect(center=(self.x, self.y))
        surf.blit(rotated, rect.topleft)

class Bullet:
    def __init__(self, pos, angle, speed, damage, owner):
        self.x, self.y = pos
        self.angle = angle
        self.speed = speed
        self.damage = damage
        self.owner = owner
        self.alive = True

    def update(self, dt):
        self.x += math.cos(self.angle) * self.speed * dt * 60
        self.y += math.sin(self.angle) * self.speed * dt * 60

    def draw(self, surf, assets):
        rect = assets['bullet'].get_rect(center=(self.x, self.y))
        surf.blit(assets['bullet'], rect.topleft)

class Loot:
    def __init__(self, pos, loot_type):
        self.x, self.y = pos
        self.type = loot_type
        self.collected = False

    def draw(self, surf, assets):
        if self.type == 'health':
            img = assets['health_pack']
        else:
            img = assets['ammo_pack']
        rect = img.get_rect(center=(self.x, self.y))
        surf.blit(img, rect.topleft)

class Zone:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.target_x = x
        self.target_y = y
        self.target_radius = radius
        self.shrink_timer = ZONE_SHRINK_TIME
        self.shrinking = False

    def update(self, dt):
        self.shrink_timer -= dt
        if self.shrink_timer <= 0 and not self.shrinking and self.radius > ZONE_MIN_RADIUS:
            # Pick new zone center and radius
            self.target_radius = max(ZONE_MIN_RADIUS, self.radius - ZONE_SHRINK_AMOUNT)
            angle = random.uniform(0, 2*math.pi)
            dist = random.uniform(0, self.radius - self.target_radius)
            self.target_x = clamp(self.x + math.cos(angle)*dist, self.target_radius, WIDTH-self.target_radius)
            self.target_y = clamp(self.y + math.sin(angle)*dist, self.target_radius, HEIGHT-self.target_radius)
            self.shrinking = True
        if self.shrinking:
            # Smoothly move and shrink
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            dr = self.target_radius - self.radius
            step = dt * 80
            if abs(dx) < step and abs(dy) < step and abs(dr) < step:
                self.x = self.target_x
                self.y = self.target_y
                self.radius = self.target_radius
                self.shrinking = False
                self.shrink_timer = ZONE_SHRINK_TIME
            else:
                self.x += clamp(dx, -step, step)
                self.y += clamp(dy, -step, step)
                self.radius += clamp(dr, -step, step)

    def draw(self, surf):
        pygame.draw.circle(surf, CYAN, (int(self.x), int(self.y)), int(self.radius), 4)

# --- Game Functions ---
def draw_hud(surf, player, enemies, zone, font):
    # Health bar
    pygame.draw.rect(surf, DARK_GRAY, (30, 30, 220, 32))
    pygame.draw.rect(surf, RED, (32, 32, 216 * clamp(player.health, 0, MAX_HEALTH)/MAX_HEALTH, 28))
    health_text = font.render(f"Health: {int(player.health)}", True, WHITE)
    surf.blit(health_text, (40, 34))
    # Ammo
    pygame.draw.rect(surf, DARK_GRAY, (30, 70, 120, 28))
    pygame.draw.rect(surf, ORANGE, (32, 72, 116 * clamp(player.ammo, 0, MAX_AMMO)/MAX_AMMO, 24))
    ammo_text = font.render(f"Ammo: {player.ammo}", True, WHITE)
    surf.blit(ammo_text, (40, 74))
    # Enemies left
    enemies_left = sum(1 for e in enemies if e.alive)
    enemies_text = font.render(f"Enemies: {enemies_left}", True, WHITE)
    surf.blit(enemies_text, (WIDTH-200, 30))
    # Zone timer
    zone_text = font.render(f"Zone: {int(zone.shrink_timer)}s", True, CYAN)
    surf.blit(zone_text, (WIDTH-200, 70))

def draw_minimap(surf, player, enemies, zone):
    scale = 0.13
    mx, my = WIDTH-180, HEIGHT-180
    pygame.draw.rect(surf, DARK_GRAY, (mx-10, my-10, 170, 170))
    # Zone
    pygame.draw.circle(surf, CYAN, (mx+75, my+75), int(zone.radius*scale), 2)
    # Player
    pygame.draw.circle(surf, BLUE, (int(mx+75 + (player.x-zone.x)*scale), int(my+75 + (player.y-zone.y)*scale)), 7)
    # Enemies
    for e in enemies:
        if e.alive:
            pygame.draw.circle(surf, RED, (int(mx+75 + (e.x-zone.x)*scale), int(my+75 + (e.y-zone.y)*scale)), 5)

def draw_gameover(surf, font, win):
    msg = "Victory Royale!" if win else "Game Over"
    text = font.render(msg, True, YELLOW if win else RED)
    rect = text.get_rect(center=(WIDTH//2, HEIGHT//2-40))
    surf.blit(text, rect)
    tip = font.render("Press R to Restart or ESC to Quit", True, WHITE)
    rect2 = tip.get_rect(center=(WIDTH//2, HEIGHT//2+20))
    surf.blit(tip, rect2)

def spawn_loot(zone, count):
    loot = []
    for _ in range(count):
        loot_type = random.choice(['health', 'ammo'])
        pos = random_pos_in_circle((zone.x, zone.y), zone.radius-LOOT_SIZE)
        loot.append(Loot(pos, loot_type))
    return loot

def check_collision(a, b, size_a, size_b):
    return distance((a.x, a.y), (b.x, b.y)) < (size_a//2 + size_b//2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(FONT_NAME, 28)
    assets = load_assets()

    def reset_game():
        zone = Zone(WIDTH//2, HEIGHT//2, min(WIDTH, HEIGHT)//2-40)
        player = Player(random_pos_in_circle((zone.x, zone.y), zone.radius-PLAYER_SIZE))
        enemies = [Enemy(random_pos_in_circle((zone.x, zone.y), zone.radius-ENEMY_SIZE)) for _ in range(ENEMY_COUNT)]
        bullets = []
        loot = spawn_loot(zone, LOOT_COUNT)
        return zone, player, enemies, bullets, loot

    zone, player, enemies, bullets, loot = reset_game()
    gameover = False
    win = False

    while True:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if gameover:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        zone, player, enemies, bullets, loot = reset_game()
                        gameover = False
                        win = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if not gameover:
            # Player movement
            dx = dy = 0
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                dy -= PLAYER_SPEED
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                dy += PLAYER_SPEED
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                dx -= PLAYER_SPEED
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                dx += PLAYER_SPEED
            if dx != 0 or dy != 0:
                norm = math.hypot(dx, dy)
                dx, dy = dx/norm*PLAYER_SPEED, dy/norm*PLAYER_SPEED
            player.move(dx, dy, zone)
            # Player aim
            player.angle = angle_to((player.x, player.y), (mx, my))
            # Shooting
            if pygame.mouse.get_pressed()[0]:
                bullet = player.shoot((mx, my))
                if bullet:
                    bullets.append(bullet)
            # Reload
            if keys[pygame.K_r]:
                player.reload()
            # Update player
            player.update(dt, zone)
            # Update zone
            zone.update(dt)
            # Update enemies
            for e in enemies:
                bullet = e.update(dt, player, zone)
                if bullet:
                    bullets.append(bullet)
            # Update bullets
            for b in bullets:
                b.update(dt)
            # Bullet collisions
            for b in bullets:
                if not b.alive:
                    continue
                if b.owner == 'player':
                    for e in enemies:
                        if e.alive and check_collision(b, e, BULLET_SIZE, ENEMY_SIZE):
                            e.health -= b.damage
                            b.alive = False
                            if e.health <= 0:
                                e.alive = False
                            break
                elif b.owner == 'enemy':
                    if player.alive and check_collision(b, player, BULLET_SIZE, PLAYER_SIZE):
                        player.health -= b.damage
                        b.alive = False
                        if player.health <= 0:
                            player.alive = False
            # Remove dead bullets
            bullets = [b for b in bullets if 0 < b.x < WIDTH and 0 < b.y < HEIGHT and b.alive]
            # Loot collection
            for l in loot:
                if not l.collected and check_collision(player, l, PLAYER_SIZE, LOOT_SIZE):
                    if l.type == 'health' and player.health < MAX_HEALTH:
                        player.health = clamp(player.health + HEALTH_PACK_AMOUNT, 0, MAX_HEALTH)
                        l.collected = True
                    elif l.type == 'ammo' and player.ammo < MAX_AMMO:
                        player.ammo = clamp(player.ammo + AMMO_PACK_AMOUNT, 0, MAX_AMMO)
                        l.collected = True
            # Remove collected loot
            loot = [l for l in loot if not l.collected]
            # Check win/lose
            if not player.alive:
                gameover = True
                win = False
            elif all(not e.alive for e in enemies):
                gameover = True
                win = True

        # --- Drawing ---
        screen.fill(GRAY)
        # Draw zone
        zone.draw(screen)
        # Draw loot
        for l in loot:
            l.draw(screen, assets)
        # Draw enemies
        for e in enemies:
            if e.alive:
                e.draw(screen, assets)
        # Draw player
        if player.alive:
            player.draw(screen, assets)
        # Draw bullets
        for b in bullets:
            b.draw(screen, assets)
        # Draw HUD
        draw_hud(screen, player, enemies, zone, font)
        draw_minimap(screen, player, enemies, zone)
        # Game over
        if gameover:
            draw_gameover(screen, font, win)
        pygame.display.flip()

if __name__ == "__main__":
    main()