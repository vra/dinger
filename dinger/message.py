""" Wrapper API for dingding bot. """


class Message:
    def __init__(self, msgtype, **kwargs):
        self.msgtype = msgtype
        self.kwargs = kwargs

        # message has two list values, first is requried, second is optional
        arg_dict = {'text': [['content'], []],
                    'link': [['title', 'text', 'messageUrl'], ['picUrl']],
                    'markdown': [['title', 'text'], []]
                    }

        assert self.msgtype in arg_dict.keys(), 'msgtype is invalid.'

        for k, v in self.kwargs.items():
            print(k, v, arg_dict[self.msgtype])
            if k not in arg_dict[self.msgtype][0]:
                print('{} is not a valid key for msgtype {}'.format(
                    k, self.msgtype))
                raise KeyError()

        for key_word in arg_dict[self.msgtype][0]:
            if key_word not in self.kwargs.keys():
                print('{} is required for msgtype {}'.format(
                    key_word, self.msgtype))
                raise KeyError()

        dict_at = {}
        if 'atMobiles' in kwargs.keys():
            dict_at = {'atMobiles': kwargs['atMobiles']}
        if 'isAtAll' in kwargs.keys():
            dict_at['isAtAll'] = kwargs['isAtAll']

        if self.msgtype == 'text':
            self.msg = {
                "msgtype": "text",
                "text": {
                    "content": kwargs['content']
                },
                "at": dict_at
            }

        elif self.msgtype == 'link':
            picUrl = ""
            if 'picUrl' in kwargs.keys():
                picUrl = kwargs['picUrl']

            self.msg = {
                "msgtype": "link",
                "link": {
                    "text": kwargs['text'],
                    "title": kwargs['title'],
                    "picUrl": picUrl,
                    "messageUrl": kwargs['messageUrl']
                }
            }

        if self.msgtype == 'markdown':
            self.msg = {
                "msgtype": "markdown",
                "text": {
                    "title": kwargs['title'],
                    "text": kwargs['text']
                },
                "at": dict_at
            }

    def get(self):
        return self.msg
