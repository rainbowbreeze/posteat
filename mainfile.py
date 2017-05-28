from datetime import date

import sys

"""
# Added to prevent ImportError: No module named 'posteat'
#  when this file is in not in the same module structure that
#  the main class to launch
# https://stackoverflow.com/a/9806045/584134
# Please also note the difference between append and insert
import os
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.insert(0, parent_dir)
"""
# ---
from posteat.posteat import PostEat


# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
def main(argv=sys.argv):
    posteat = PostEat(debug=True, persist_data=False)
    today = date.today()
    # posteat.save_menu_info_storage(today.year, today.month, today.day, 'A long meal here for today')
    year = today.year
    month = today.month
    day = today.day - 4
    menu = posteat.get_menu(year, month, day)
    print('This is the menu for {}-{}-{}\n{}'.format(year, month, day, menu))
    return

if __name__ == "__main__":
    main()
