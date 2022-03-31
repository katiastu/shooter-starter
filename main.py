def on_b_pressed():
    global projectile
    if gameMode == True:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . 3 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 5 5 2 2 3 . . . . . . 
                            . . . . . 5 5 2 2 3 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            -50,
            50)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def level1():
    global current_level
    current_level = 1
    scene.set_background_color(15)
    MyPlayer()

def on_a_pressed():
    global gameMode
    if gameMode == True:
        gameMode = True
        MyPlayer()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def MyPlayer():
    global mySprite
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 4 4 4 4 4 4 4 . . . . . 
                    . . . 5 4 4 9 4 4 9 4 4 . . . . 
                    . . . . 4 4 4 4 4 4 4 4 . . . . 
                    . . . . 4 4 4 4 4 4 4 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    controller.move_sprite(mySprite, 100, 100)
current_level = 0
mySprite: Sprite = None
projectile: Sprite = None
gameMode = False
scene.set_background_image(assets.image("""
    woods
"""))
gameMode = True