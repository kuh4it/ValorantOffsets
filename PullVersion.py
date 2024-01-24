# github.com/ultracage
import requests

def get_valorant_version_details(api_url):
    try:
        response = requests.get(api_url + "/v1/version")
        response.raise_for_status()
        
        version_data = response.json().get('data', {})
        
        valorant_version = version_data.get('version', 'N/A')
        engine_version = version_data.get('engineVersion', 'N/A')
        build_date = version_data.get('buildDate', 'N/A')
        riot_client_version = version_data.get('riotClientVersion', 'N/A')

        return f"// VALORANT v{valorant_version}\n" \
               f"// Unreal Engine v{engine_version}\n" \
               f"// Game Build Date: {build_date}\n" \
               f"// Riot Client Version: {riot_client_version}"
    except requests.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'An error occurred: {err}'

api_url = 'https://valorant-api.com'

valorant_version_details = get_valorant_version_details(api_url)
valorant_version_details

