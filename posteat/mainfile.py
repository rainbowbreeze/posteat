from datetime import date

from posteat import PostEat

# http://www.artima.com/weblogs/viewpost.jsp?thread=4829
def main():
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
