from index import params_string, extract_details_from_venue, extract_likes, venue

def test_params_string():
    params_1 = {'ll': "40.7,-74", "query": "tacos"}
    params_2 = {'ll': '54.2,-98', "query": "pizza", "borough": 'M'}
    two_key_values = params_string(params_1)
    three_key_values = params_string(params_2)
    assert two_key_values == 'll=40.7,-74&query=tacos'
    assert three_key_values == 'll=54.2,-98&query=pizza&borough=M'

def test_extract_details_from_venue():
    venue_keys = extract_details_from_venue(venue)
    assert venue_keys == {'id': '5b2932a0f5e9d70039787cf2', 'name': 'Los Tacos Al Pastor', 'location': [40.702449, -73.987411]}

def test_extract_likes():
    values = extract_likes(venue)
    assert values == {'rating': 8.2, 'signals': 60, 'likes_count': 45}
    
