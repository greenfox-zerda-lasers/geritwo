'''
*** TkWanderer Game ***
by Gergo Vamosi, alias GergoV

Green Fox Academy, 2016.
'''

import model
import view

class Game:
    '''
    Game controller object with main game functions.
    '''

    def __init__(self):
        self.model = model.GameData()
        self.view = view.GameDisplay()
        self.hero = model.Hero() # Game instantiates?

        self.game_flow_controller()

    def game_flow_controller(self):
        # Init level
        self.init_level()
        #   Character generation < Model char data
        # Launch level
            # Starting position display
        # Main loop:
            # Get I/O
            # Move characters
            # Check positions
            # Check if battle > Call battle
            # Display
        self.game_display_controller()

    def init_level(self):
        self.view.create_canvas(self.model.get_area_floorplan())
        # generate characters < model char data, model level data

    def game_display_controller(self):
        self.view.display_area(self.model.get_area_floorplan())
        self.view.display_hero(self.hero.get_hero_position())
        # display enemies
        self.view.put_all_in_mainloop()

    '''
    def set_hero_position(self):
        self.hero.get_hero_position(self)
    '''

# LAUNCH GAME
game = Game()
