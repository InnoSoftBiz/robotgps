import pygame
import math
import numpy as np

class Robot:
    def __init__(self, startpos, robotimg, width, follow=None):
        self.m2p = 3779.52  # from meter to pixels\
        self.width = width
        self.x, self.y = startpos
        self.theta = 0
        self.w = 0  # angular velocity (rad/sec)
        self.u = 0  # linear velocity (pixels/sec)
        self.a = 8.4
        self.img = pygame.image.load(robotimg)  # skin img path provided in the arguments
        self.follow = follow
        self.vr = 0
        self.vl = 0

    def following(self, point):
        target_x, target_y = point
        delta_x = target_x - self.x
        delta_y = target_y - self.y
        self.u = delta_x * math.cos(self.theta) + delta_y * math.sin(self.theta)
        self.w = (-1 / self.a) * math.sin(self.theta) * delta_x + (1 / self.a) * math.cos(self.theta) * delta_y
        self.vr = self.u + ((self.width / 2) * self.w)
        self.vl = self.u - ((self.width / 2) * self.w)
        #print(self.w, (self.vr-self.vl)/self.width)

    def move(self, dt):
        self.theta += self.w * dt
        self.x += ((self.vl+self.vr)/2) * math.cos(self.theta) * dt
        self.y += ((self.vl+self.vr)/2) * math.sin(self.theta) * dt
        # self.vr = self.u + ((self.width / 2) * self.w)
        # self.vl = self.u - ((self.width / 2) * self.w)

        if self.theta > 2 * math.pi or self.theta < -2 * math.pi:
            self.theta = 0


    def draw(self, surface):
        # Rotate the image according to the robot's orientation
        rotated_img = pygame.transform.rotate(self.img, math.degrees(-self.theta))

        # Get the rectangle enclosing the rotated image and set its center to the robot's position
        rect = rotated_img.get_rect(center=(self.x, self.y))

        # Draw the rotated image onto the surface
        surface.blit(rotated_img, rect)

class Envir:
    def __init__(self, dimentions):
        self.black = (0, 0, 0)
        self.yel = (255, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.width, self.height = dimentions

        pygame.display.set_caption("Differential drive of robot GPS")
        self.map = pygame.display.set_mode((self.width, self.height))

        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = self.font.render('default', True, self.width, self.black)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.width - 600,
                                self.height - 100)

        self.trail_set = []

    def write_info(self, VL, VR, theta):
        txt = f"Vl = {VL} VR = {VR} theta = {int(math.degrees(theta))}"
        self.text = self.font.render(txt, True, self.white, self.black)
        self.map.blit(self.text, self.textRect)

    def trail(self,pos):
        for i in range(len(self.trail_set)-1):
            pygame.draw.line(self.map, self.yel, (self.trail_set[i][0], self.trail_set[i][1]),
                            (self.trail_set[i+1][0], self.trail_set[i+1][1]), 1)
        # if self.trail_set.__sizeof__() > 10000:
        #     self.trail_set.pop(0)
        self.trail_set.append(pos)


    def draw_path(self, main, allpath):
        allpos = np.array(allpath)
        min_lon = allpos[0:len(allpos), 1].min()
        min_lat = allpos[0:len(allpos), 0].min()
        max_lon = allpos[0:len(allpos), 1].max()
        max_lat = allpos[0:len(allpos), 0].max()

        main = np.array(main)
        mmin_lon =  main[0:len(main), 1].min()
        mmin_lat =  main[0:len(main), 0].min()
        mmax_lon =  main[0:len(main), 1].max()
        mmax_lat =  main[0:len(main), 0].max()

        poslist = []
        mainlist = []

        for lat, lon in allpos:
            x = (self.width // 2) + int((lon - min_lon) * self.width / (max_lon - min_lon))
            y = (self.height // 2) + int((lat - min_lat) * self.height / (max_lat - min_lat))
            poslist.append((x//2, y//2))

        for lat, lon in main:
            x = (self.width // 2) + int((lon - mmin_lon) * self.width / (mmax_lon - mmin_lon))
            y = (self.height // 2) + int((lat - mmin_lat) * self.height / (mmax_lat - mmin_lat))
            mainlist.append((x//2, y//2))
        #print(self.map)
        pygame.draw.lines(self.map, self.blue, False, poslist, 2)
        for mains in mainlist:
            pygame.draw.circle(self.map, self.blue, mains, 10)

        return poslist

    def robot_frame(self, pos, rotation):
        n = 40
        centerX, centerY = pos
        x_axis = (centerX + n * math.cos(-rotation), centerY + n * math.sin(-rotation))
        y_axis = (centerX + n * math.cos(-rotation + math.pi / 2), centerY + n * math.sin(-rotation + math.pi / 2))
        pygame.draw.line(self.map, self.red, (centerX, centerY), x_axis, 3)
        pygame.draw.line(self.map, self.green, (centerX, centerY), y_axis, 3)