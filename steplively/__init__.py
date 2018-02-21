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
if __name__ == "__main__": 
    import helpers as h

    print(h.get_uncommented_text('./assets/splash.txt'))
    user_key_pressed = h.wait_for_key_press(h.get_uncommented_text('./assets/instructions.txt'))
    print('\n')

    user_choices = {'w': h.warranty, 'c': h.conditions, ' ': h.run}

    try:
        user_choices[user_key_pressed]()
    finally:
        h.goodbye()