sample_weathers = {
    'sunny' : {
        'hot' : {
            'humid': {
                'windy': 0,
                'not_windy': 0
            }
        },
        'cool' : {
            'humid': {
                'not_windy': 0
            },
            'dry' : {
                'windy': 1
            }
        },
        'cold' : {
            'dry' : {
                'not_windy': 1
            }
        }
    },
    'rainy' : {
        'cool' : {
            'humid': {
                'windy': 0,
                'not_windy': 1
            },
            'dry' : {
                'not_windy': 1
            }
        },
        'cold' : {
            'dry' : {
                'windy': 0,
                'not_windy': 1
            }
        }
    },
    'cloudy' : {
        'hot' : {
            'humid': {
                'not_windy': 1
            },
            'dry' : {
                'not_windy': 1
            }
        },
        'cool' : {
            'humid': {
                'windy': 1
            }
        },
        'cold' : {
            'dry' : {
                'windy': 1
            }
        }
    }
}

# weather = { # Percentage of each condition / 10
#     'sunny' : 4,
#     'rainy' : 6,
#     'cloudy' : 10,
#     'hot' : 5,
#     'cool' : 6.66,
#     'cold' : 7.5,
#     'humid' : 4.28,
#     'dry' : 6.25,
#     'windy' : 2.5,
#     'not_windy' : 7.5
# }

# import pickle

# file = open('weather.txt', 'wb')
# pickle.dump(weather, file)
# file.close()