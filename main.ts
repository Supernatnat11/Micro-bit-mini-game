function Win () {
    music.playTone(523, music.beat(BeatFraction.Quarter))
    music.playTone(494, music.beat(BeatFraction.Quarter))
    music.playTone(392, music.beat(BeatFraction.Quarter))
    music.playTone(494, music.beat(BeatFraction.Quarter))
    music.playTone(523, music.beat(BeatFraction.Quarter))
}
input.onButtonPressed(Button.A, function () {
    Player.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    game.gameOver()
    basic.showNumber(game.score())
})
input.onButtonPressed(Button.B, function () {
    Player.change(LedSpriteProperty.X, 1)
})
function Lose () {
    music.playTone(440, music.beat(BeatFraction.Quarter))
    music.playTone(349, music.beat(BeatFraction.Quarter))
    music.playTone(294, music.beat(BeatFraction.Quarter))
    music.playTone(262, music.beat(BeatFraction.Quarter))
}
let Apple: game.LedSprite = null
let Player: game.LedSprite = null
Player = game.createSprite(2, 4)
music.setVolume(255)
basic.forever(function () {
    if (game.isRunning()) {
        basic.pause(randint(1800, 2000))
        Apple = game.createSprite(randint(0, 4), 0)
        for (let index = 0; index < 5; index++) {
            basic.pause(randint(400, 500))
            Apple.change(LedSpriteProperty.Y, 1)
        }
        if (Apple.isTouching(Player)) {
            Apple.delete()
            game.addScore(1)
            Win()
        } else {
            Apple.delete()
            game.addScore(-1)
            Lose()
        }
    }
})
