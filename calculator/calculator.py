# 두 지점의 위경도로 두 지점 사이 거리 구하는 함수
#코드 출처: https://ko.martech.zone/calculate-great-circle-distance/
from numpy import sin, cos, arccos, pi, round
import pandas as pd
import numpy as np
def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2, unit = 'kilometers'):
    
    theta = longitude1 - longitude2
    
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    
    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)


# 비상벨, 유흥업소, 경찰관서, 안심이cctv, 여성 안심 택배함, 여성 안심지킴이집

# 비상벨
df_bell = pd.read_csv('EDA/dataset/emergency_bell/12_04_09_E_안전비상벨위치정보.csv')

def calculate_dist_from_bell(latitude, longitude):

    df_dist = pd.DataFrame(
        columns = ['bells_road_addr','bells_addr', 'distance']
    )

    df_bell = pd.read_csv('EDA/dataset/emergency_bell/12_04_09_E_안전비상벨위치정보.csv')

    for ind in df_bell.index:
        #print(df_bell['WGS84위도'][ind],df_bell['WGS84경도'][ind])

        dist = getDistanceBetweenPointsNew(latitude, longitude, df_bell['WGS84위도'][ind], df_bell['WGS84경도'][ind])
        row = {
            df_bell['소재지도로명주소'][ind],
            df_bell['소재지지번주소'][ind],
            dist
        }

        df_dist = df_dist.append(row, ignore_index = True)

def rate_with_bells(df_bell):
    dist = df_bell['distance']
    for d in dist:
        if d < 1:
            return True   #반경 1km 이내 안심벨 있음.
        else:
            return False  #반경 1km 이내 안심벨 없음.

