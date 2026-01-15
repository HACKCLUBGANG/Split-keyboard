import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP5, board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.modules.append(
    Split(
        split_side=SplitSide.LEFT,
        data_pin=board.GP10,
        use_pio=True,
    )
)

keyboard.keymap = [
    [
        KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,
        KC.A,  KC.S,  KC.D,  KC.F,  KC.G,
        KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,
        KC.NO, KC.NO, KC.NO, KC.SPC, KC.ENT,
        KC.LCTL, KC.LALT,
    ]
]

keyboard.go()
