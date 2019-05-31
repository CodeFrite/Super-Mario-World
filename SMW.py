import pygame

class Character(object):    
    
    DIRECTION_LEFT  = 0;
    DIRECTION_RIGHT = 1;
    
    STATE_ACTION_STAND     = 0;
    STATE_ACTION_WALK      = 1;
    STATE_ACTION_SPRINT    = 2;
    STATE_ACTION_JUMP      = 3;
    STATE_ACTION_DOCK      = 4;
    STATE_ACTION_LOOK_UP   = 5;
    STATE_ACTION_FLY       = 6;
    STATE_ACTION_SWIM      = 7;
    STATE_ACTION_FIRE_BALL = 8;
    
    STATE_SIZE_SMALL  = 0;
    STATE_SIZE_BIG    = 1;
    STATE_SIZE_FLOWER = 2;
    STATE_SIZE_STAR   = 3;
    STATE_SIZE_BEAR   = 4;
    
     
    def __init__(self):
        # the first item represents the head
        self.x = 0;
        self.y = 0;
        self.state = 0;
        self.state_action = self.STATE_ACTION_STAND;
        self.direction = self.DIRECTION_RIGHT;
        self.loadImages();
    
    def loadImages(self):
        self.image_characters = pygame.image.load('images/mario.png');
        
    def sendKeys(self, keys):
        if (keys == keys[pygame.K_LEFT]):
            self.direction = self.DIRECTION_LEFT;
    
    def update(self):
        pass;
    
    def render(self, window):
        if self.state == 0:
            window.blit(self.image_characters, (0, 0), (1, 10, 16, 24));
            self.state = 1;
        else:
            window.blit(self.image_characters, (0, 0), (18, 10, 16, 24));
            self.state = 0;

class Game(object):
    
    SCREEN_WIDTH  = 256;
    SCREEN_HEIGHT = 224;
        
    GAME_FRAME_RATE_MS = 100;
        
    GAME_STATE_MENU  = 0;
    GAME_STATE_PLAY  = 1;
    GAME_STATE_PAUSE = 2;
    GAME_STATE_EXIT  = 3;
    
    def __init__(self):        
        # Init game state
        self.game_state = self.GAME_STATE_PLAY;
        
        # Create game components
        self.mario = Character();
        
        # Init game graphics
        pygame.init();
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT));
        pygame.display.set_caption("*** Super Mario World ***");
    
        # Init sounds
        #self.sound_eat = pygame.mixer.Sound('sounds/eat.wav');
        
    def start(self):
        ''' MAIN GAME LOOP '''          
        while self.game_state != self.GAME_STATE_EXIT:
            # Delay between 2 images
            pygame.time.delay(self.GAME_FRAME_RATE_MS);
            # Dispatch events
            self.dispatchInputs();
            # Update mario
            self.mario.update();
            # Render objects            
            self.render();
            
        # Quit the game
        pygame.quit();
    
    def dispatchInputs(self):
        for event in pygame.event.get():    
            # Check keyboard keypress
            keys = pygame.key.get_pressed();
            
            # User closes the window
            if (event.type == pygame.QUIT) or keys[pygame.K_ESCAPE]:
                self.game_state = self.GAME_STATE_EXIT;
            
            # Send keys to snake
            self.mario.sendKeys(keys);
    
    def render(self):
        # Clear the window
        self.window.fill((255,255,255));
        # Render mario
        self.mario.render(self.window);
        # Refresh the window
        pygame.display.update();
    
    def renderText(self, text, x, y):
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Comic Sans MS", 30);
        # apply it to text on a label
        label = myfont.render(str(text), 1, (255, 255, 0));
        # put the label object on the screen at point x=100, y=100
        self.window.blit(label, (x, y));
        
    def playMusic(self, file):
        pygame.mixer.music.load(file);
        pygame.mixer.music.play();
        
if __name__ == '__main__':
    game = Game();
    game.start();