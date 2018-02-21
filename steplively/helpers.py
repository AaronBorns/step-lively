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

import matplotlib.pyplot
import numpy.core.function_base
import sys
import os
import textwrap
from os import path

splash = textwrap.dedent(
    """

    Welcome to
      ______     __                                __        __                       __           
     /      \   /  |                              /  |      /  |                     /  |          
    /$$$$$$  | _$$ |_     ______    ______        $$ |      $$/  __     __   ______  $$ | __    __ 
    $$ \__$$/ / $$   |   /      \  /      \       $$ |      /  |/  \   /  | /      \ $$ |/  |  /  |
    $$      \ $$$$$$/   /$$$$$$  |/$$$$$$  |      $$ |      $$ |$$  \ /$$/ /$$$$$$  |$$ |$$ |  $$ |
     $$$$$$  |  $$ | __ $$    $$ |$$ |  $$ |      $$ |      $$ | $$  /$$/  $$    $$ |$$ |$$ |  $$ |
    /  \__$$ |  $$ |/  |$$$$$$$$/ $$ |__$$ |      $$ |_____ $$ |  $$ $$/   $$$$$$$$/ $$ |$$ \__$$ |
    $$    $$/   $$  $$/ $$       |$$    $$/       $$       |$$ |   $$$/    $$       |$$ |$$    $$ |
     $$$$$$/     $$$$/   $$$$$$$/ $$$$$$$/        $$$$$$$$/ $$/     $/      $$$$$$$/ $$/  $$$$$$$ |
                                  $$ |                                                   /  \__$$ |
                                  $$ |                                                   $$    $$/ 
                                  $$/                                                     $$$$$$/  
    
    """
)

instructions = textwrap.dedent(
    """
    Step Lively Copyright (C) 2018 Cleveland State University
    This program comes with ABSOLUTELY NO WARRANTY; for details type 'w'.
    This is free software, and you are welcome to redistribute it under certain conditions; type 'c' for details.

    If you accept these terms, press the space bar; press any other key to exit."""
)
license_excerpt = textwrap.dedent(
    """
    An excerpt from the GPLv3 license found in COPYING.txt...

        15. Disclaimer of Warranty.

    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
    APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
    HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
    OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
    IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
    ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

    """
)

goodbye = textwrap.dedent(
    """
    Thank you for using Step Lively!

    From the Step Lively team:
    * Dr. Dan Simon - http://academic.csuohio.edu/simond/
    * Mohamed Abdelhady
    * Mike Stojsavljevic
    * Xavier Williams
    * Joe Ayoub
    * Aaron Borns - https://www.linkedin.com/in/aaron-borns/

    """
)

with open(path.join(path.abspath(path.dirname(__file__)), '..', 'COPYING'), encoding='utf-8') as license_file:
    license = license_file.read()

def prompt_for_user_choice():
    print(splash)
    try:
        user_key_pressed = wait_for_key_press(instructions)
    except Exception:
        user_key_pressed = '~'
    print('\n')
    return user_key_pressed

def warranty():
    print(license_excerpt)

def conditions():
    print(license)

def quit():
    print(goodbye)
    exit(0)

def plot_sine_wave():
    x = numpy.linspace(0, 20, 100)
    matplotlib.pyplot.plot(x, numpy.sin(x))
    matplotlib.pyplot.show()

# prints the message without a new line, and waits for any cross-platform key press
def wait_for_key_press(message):
    print(message, end='', flush=True)
    result = None
    if os.name == 'nt':
        import msvcrt
        try:
            key_pressed = msvcrt.getch().decode('utf-8')
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