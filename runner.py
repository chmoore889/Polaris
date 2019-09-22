import gmaps
import os

gmaps_client = gmaps.initiate_gmap_client()

# takes input from the user for now. eventually will be inputed through audio
starting_address = "100 Nicolls Rd, Stony Brook, NY 11790"
destination_address = gmaps.read_destination_address("addressFile.txt")


lats, lngs = gmaps.parse_gpx_temp_method()

geocode_start, geocode_dest = gmaps.geocode_addresses(
    gmaps_client, starting_address, destination_address)

start_coords = gmaps.get_start_coords(geocode_start)
dest_coords = gmaps.get_dest_coords(geocode_dest)

direction = gmaps.get_directions(
    gmaps_client, start_coords[0], start_coords[1], dest_coords[0], dest_coords[1])

parsed_directions = gmaps.parse_directions(direction)

gmaps.write_waypoints_to_file(parsed_directions)
gmaps.generate_map_instructions(parsed_directions)

