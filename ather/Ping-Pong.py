import pygame, random
pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Ping-Pong')

# Класс для создания персонажей
class Characters():
   def __init__(self, color, x, y, width, height, radius, speed):
      self.color = color
      self.x = x
      self.y = y 
      self.width = width
      self.height = height
      self.radius = radius
      self.speed = speed
   def drawing(self, form):
      if form == 'rectang':
         pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
      elif form == 'circle':
         pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
# Проверка слокновений шарика с движущимися поверхностями
def colligions(x_1, x_2, x_3, y_1, y_2, y_3, radius_1, width_2, height_2, height_3):
   # For play_rect_1
   if y_1 in range(y_2 - radius_1 + 1, y_2 + height_2 + radius_1 - 1) and x_1 - radius_1 < x_2 + width_2:
      return True
   elif y_1 in range(y_3 - radius_1 + 1, y_3 + height_3 + radius_1 - 1) and x_1 + radius_1 > x_3:
      return True
   else:
      return False
# Узнаем проекции на X и Y
def legs(name_of_object):
   opposite_leg = name_of_object.speed
   adjacent_leg = name_of_object.speed
   angle_size = random.randrange(30, 61, 15)

   if angle_size == 30:
      opposite_leg *= 2
      adjacent_leg *= 1
   if angle_size == 45:
      opposite_leg *= 1.5
      adjacent_leg *= 1.5
   if angle_size == 60:
      opposite_leg *= 2
      adjacent_leg *= 1

   return opposite_leg, adjacent_leg

def print_text(message, x, y, font = 'vagworld', color = (255, 255, 255), size = 40):
   font_type = pygame.font.SysFont(font, size)
   text = font_type.render(message, True, color)
   window.blit(text, (x, y))

# Создаём сам шарик
main_ball = Characters((255,255,255), 640, 360, 0, 0, 40, 9)
# Создаем игровые прямоугольники
play_rect_1 = Characters((127,255,212), 0, 260, 15, 200, 0, 10)
play_rect_2 = Characters((127,255,212), 1265, 260, 15, 200, 0, 10)
# Проекции на ось X и Y 
# Случойно выбираем одну из четвертей
opposite_leg = int(legs(main_ball)[0])
adjacent_leg = int(legs(main_ball)[1])
what_quater = random.randint(1, 4)

player_1 = 0
player_2 = 0

# Основной цикл
run = True
while run == True:
   pygame.time.delay(30)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

   play_rect_1.drawing('rectang')
   play_rect_2.drawing('rectang')
   main_ball.drawing('circle')
   second_run = False
   print_text('Press SPACE to start the game!', 350, 550)
   print_text('Player 1', 120, 30, color = (255, 255, 153))
   print_text('Player 2', 1000, 30, color = (255, 255, 153))
   print_text(str(player_1), 150, 100, color = (255, 255, 153), size = 50)
   print_text(str(player_2), 1050, 100, color = (255, 255, 153), size = 50)


   btns = pygame.key.get_pressed()
   if btns[pygame.K_SPACE]:
      second_run = True

   while second_run == True:
      pygame.time.delay(30)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
            second_run = False
      colligion = colligions(main_ball.x, play_rect_1.x, play_rect_2.x, main_ball.y, play_rect_1.y, play_rect_2.y, main_ball.radius, play_rect_1.width, play_rect_1.height, play_rect_2.height)
      # Движение шарика и отскоки (от стенок, от ракеток игроков
      if not colligion and what_quater == 1:   # 1 QUATER
         if main_ball.y in range(50, 671):
            main_ball.x -= opposite_leg
            main_ball.y -= adjacent_leg
         elif main_ball.y < 50:
            adjacent_leg *= -1
            main_ball.x -= opposite_leg
            main_ball.y -= adjacent_leg
         elif main_ball.y > 670:
            adjacent_leg *= -1
            main_ball.x -= opposite_leg
            main_ball.y -= adjacent_leg 
      elif colligion and what_quater == 1:
         opposite_leg *= -1
         main_ball.x -= opposite_leg
         main_ball.y -= adjacent_leg
      
      if not colligion and what_quater == 2:   # 2 QUATER
         if main_ball.y in range(50, 671):
            main_ball.x += opposite_leg
            main_ball.y -= adjacent_leg
         elif main_ball.y < 50:
            adjacent_leg *= -1
            main_ball.x += opposite_leg
            main_ball.y -= adjacent_leg
         elif main_ball.y > 670:
            adjacent_leg *= -1
            main_ball.x += opposite_leg
            main_ball.y -= adjacent_leg 
      elif colligion and what_quater == 2:
         opposite_leg *= -1
         main_ball.x += opposite_leg
         main_ball.y -= adjacent_leg

      if not colligion and what_quater == 3:   # 3 QUATER
         if main_ball.y in range(50, 671):
            main_ball.x += opposite_leg
            main_ball.y += adjacent_leg
         elif main_ball.y < 50:
            adjacent_leg *= -1
            main_ball.x += opposite_leg
            main_ball.y += adjacent_leg
         elif main_ball.y > 670:
            adjacent_leg *= -1
            main_ball.x += opposite_leg
            main_ball.y += adjacent_leg 
      elif colligion and what_quater == 3:
         opposite_leg *= -1
         main_ball.x += opposite_leg
         main_ball.y += adjacent_leg

      if not colligion and what_quater == 4:   # 4 QUATER
         if main_ball.y in range(50, 671):
            main_ball.x -= opposite_leg
            main_ball.y += adjacent_leg
         elif main_ball.y < 50:
            adjacent_leg *= -1
            main_ball.x -= opposite_leg
            main_ball.y += adjacent_leg
         elif main_ball.y > 670:
            adjacent_leg *= -1
            main_ball.x -= opposite_leg
            main_ball.y += adjacent_leg 
      elif colligion and what_quater == 4:
         opposite_leg *= -1
         main_ball.x -= opposite_leg
         main_ball.y += adjacent_leg
      
      btns = pygame.key.get_pressed()
      # Движение левого игрока
      if btns[pygame.K_w] and play_rect_1.y != 0:
         play_rect_1.y -= play_rect_1.speed
      if btns[pygame.K_s] and play_rect_1.y != 520:
         play_rect_1.y += play_rect_1.speed
      # Движение правого игрока
      if btns[pygame.K_UP] and play_rect_2.y != 0:
         play_rect_2.y -= play_rect_2.speed
      if btns[pygame.K_DOWN] and play_rect_2.y != 520:
         play_rect_2.y += play_rect_2.speed

      window.fill((0,0,0))
      play_rect_1.drawing('rectang')
      play_rect_2.drawing('rectang')
      main_ball.drawing('circle')

      if main_ball.x <= -50 or main_ball.x >= 1330:
         if main_ball.x <= -50:
            player_2 += 1
         else:
            player_1 += 1
         main_ball.x = 640
         main_ball.y = 360
         play_rect_1.x = 0
         play_rect_1.y = 260
         play_rect_2.x = 1265
         play_rect_2.y = 260
         second_run = False
         window.fill((0,0,0))

      pygame.display.update()
      
   pygame.display.update()
pygame.quit()