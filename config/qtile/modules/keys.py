from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
import os

mod = "mod4"
terminal = "kitty"

keys = [
    # --- User Config --- #
    Key([mod], "b", lazy.spawn("brave"), desc="open Web Browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="open File Manager"),
    Key([mod], "p", lazy.spawn("pamac-manager"), desc="open Package Manager"),
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "space", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    KeyChord(
        [mod, "control"],
        "w",
        [
            Key(
                [],
                "Left",
                lazy.layout.grow_left(),
                desc="Grow window to the left",
            ),
            Key(
                [],
                "Right",
                lazy.layout.grow_right(),
                desc="Grow window to the right",
            ),
            Key(
                [],
                "Down",
                lazy.layout.grow_down(),
                desc="Grow window down",
            ),
            Key([], "Up", lazy.layout.grow_up(), desc="Grow window up"),
            Key([], "m", lazy.layout.maximize(), desc="Maximize focused window"),
            Key([], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        ],
        mode=True,
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # terminal
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "grave", lazy.group["dropdown"].dropdown_toggle("terminal")),
    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "Left", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "Right", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload Qtile Config"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod, "shift"],
        "q",
        lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu.sh")),
        desc="Power Menu",
    ),
    Key(
        [
            mod,
        ],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    # audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 1")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 1")),
    # screenshot
    Key([], "Print", lazy.spawn("xfce4-screenshooter -fm --no-border")),
    Key([mod], "Print", lazy.spawn("xfce4-screenshooter -wm")),
    Key(["shift"], "Print", lazy.spawn("xfce4-screenshooter -rm --no-border")),
]
