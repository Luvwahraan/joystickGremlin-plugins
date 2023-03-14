import gremlin
from gremlin.user_plugin import *


# Plugin variables
mode = ModeVariable("Mode", "Mode in which to use these settings")
phys_axis = PhysicalInputVariable(
        "Physical axis",
        "Physical axis to double",
        [gremlin.common.InputType.JoystickAxis]
)

virt_axis = VirtualInputVariable(
        "vJoy output",
        "Virtual output axis",
        [gremlin.common.InputType.JoystickAxis]
)

btn = PhysicalInputVariable(
        "Button changer",
        "Button changing direction.",
        [gremlin.common.InputType.JoystickButton]
)


decorate_1 = phys_axis.create_decorator(mode.value)


def update_vjoy(value, vjoy, joy):
    # All physical axis mapped to half of virtual axis
    value = (value - 1) / 2
    
    if joy[btn.device_guid].button(btn.input_id).is_pressed:
        value = -value

    vjoy[virt_axis.vjoy_id].axis(virt_axis.input_id).value = value


@decorate_1.axis(phys_axis.input_id)
def axis_cb(event, vjoy, joy):
    update_vjoy(event.value, vjoy, joy)
