import pandas as pd
from PyKakao import Local

api = Local(service_key = "use-kakao-api-REST-key")

def roadname2address(df, column_name):
    addr = pd.DataFrame(
        columns=[
            "lot_addr",
            "depth1",
            "depth2",
            "depth3_legal",
            "depth3_admin",
            "road_addr",
            "roadname",
            "x",
            "y",
        ]
    )
    result = df[column_name].apply(lambda x: api.search_address(x, dataframe=True))

    for i, res in enumerate(result):
        road_address = df[column_name].iloc[i]
        roadname = road_address.split()[2]
        x = float(res["x"].item())
        y = float(res["y"].item())
        lot_df = api.geo_coord2regioncode(x, y, dataframe=True)
        lot_addr = lot_df.iloc[0]["address_name"]
        depth1 = lot_df.iloc[0]["region_1depth_name"]
        depth2 = lot_df.iloc[0]["region_2depth_name"]
        depth3_legal = lot_df.iloc[0]["region_3depth_name"]
        depth3_admin = lot_df.iloc[1]["region_3depth_name"]
        row = {
            "lot_addr": lot_addr,
            "depth1": depth1,
            "depth2": depth2,
            "depth3_legal": depth3_legal,
            "depth3_admin": depth3_admin,
            "road_addr": road_address,
            "roadname": roadname,
            "x": x,
            "y": y,
        }
        addr = addr.append(row, ignore_index=True)
    return addr


def lotnumber2address(df, column_name):
    pass

def coords2address(coords_list):

    addr = pd.DataFrame(
        columns = [
            "lamp_addr",
            "depth1", 
            "depth2", 
            "main_addr_no",
            "sub_addr_no", 
            "latitude",
            "longitude",
        ]
    )

    for i, res in enumerate(coords_list):
        x = float(res[0])
        y = float(res[1])
       
        response = api.geo_coord2address(x, y)
        
        if response['meta']['total_count'] == 1:
            lamp_addr = response['documents'][0]['address']["address_name"]
            depth1 = response['documents'][0]['address']["region_1depth_name"]
            depth2 = response['documents'][0]['address']["region_2depth_name"]
            main_addr_no = response['documents'][0]['address']['main_address_no']
            sub_addr_no = response['documents'][0]['address']['sub_address_no']
        
        row = {
            "lamp_addr" : lamp_addr, 
            "depth1" : depth1, 
            "depth2" : depth2, 
            "main_addr_no" : main_addr_no,
            "sub_addr_no" : sub_addr_no, 
            "latitude": y,
            "longitude": x,
        }
        
        addr = addr.append(row, ignore_index = True)
        
    return addr