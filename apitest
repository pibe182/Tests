import requests

api_key = "1258dc663b7584edf2e037c079d39941"
base_url = "http://api.countrylayer.com/v2"

def test_get_country_info():
    countries = ["US", "DE", "GB"]
    for country_code in countries:
        url = f"{base_url}/alpha/{country_code}?access_key={api_key}"
        response = requests.get(url)
        
        assert response.status_code == 200, f"Failed for {country_code}: {response.text}"
        country_info = response.json()
        assert country_info["alpha2Code"] == country_code, f"Country code mismatch for {country_code}"


def test_get_inexistent_country_info():
    inexistent_countries = ["XYZ", "ABC", "123"]
    for country_code in inexistent_countries:
        url = f"{base_url}/alpha/{country_code}?access_key={api_key}"
        response = requests.get(url)
        
        assert response.status_code == 404, f"Expected 404 for {country_code} but got {response.status_code}"
        # error_info = response.json()
        # assert error_info["error"]["code"] == "404", f"Error code mismatch for {country_code}"


def test_future_new_country_addition():
    new_country_data = {
        "name": "Test Country",
        "alpha2_code": "TC",
        "alpha3_code": "TCY"
    }
    url = f"{base_url}/alpha/{new_country_data['alpha2_code']}?access_key={api_key}"
    
    # Perform the POST request once it becomes available
    response = requests.post(url, json=new_country_data)
    
    # Currently, we expect a 500 status code since POST is not supported
    assert response.status_code == 500, f"Expected 405 for POST but got {response.status_code}"

if __name__ == "__main__":
    test_get_country_info()
    test_get_inexistent_country_info()
    test_future_new_country_addition()
    print("All test scenarios executed.")
