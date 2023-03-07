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