import math
import random

import pygame
import itertools


def getPathDistance(places: list):
    if len(places) < 2:
        return 0.0

    total_distance = 0.0

    # Calculate distance between consecutive points
    for i in range(len(places) - 1):
        x1, y1 = places[i]
        x2, y2 = places[i + 1]
        distance = ((x2 - x1) ** 2 + (y2 - y2) ** 2) ** 0.5
        total_distance += distance

    # Add distance from last point back to start
    x1, y1 = places[-1]
    x2, y2 = places[0]
    distance = ((x2 - x1) ** 2 + (y2 - y2) ** 2) ** 0.5
    total_distance += distance

    return total_distance

def full_TSP(places: list):
    bestRoute = None
    bestDistance = float('inf')
    calculations = 0

    # Fix first point as start, permute the rest
    start = places[0]
    remaining = places[1:]

    all_permutations = generatePermutations(remaining)

    for route in all_permutations:
        # Create full route with fixed start point - convert tuples to lists
        route_list = [start] + [list(point) if isinstance(point, tuple) else point for point in route]
        distance = getPathDistance(route_list)
        calculations += 1

        if distance < bestDistance:
            bestDistance = distance
            bestRoute = route_list

    print(f"There were {calculations} calculations for full TSP")
    return tuple(bestRoute) if bestRoute else tuple(places)
def hueristic_TSP(places: list):
    # Perform a hueristic calculation for traveling salesman.
    # For each node find the closest node to it and assume it is next node then repeat until you have your path.
    # Return the path and print out the number of distance calculations you did.


    calculations = 0
    route = []
    unvisited = places.copy()

    # Start at the first location
    current = unvisited.pop(0)
    route.append(current)

    # While there are still unvisited nodes
    while unvisited:
        closest_distance = float('inf')
        closest_index = 0

        # Find the closest unvisited node to the current node
        for i, place in enumerate(unvisited):
            distance = getDistance(current, place)
            calculations += 1

            if distance < closest_distance:
                closest_distance = distance
                closest_index = i

        # Move to the closest node
        current = unvisited.pop(closest_index)
        route.append(current)

    print(f"there were {calculations} calculations for hueristic TSP")
    return route
def generatePermutations(places : list):
    # a function that given a list will return all possible permutations of the list.
    return list(itertools.permutations(places))


def getDistance(spot1, spot2):
    #Given two coordinates in a plane return the distance between those two points.
    dist = math.sqrt((spot1[0] - spot2[0]) ** 2 + (spot2[1] - spot2[1]) ** 2)
    return dist


def generate_RandomCoordinates(n):
    #Creates a list of random coordinates
    newPlaces = []
    for i in range(n):
        newPlaces.append([random.randint(10,790),random.randint(10,590)])
    return newPlaces

places = [[80,75],[100,520],[530,300],[280,200],[350,150],[700,120],[400,500]]


def DrawExample(places):
    #Draws the TSP showcase to the screen.
    TSP = full_TSP(places.copy())
    Hueristic = hueristic_TSP(places.copy())
    # Initialize Pygame
    pygame.init()
    print(TSP)
    print(Hueristic)
    # Set up the game window
    screen = pygame.display.set_mode((800, 800))
    # Game loop
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render('Hello, Pygame!', True, (0, 0, 0))
    text_surface.set_colorkey((0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (300, 700)  # Center the text on the screen
    # Arguments: text string, antialias boolean (True for smooth edges), text color, optional background color
    text_surface = font.render('Hello, Pygame!', True, (255, 255, 255))  # White text
    while running:
        screen.fill((255,255,255))
        for i in range(len(TSP)-1):
            pygame.draw.line(screen,(255,0,0),(TSP[i][0],TSP[i][1]),(TSP[i+1][0],TSP[i+1][1]),width = 8)
        if len(TSP) >=1:pygame.draw.line(screen, (255, 0, 0), (TSP[0][0], TSP[0][1]), (TSP[-1][0], TSP[-1][1]),width =8)
        for i in range(len(Hueristic) - 1):
            pygame.draw.line(screen, (0, 0, 255), (Hueristic[i][0], Hueristic[i][1]), (Hueristic[i + 1][0], Hueristic[i + 1][1]), width=4)
        if len(Hueristic) >=1:pygame.draw.line(screen, (0, 0, 255), (Hueristic[0][0], Hueristic[0][1]), (Hueristic[-1][0], Hueristic[-1][1]), width=4)
        for spot in places:
            pygame.draw.circle(screen, (0,0,0),(spot[0],spot[1]), 10)
        text_surface = font.render('Red is full TSP Blue is Heuristic', True, (0, 0, 0))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    # Quit Pygame

DrawExample(places)
#DrawExample(generate_RandomCoordinates(5))# DO NOT run more than 9 or 10
pygame.quit()