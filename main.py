from evaluation import *
import pickle

def Process():
    with open('weather.txt', 'rb') as handle:
        weathers = handle.read()

    weathers = pickle.loads(weathers)
    for weather in sample_weathers:
        for tempurature in sample_weathers[weather]:
            for humidity in sample_weathers[weather][tempurature]:
                for wind_level in sample_weathers[weather][tempurature][humidity]:
                    point = weathers[weather] + weathers[humidity] + weathers[wind_level] + weathers[tempurature]
                    if point > 22.03: # 22.03 = ((average_of"YES") / number_of("YES") + (average_of "NO") / number_of("NO")) / 2
                        if sample_weathers[weather][tempurature][humidity][wind_level] == 0:
                            weathers[weather] *= (1 - weathers[weather] / point)
                            weathers[humidity] *= (1 - weathers[weather] / point)
                            weathers[wind_level] *= (1 - weathers[weather] / point)
                            weathers[tempurature] *= (1 - weathers[weather] / point)
                    else:
                        if sample_weathers[weather][tempurature][humidity][wind_level] == 1:
                            weathers[weather] /= (1 - weathers[weather] / point)
                            weathers[humidity] /= (1 - weathers[weather] / point)
                            weathers[wind_level] /= (1 - weathers[weather] / point)
                            weathers[tempurature] /= (1 - weathers[weather] / point)
    with open('weather.txt', 'wb') as handle:
        pickle.dump(weathers, handle)

def Output_tree():

    with open('weather.txt', 'rb') as handle:
        weathers = handle.read()

    weathers = pickle.loads(weathers)

    for weather in ['sunny', 'rainy', 'cloudy']:
        print(weather + ": ")
        for tempurature in ['hot', 'cool', 'cold']:
            print("  " + tempurature + ": ")
            for humidity in ['humid', 'dry']:
                print("    " + humidity + ": ")
                for wind_level in ['windy', 'not_windy']:
                    point = weathers[weather] + weathers[humidity] + weathers[wind_level] + weathers[tempurature]
                    print("      " + wind_level + ": " + ("YES" if (point - 22.03) > 0 else "NO"))

if __name__ == '__main__':
    times = 1000
    while times >= 0:
        Process()
        times -= 1

    Output_tree()