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

    user_choices = {'w': h.warranty, 'c': h.conditions, ' ': lambda:None}
    user_choice = ''
    while (user_choice != ' '):
        user_choice = h.prompt_for_user_choice()
        user_choices.get(user_choice, h.goodbye)()

    h.plot_sine_wave()
    h.goodbye()