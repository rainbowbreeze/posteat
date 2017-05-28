from tinydb import TinyDB, Query
from datetime import date, datetime
import facebook


class PostEat:
    """
    The main class, entry point for everything
    """

    def __init__(self, debug=False, persist_data=False):
        self.__debug = debug
        self.__persist_data = persist_data
        self.db = TinyDB('db.json')
        self.access_token = 'EAACEdEose0cBALTqc1mZBuFRVHS7pzXgU5bv7siBEOvj8gaPYLpLyVvN47Lfhvg8QRCONN9FQsnwg5n8YZCZAnEYkluZBmMiRdGN079T79fLEEoijbWSQ6VNcPQNRtWdlJKGZAJ6VilksaVcWKMZAVKCCNDAkg8worIkYuYKFEZAcIecDmCZBAsG8R983pEHUGwZD'

    def get_menu(self, year, month, day):
        """Gets the menu for the given day.
        If it's not cached on the storage, it tries to retrieve online"""
        if self.__debug:
            print('Searching for the menu ot the day', year, month, day)
        menu = self.__get_menu_from_storage(year, month, day)
        if menu is not None:
            return menu

        # Retrieves the menu online
        menu = self.__get_menu_from_facebook(year, month, day)

        if menu is not None:
            # Saves menu for the next time
            if self.__persist_data:
                if self.__debug:
                    print('Saving data on persistent storage')
                self.save_menu_info_storage(year, month, day, menu)
            else:
                if self.__debug:
                    print('Skipping save data on persistent storage')

        return menu

    def save_menu_info_storage(self, year, month, day, menu_food):
        """Save current menu into storage"""
        str_date = self.__get_menu_date_str(year, month, day)
        row_id = self.db.insert(
            {
                'menu_date': str_date,
                'menu_food': menu_food
            }
        )
        print('Row: ', row_id)
        return row_id

    def __get_menu_from_storage(self, year, month, day):
        """Get the menu for a particular day from the storage"""
        str_date = self.__get_menu_date_str(year, month, day)
        menu = Query()
        result = self.db.search(menu.menu_date == str_date)
        if self.__debug:
            print('Result from storage: ', result)
        if result is None or len(result) == 0:
            return None
        else:
            return result[0]['menu_food']

    def __get_menu_date_str(self, year, month, day):
        """Transform a date into a string with a unified format for storage purpose"""
        # See: https://docs.python.org/3.5/library/datetime.html#strftime-strptime-behavior
        # return date(year, month, day).strftime('%Y/%m/%d')
        return date(year, month, day).isoformat()

    def __get_menu_from_facebook(self, year, month, day):
        """Reads post on facebook from the page and retrieve the menu"""
        graph = facebook.GraphAPI(
            access_token='EAACEdEose0cBAHcnx6Wub8W3JjkidZC18EJ9zWDe6FZBV3yspAAFEKj8txsD1gLWi8wjcEhlLPAZCMQPXCUz5HgXgILrdBzbMbo3zaPGBYPShux9Cn6ZBWvdkIyZAA1DoLvUH5DRuXuWzKeT5fNabU7feNBQ6NQHYLYRybjgO5Det2lpYAMmY31i3avMixTgZD',
            version='2.7'
        )

        posteat_posts = graph.get_object(
            id='147172505469032',
            # fields='posts'
            fields='posts.limit(10)'
        )
        if self.__debug:
            print('Read from facebook')
        # return posteat_posts['posts']['data'][0]['message']

        message = None
        for post in posteat_posts['posts']['data']:
            if self.__debug:
                print('--------------- Post ---------------')
                print(post)

            # Converts the string in a valid datetime object, following Facebook date format
            created_time_srt = post['created_time']
            created_time = datetime.strptime(created_time_srt, "%Y-%m-%dT%H:%M:%S%z")
            # Checks if the post was written in the same day
            if self.__check_if_post_has_valid_date(created_time, year, month, day):
                # The post date is correct, now let's check for the content
                if self.__debug:
                    print("Foud a post for the given date")
                message = post['message']
                if self.__check_if_post_is_valid_menu(message):
                    if self.__debug:
                        print('Found the menu for the given day')
                        print(message)
                    break

        return message

    def __check_if_post_has_valid_date(self, post_datetime, year, month, day):
        """Checks if the post was written in the given day of the year"""
        if self.__debug:
            print('Comparing ', post_datetime, ' with ', year, month, day)
        return post_datetime.year == year and post_datetime.month == month and post_datetime.day == day

    def __check_if_post_is_valid_menu(self, text):
        """Checks if the post is a valid menu post"""
        # Get first post line and clean-up it a little bit
        title = text.splitlines()[0].casefold().strip()
        if self.__debug:
            print('Post title: ###', title, '###')
        return title in ('il menu di oggi', 'il menù di oggi')



