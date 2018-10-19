# -*- coding: utf-8 -*-

# From sUnnnn
# Q Q  1119506222


class SunMongodb(object):

    @staticmethod
    def insert_mongo(client, data):
        try:
            client.insert(data)
            return dict(code=200, data=data)
        except Exception as e:
            return dict(code=400, data=e)