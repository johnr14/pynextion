
import pytest
from .config import PORT_DEFAULT
import time
from pynextion import PySerialNex
from pynextion.widgets import NexPage, NexSlider
from pynextion.color import NamedColor


@pytest.mark.parametrize("port", [PORT_DEFAULT])
def test_slider(port):
    nexSerial = PySerialNex(port)
    nexSerial.init()

    nexPage = NexPage(nexSerial, "pg_slider", pid=11)

    nexSlider = NexSlider(nexSerial, "h0", cid=4)

    nexPage.show()

    time.sleep(0.1)

    nexSlider.value = 43691  # 0-65535

    time.sleep(1)

    # nexSlider.cursor.color = NamedColor.GRAY
    nexSlider.forecolor = NamedColor.GRAY

    time.sleep(1)

    w = 10
    nexSlider.cursor.width = w
    assert nexSlider.cursor.width == w

    time.sleep(1)

    h = 13
    nexSlider.cursor.height = h
    assert nexSlider.cursor.height == h

    time.sleep(1)

    nexSerial.close()
