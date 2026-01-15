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
        split_side=SplitSide.RIGHT,
        data_pin=board.GP10,
        use_pio=True,
    )
)

keyboard.keymap = [
    [
        KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,
        KC.H,  KC.J,  KC.K,  KC.L,  KC.SCLN,
        KC.N,  KC.M,  KC.COMM, KC.DOT, KC.SLSH,
        KC.NO, KC.NO, KC.NO, KC.BSPC, KC.RSFT,
        KC.RALT, KC.RCTL,
    ]
]

keyboard.go()
