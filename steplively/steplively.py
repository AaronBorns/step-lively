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

def warranty():
    print(parse.get_uncommented_text('./assets/warranty.txt'))

def conditions():
    print(parse.get_uncommented_text('../COPYING'))

def goodbye():
    print(parse.get_uncommented_text('./assets/goodbye.txt'))
    exit(0)

def run():
    plot.plot_sine_wave()

if __name__ == "__main__": 
    import plot
    import parse

    print(parse.get_uncommented_text('./assets/splash.txt'))
    user_key_pressed = parse.wait_for_key_press(parse.get_uncommented_text('./assets/instructions.txt'))
    print('\n')

    user_choices = {'w': warranty, 'c': conditions, ' ': run}

    try:
        user_choices[user_key_pressed]()
    finally:
        goodbye()
PY