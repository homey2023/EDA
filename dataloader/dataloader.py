import pandas as pd

def format_address_string(addresses):
    # Split the string of addresses into individual addresses
    addresses = addresses.split('\n')
    addresses = [address.strip() for address in addresses]

    # Extract the last road name from each address
    last_road_names = [address.split()[-1] for address in addresses]

    # Extract the si, gu, and road name from each address
    si_gu_road_names = [address.rsplit(' ', 1) for address in addresses]

    # Create a dictionary with the address components as keys and empty lists as values
    address_dict = {'Si': [], 'Gu': [], 'Road Name': [], 'Last Road Name': []}

    # Iterate over the addresses and add the components to the dictionary
    for i, address in enumerate(si_gu_road_names):
        address_dict['Si'].append(address[0].split()[0])
        address_dict['Gu'].append(address[0].split()[1])
        address_dict['Road Name'].append(address[1].strip())
        address_dict['Last Road Name'].append(last_road_names[i])

    # Create a pandas dataframe from the dictionary
    df = pd.DataFrame.from_dict(address_dict)

    return df
