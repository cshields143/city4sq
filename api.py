import foursquare

client = foursquare.Foursquare(
    client_id='Y1CPCQJRBWVHOPPLP1IHFWVYRSIGKNDY4PN32X1OWCSAVVPN',
    client_secret='1CEWCHG0YU00VP1JZ4P0T0VRNOX43FB2IIUE3G1F511TEGRX'
)

if __name__ == '__main__':
    print(client.venues.search(params={'near':'spokane wa'}))