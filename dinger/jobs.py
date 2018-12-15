""" Here list some useful or interesting functions for dingding bot. """

from message import Message


def say_hello_world():
    context = 'Hello, world!'
    message = Message('text', content=context)
    return message.get()


def weather_forecast():
    """
    use: https://restapi.amap.com/v3/weather/weatherInfo?city=<adcode>&key=<your_key>
    like: https://restapi.amap.com/v3/weather/weatherInfo?city=110108&key=xxxxxxx
    """


def obtain_latest_weibo_of(wb_id):
    """ 获取微博用户xxx的最新微博.
    """
    pass


def obtain_random_wallpaper():
    """ 从Bing获取壁纸.
    """
    pass


def obtain_poetry():
    """ 获取今日的诗词.

    API: http://gxy.me/shici
    """
    pass


def obtain_news():
    """ 获取新闻.
    """
    pass


def obtain_zhihu_hot():
    """ 获取知乎热榜.
    """
    pass


def obtain_github_trending():
    """ 获取GitHub最热项目.

    API: https://github.com/trending
    """
    pass


def obtain_hn_latest():
    """ 获取Hacker News 最新的 Post.

    API: https://news.ycombinator.com/
    """
    pass


def obtain_todo_list():
    """ 获取今日计划.
    """
    pass


def obtain_github_notice():
    """ 获取GtiHub未读消息
    """
    pass


def time_for_book_food():
    """ 提醒点餐
    """
    pass


def choose_where_for_lunch(cafes):
    """ 随机选择去哪个餐厅吃午饭
    """
    pass
