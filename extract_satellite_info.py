def extract_satellite_info(satellites):
    # Initialize lists to hold the satellite names and IDs
    satnames = []
    satids = []

    # Iterate through each satellite in the list
    for satellite in satellites:
        # Extract 'satname' and 'satid'
        satnames.append(satellite.get('satname'))
        satids.append(str(satellite.get('satid')))

    # Join the lists into strings
    satnames_str = ', '.join(satnames)
    satids_str = ', '.join(satids)

    return satnames_str, satids_str