from libqtile.config import ScratchPad, DropDown, Key, Group, Match
from libqtile.command import lazy
from .keys import keys, mod

groups = [
    ScratchPad(
        "dropdown",
        [DropDown("terminal", "kitty", width=0.8, height=0.8)],
    ),
    Group(name="main", matches=[Match(role="terminal")], label="m"),
    Group(name="web", matches=[Match(role="browser")], label="e"),
    Group(name="code", matches=[Match(wm_class="code-oss")], label="n"),
    Group(name="misc", matches=[Match(wm_class="Thunar")], label="u"),
]

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
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                # i.name,
                str(index),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
