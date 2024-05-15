import numpy as np
import pygame
import gymnasium as gym
from gymnasium import spaces

class MoonEnvironment(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array'],'render_fps':4}

    def __init__(self, X, Y, elevation,render_mode=None):
        self.X = X
        self.Y = Y
        self.elevation = elevation
        self.window_size = 512 # Size of PyGame window

        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0,len(self.X)-1,shape=(2,),dtype=np.int),
                "target": spaces.Box(0,len(self.X)-1,shape=(2,),dtype=np.int),
            }
        )

        """We start with 4 actions and then we increase it"""
        self.action_space = spaces.Discrete(4)

        self.action_to_direction = {
            0: np.array([0, 1]),  # Up
            1: np.array([1, 0]),  # Right
            2: np.array([0, -1]),  # Down
            3: np.array([-1, 0]),  # Left
        }

        assert render_mode is None or render_mode in self.metadata['render.modes']
        self.render_mode = render_mode

        #If we use human rendering, we add window and clock to set the correct framerate for rendering.
        self.window = None
        self.clock = None

        #Use observation function to implement in reset and step
    def _get_observation(self):
        return {"agent": self._agent_location, "target": self._target_location}

        #For other info, we use this.
        """TODO: Add more info (for now we have the Manhattan distance)"""
    def _get_info(self):
        return {
            'distance': np.linalg.norm(self._agent_location - self._target_location,ord=1)
        }
    
        #Initiate new episode
    def reset(self, seed =None, options = None):
        super().reset(seed=seed)
        self._agent_location = self.np_random.intergers(0,len(self.X),size=2,dtype=int)

        #Choose random location for target until it's not the same
        self._target_location = self._agent_location
        while np.array_equal(self._agent_location,self._target_location):
            self._target_location = self.np_random.integers(0,len(self.X),size=2,dtype=int)

        observation = self._get_observation()
        info = self._get_info()
        
        if self.render_mode == 'human':
            self._render_frame()
        
        return observation, info
    
def step(self,action):
    direction = self.action_to_direction[action]
    self._agent_location = np.clip(self._agent_location + direction,0,len(self.X)-1)

    done = np.array_equal(self._agent_location,self._target_location)
    reward = 1 if done else 0 
    observation = self._get_observation()
    info = self._get_info()

    if self.render_mode == 'human':
        self._render_frame()
    
    return observation, reward, done, False, info

def render(self):
    if self.render_mode == 'rgb_array':
        return self._render_frame()

def _render_frame(self):
    if self.window is None and self.render_mode == 'human':
        pygame.init()
        pygame.display.init()
        self.window = pygame.display.set_mode((self.window_size, self.window_size))

    if self.clock is None and self.render_mode == 'human':
        self.clock = pygame.time.Clock()
    
    canvas = pygame.Surface((self.window_size, self.window_size))
    canvas.fill((255, 255, 255))
    pixel_size = self.window_size // len(self.X)

    pygame.draw.rect(canvas,(255,0,0),pygame.Rect(pixel_size*self._target_location, (pixel_size, pixel_size)))

    pygame.draw.circle(canvas, (0, 0, 255), (self._agent_location + 0.5)* pixel_size , pixel_size // 3)

    for x in range(len(self.X)):
        pygame.draw.line(canvas, 0,(pixel_size*x,0),(pixel_size*x,self.window_size),width=3)
        pygame.draw.line(canvas, 0,(0,pixel_size*x),(self.window_size,pixel_size*x),width=3)

    if self.render_mode == 'human':
        self.window.blit(canvas, canvas.get_rect())
        pygame.event.pump()
        pygame.display.update()

        self.clock.tick(self.metadata['render_fps'])
    else:
        return np.transpose(np.array(pygame.surfarray.pixels3d(canvas)),axes = (1,0,2))

def close(self):
    if self.window is not None:
        pygame.display.quit()
        pygame.quit()
