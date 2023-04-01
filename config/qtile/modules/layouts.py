from libqtile import layout
from libqtile.config import Match
from .widgets import colors

# from .screens import screen_info

accent_color = colors[8][0]
border_thickness = 4

screen_width = 2256  # screen_info[0]["width"]
screen_height = 1504  # screen_info[0]["height"]

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
    border_width=border_thickness,
    border_focus=accent_color,
)

layouts = [
    # layout.MonadTall(margin=8, border_focus='#5294e2',
    #                  border_normal='#2c5380'),
    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(
        fair=False,
        margin=2,
        border_width=border_thickness,
        border_focus=accent_color,
        ratio=(screen_width / screen_height),
    ),
    # layout.Stack(num_stacks=1),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Max(),
    floating_layout,
]
