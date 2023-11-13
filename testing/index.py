venue = {'fsq_id': '5b2932a0f5e9d70039787cf2',
 'categories': [{'id': 13306,
   'name': 'Taco Restaurant',
   'short_name': 'Tacos',
   'plural_name': 'Taco Restaurants',
   'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/taco_',
    'suffix': '.png'}}],
 'chains': [],
 'closed_bucket': 'LikelyOpen',
 'geocodes': {'drop_off': {'latitude': 40.702449, 'longitude': -73.987411},
  'main': {'latitude': 40.702573, 'longitude': -73.987408},
  'roof': {'latitude': 40.702573, 'longitude': -73.987408}},
 'link': '/v3/places/5b2932a0f5e9d70039787cf2',
 'location': {'address': '141 Front St',
  'census_block': '360470021002009',
  'country': 'US',
  'cross_street': 'Pearl St',
  'dma': 'New York',
  'formatted_address': '141 Front St (Pearl St), New York, NY 11201',
  'locality': 'New York',
  'postcode': '11201',
  'region': 'NY'},
 'name': 'Los Tacos Al Pastor',
 'related_places': {},
 'timezone': 'America/New_York',
 'rating': 8.2, 'signals': 60, 'likes_count': 45}

def params_string(params):
    return '&'.join([f'{k}={v}' for k,v in params.items()])

# id, name, and location
def extract_details_from_venue(venue):
    id = venue['fsq_id']
    name = venue['name']
    location = [venue['geocodes']['drop_off']['latitude'], venue['geocodes']['drop_off']['longitude']]
    # {'latitude': 40.702449, 'longitude': -73.987411}

    return {'id': id, 'name': name, 'location': location}

def extract_likes(venue):
    return {k:v for k,v in venue.items() if k in ['rating', 'signals', 'likes_count']}