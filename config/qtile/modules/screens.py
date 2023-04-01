from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from .keys import terminal
import os

accent_color = colors[8][0]
accent_bg = colors[9][0]


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Notify(),
                widget.Sep(padding=4, linewidth=0),
                # widget.Image(
                #     # filename="~/.config/qtile/eos-c.png",
                #     filename="~/Pictures/Apple_logo_white.svg.png",
                #     margin=4,
                #     background="#2f343f",
                #     mouse_callbacks={
                #         "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
                #     },
                # ),
                widget.TextBox(
                    text="(λ)",
                    fontsize=24,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
                    },
                    foreground="#ff86ff",
                ),
                widget.Sep(padding=8, linewidth=0),
                widget.GroupBox(
                    highlight_method="line",
                    this_screen_border=accent_color,
                    this_current_screen_border=accent_color,
                    active=colors[2][0],
                    inactive="#848e96",
                    # background="#2f343f",
                    fontsize=18,
                ),
                widget.Sep(padding=8, linewidth=0),
                # widget.TextBox(
                #     # text = '',
                #     padding=0,
                #     fontsize=28,
                #     foreground="#2f343f",
                # ),
                widget.Prompt(fontsize=18),
                widget.Spacer(length=8),
                widget.WindowName(
                    foreground="#b7ebba", fmt="{}", max_chars=32, fontsize=18
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.64),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syyu")
                    },
                    # background="#2f343f",
                ),
                widget.Systray(icon_size=24),
                widget.Sep(padding=8, linewidth=0),
                # widget.TextBox(
                #     # text = '',
                #     padding=0,
                #     fontsize=28,
                #     foreground="#2f343f",
                # ),
                volume,
                widget.Sep(padding=8, linewidth=0),
                widget.Battery(
                    battery=1,
                    fontsize=20,
                    charge_char="🔌",
                    discharge_char="🔋",
                    empty_char="🪫",
                    full_char="⚡",
                    format="{char}{percent:2.0%}",
                    notify_below=15,
                    notification_timeout=15,
                ),
                widget.Sep(padding=8, linewidth=0),
                # widget.TextBox(
                #     # text = '',
                #     padding=0,
                #     fontsize=28,
                #     foreground="#2f343f",
                # ),
                # widget.TextBox(
                #     # text = '',
                #     padding=0,
                #     fontsize=28,
                #     foreground="#2f343f",
                # ),
                widget.Clock(
                    format=" %a %d %b %I:%M %p",
                    # background="#2f343f",
                    foreground="#9bd689",
                    fontsize=18,
                ),
                widget.Sep(padding=8, linewidth=0),
                # widget.TextBox(
                #     # text = '',
                #     padding=0,
                #     fontsize=28,
                #     foreground="#2f343f",
                # ),
                widget.TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser("~/.config/rofi/powermenu.sh")
                        )
                    },
                    foreground="#e39378",
                    fontsize=18,
                ),
                widget.Sep(padding=8, linewidth=0),
                # widget.TextBox(
                #     # text = '',
                #     padding=0,
                #     fontsize=28,
                #     foreground="#2f343f",
                # ),
            ],
            42,  # height in px
            # background="#404552"  # background color
            background=accent_bg,  # background color
        )
    ),
]


# screen_info = [{"width": screen.width, "height": screen.height} for screen in screens]
