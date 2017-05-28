from datetime import date

from posteat import PostEat

# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
def main():
    posteat = PostEat(debug=True, persist_data=True)
    today = date.today()
    # posteat.save_menu_info_storage(today.year, today.month, today.day, 'A long meal here for today')
    menu = posteat.get_menu(today.year, today.month, today.day -1)
    print('This is the menu\n', menu)
    return

if __name__ == "__main__":
    main()
