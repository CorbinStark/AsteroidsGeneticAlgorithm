import itertools

#Game
WINDOW_WIDTH = 1280                                                             #Width of game window.
WINDOW_HEIGHT = 920                                                             #Height of game window.
BLACK = (0, 0, 0)                                                               #Color value used for display.
WHITE = (255, 255, 255)                                                         #Color value used for display.
MAXSPEED = 10                                                                   #Maximum ship speed.
THRUST = 2.5                                                                    #Thrust vector increase per input.
DECAY = 0.05                                                                    #Thrust vector decay per frame.
VECTORCOUNT = 30                                                                #Number of thrust vectors
BREAKPOINTS = [0, 100, 50, 20]                                                  #Points awarded for breaking each size.
DEATHPOINTS = -1000                                                             #Points deducted for getting hit.
RESPAWNTIME = 6000                                                              #Invulnerability time in milliseconds.
ASTEROIDSCALE = 30                                                              #Scalar for asteroid size.
PLAYERSIZE = 20                                                                 #Scalar for player size.
FPS = 60                                                                        #Frames per second during user play.
SENSORCOUNT = 8                                                                 #Ship sensors, limited by Q.sensors[].
SENSORRANGE = WINDOW_HEIGHT/2                                                   #Distance asteroids can be detected.
SAVEQMATRIX = False                                                             #Toggle for output of Q-Matrix.
DRAW_SENSORS = True                                                             #Toggle for displaying sensors.
DISPLAY_GAME = True                                                             #Toggle for displaying game.

sensors = ['F', 'FR', 'R', 'BR', 'B' , 'BL' , 'L' , 'FL']                       #List of sensor directions, relative to player.
results = ['None', 'Some']                                                      #List of sensor results.
actions = ['Left', 'Right', 'Thrust', 'Shoot']                                  #List of possible ship actions.
state = []                                                                      #Array for storing state enumeration.

#Genetic algorithm tunable parameters
PopulationSize = 10								                                #Number of chromosomes.
NumIterations = 10  							                                #Number of generations.
SimulationLength = 1000                                                         #Number of frames to simulate
MutationPct = 0.45								                                #Liklihood of mutation.
Replacement = True								                                #Multiple recombination.
Elitism = True									                                #Better parents persist.
statespace = len(results)**len(sensors)                                         #Size of statespace = |R|^|S|

#Q-learning
stepsize = 0.2                                                                  #Eta: Learning rate.
discount = 0.9                                                                  #Gamma: exploration vs exploitation.
takerisk = 0.1                                                                  #Epsilon: chance of suboptimal choice.
Qlimiter = 100000                                                               #Number of frames to simulate.
FRAMES_PER_ACTION = 6                                                           #Number of frames to wait between actions.

def initialize():                                                               #Initialize statespace enumeration.
    for s in itertools.product(results, repeat = len(sensors)): state.append(s) #Generates permutations with replacement.
