#    steplively is an application for sensor measurement 
#    Copyright (C) 2018 Cleveland State University
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys, os

# prints the message without a new line, and waits for any cross-platform key press
def wait_for_key_press(message):
    print(message, end='', flush=True)
    result = None
    if os.name == 'nt':
        import msvcrt
        try:
            key_pressed = msvcrt.getch().decode('UTF-8')
        except Exception:
            key_pressed = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            key_pressed = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return key_pressed

# returns text of a specified file for any uncommented (#) lines
def get_uncommented_text(file):
    msg = ''
    for line in open(file, 'r'):
        if line.startswith('#'):
            continue
        msg += line
    return msg
