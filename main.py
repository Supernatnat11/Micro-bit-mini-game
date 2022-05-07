def Win():
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    music.play_tone(494, music.beat(BeatFraction.QUARTER))
    music.play_tone(392, music.beat(BeatFraction.QUARTER))
    music.play_tone(494, music.beat(BeatFraction.QUARTER))
    music.play_tone(523, music.beat(BeatFraction.QUARTER))

def Lose():
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))

def on_button_pressed_a():
    Player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    game.game_over()
    basic.show_number(game.score())
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    Player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Apple: game.LedSprite = None
Player: game.LedSprite = None
Player = game.create_sprite(2, 4)
music.set_volume(255)

def on_forever():
    global Apple
    if game.is_running():
        basic.pause(randint(1800, 2000))
        Apple = game.create_sprite(randint(0, 4), 0)
        for index in range(5):
            basic.pause(randint(400, 500))
            Apple.change(LedSpriteProperty.Y, 1)
        if Apple.is_touching(Player):
            Apple.delete()
            game.add_score(1)
            Win()
        else:
            Apple.delete()
            game.add_score(-1)
            Lose()
basic.forever(on_forever)
