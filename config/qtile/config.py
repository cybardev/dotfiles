from libqtile.lazy import lazy
from libqtile.config import Key, Group, DropDown, ScratchPad, Match, Click, Drag, Screen
from libqtile import layout, hook, bar
from locale import setlocale, LC_ALL
import subprocess
import os
from libqtile import widget
from libqtile import qtile

setlocale(LC_ALL, "")

mod = "mod4"
terminal = "kitty"

####################################################
####################################################
#                                                  #
#                   Keys                           #
#                                                  #
####################################################
####################################################

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="spawn rofi"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "l", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # Utility
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "grave", lazy.group["dropdown"].dropdown_toggle("terminal")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 1")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 1")),
]


####################################################
####################################################
#                                                  #
#                   Groups                         #
#                                                  #
####################################################
####################################################

groups = [
    ScratchPad(
        "dropdown",
        [DropDown("terminal", terminal, width=0.8, height=0.8)],
    ),
    Group(name="main", matches=[Match(role="terminal")], label="m"),
    Group(name="web", matches=[Match(role="browser")], label="e"),
    Group(name="code", matches=[Match(wm_class="code-oss")], label="n"),
    Group(name="misc", matches=[Match(wm_class="Thunar")], label="u"),
]

keys.extend(
    [
        Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
        Key([mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"),
    ]
)

for index, i in enumerate(groups):
    keys.extend(
        [
            Key([mod], "Next", lazy.screen.next_group(),
                desc="Switch to next group"),
            Key(
                [mod],
                "Prior",
                lazy.screen.prev_group(),
                desc="Switch to previous group",
            ),
            # mod1 + number of group = switch to group
            Key(
                [mod],
                str(index),
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod1 + shift + number of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(index),
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + number of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


####################################################
####################################################
#                                                  #
#                   Layouts                        #
#                                                  #
####################################################
####################################################

layouts = [
    layout.Spiral(border_focus="#398a6b", border_normal="#121f1b", margin=4, border_width=4),
    layout.Max(border_focus="#398a6b", border_normal="#121f1b"),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadTall(margin=4, border_focus="#398a6b", border_normal="#121f1b"),
    # layout.Bsp(border_focus="#398a6b", border_normal="#121f1b", margin=4),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=4,
    border_focus="#398a6b",
    border_normal="#121f1b",
)

####################################################
####################################################
#                                                  #
#                   Mouse                          #
#                                                  #
####################################################
####################################################

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

####################################################
####################################################
#                                                  #
#                   Hooks                          #
#                                                  #
####################################################
####################################################


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


@hook.subscribe.startup
def start_always():
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


####################################################
####################################################
#                                                  #
#                   Screens                        #
#                                                  #
####################################################
####################################################

colors = [
    ["#282c34", "#282c34"],  # panel background
    ["#3d3f4b", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    [
        "#74438f",
        "#74438f",
    ],  # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
    ["#e1acff", "#e1acff"],  # window name
    ["#ecbbfb", "#ecbbfb"],  # backbround for inactive screens
]

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=5, linewidth=0, background="#2f343f"),
                widget.Image(
                    # filename="~/.config/qtile/eos-c.png",
                    filename="~/Pictures/cy-icon.png",
                    margin=3,
                    background="#2f343f",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show drun")
                    },
                ),
                widget.Sep(padding=5, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method="line",
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f",
                    font="Cantarell",
                    fontsize=20,
                    padding=4,
                    margin_y=4,
                ),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                    font="Cantarell",
                ),
                widget.Sep(padding=4, linewidth=0),
                widget.WindowName(
                    foreground="#99c0de",
                    fmt="{}",
                    font="Cantarell",
                    fontsize=18,
                    padding=3,
                ),
                widget.CurrentLayoutIcon(scale=0.80),
                widget.Sep(padding=4, linewidth=0),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                    font="Cantarell",
                ),
                # widget.CheckUpdates(
                #     update_interval=1800,
                #     distro="Arch_yay",
                #     display_format="{updates} Updates",
                #     foreground="#ffffff",
                #     mouse_callbacks={
                #         "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syu")
                #     },
                #     background="#2f343f",
                #     font="Cantarell",
                #     fontsize=20,
                #     padding=8,
                # ),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                    font="Cantarell",
                ),
                widget.Systray(icon_size=24),
                widget.Sep(padding=5, linewidth=0),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                    font="Cantarell",
                ),
                widget.Volume(
                    fontsize=20,
                    padding=3,
                    foreground=colors[4],
                    background="#2f343f",
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
                    font="Cantarell",
                ),
                widget.Volume(
                    fontsize=20,
                    padding=3,
                    foreground=colors[4],
                    background="#2f343f",
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
                    font="Cantarell",
                    emoji=True,
                ),
                widget.Sep(
                    padding=0, linewidth=5, foreground="#2f343f", size_percent=100
                ),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                    font="Cantarell",
                ),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                    font="Cantarell",
                ),
                widget.Clock(
                    format="󰥔  %Y-%m-%d %a %I:%M %p",
                    background="#2f343f",
                    foreground="#9bd689",
                    padding=8,
                    font="Cantarell",
                    fontsize=20,
                ),
                widget.TextBox(
                    text="",
                    # text=" ",
                    padding=0,
                    fontsize=32,
                    foreground="#2f343f",
                ),
                widget.TextBox(
                    text="⏻",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser("~/.config/rofi/powermenu.sh")
                        )
                    },
                    foreground="#e39378",
                    font="Cantarell",
                    fontsize=24,
                    padding=8,
                ),
                widget.Sep(padding=6, linewidth=0),
            ],
            36,  # height in px
            background="#404552",  # background color
        ),
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
