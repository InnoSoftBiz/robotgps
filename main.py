import math

import  pygame
import calcu as ca
import pygameGUI as gui
import read_filewaypoint as mp
import line

pygame.init()

rmp = mp.read_mp("mainpath.waypoints") #mainpath.waypoints
waypoint = rmp
Nwaypoint = []
#print(len(waypoint))

window = (1200, 720)
environment = gui.Envir(window)
running = True

dt = 0
lasttime = pygame.time.get_ticks()

clock = pygame.time.Clock()

for i in range(len(waypoint)-1):
    calculate = ca.waypoints(waypoint[i],waypoint[i+1])
    calculate.haversine()
    calculate.bearing()
    der = calculate.destination(waypoint[i])
    Nwaypoint.append(waypoint[i])
    #print((waypoint[i],waypoint[i+1]),calculate.haversine())

    for j in range(der[0]):
        pos = der[2]
        Nwaypoint.append(pos)
        der = calculate.destination(waypoint[i])
Nwaypoint.append(waypoint[len(waypoint)-1])
print(Nwaypoint)
start = (environment.draw_path(waypoint, Nwaypoint)[0])
robot = gui.Robot(start, r"SpeVm6L - Imgur.png", 80)

def main():
    pygame.display.update()
    environment.map.fill(environment.black)
    environment.draw_path(waypoint, Nwaypoint)
    robot.draw(environment.map)
    environment.write_info(int(robot.vl), int(robot.vr), robot.theta)
    #environment.robot_frame((robot.x, robot.y), robot.theta)
    environment.trail((robot.x, robot.y))
    # if robot.vl != robot.vr:
    #     print(robot.vl, robot.vr)
    #print(robot.x, robot.y)


point = environment.draw_path(waypoint, Nwaypoint).copy()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    line.Line_kml(Nwaypoint)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if len(point) > 0:
            target_point = point[0]
            robot.following(target_point)
            robot.move(dt)
            #print((robot.x, robot.y))

            if math.dist((robot.x, robot.y), target_point) < 20:
                point.pop(0)

        dt = (pygame.time.get_ticks() - lasttime)/1000
        lasttime = pygame.time.get_ticks()
        main()
        #clock.tick(20)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
