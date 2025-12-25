import requests
import logging
import json

logger = logging.getLogger('security')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def enrich_event_data(ip_address):
    if not ip_address or ip_address in ['127.0.0.1', '::1']:
        return None
    
    try:
        url = f"http://ip-api.com/json/{ip_address}?fields=6684671"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return {
                    'city': data.get('city'),
                    'state': data.get('regionName'),
                    'country': data.get('country'),
                    'latitude': data.get('lat'),
                    'longitude': data.get('lon'),
                    'isp': data.get('isp'),
                    'asn': data.get('as'),
                    'is_proxy': data.get('proxy', False),
                    'is_vpn': data.get('vpn', False),
                }
    except Exception as e:
        logger.error(f"Geolocation enrichment failed for {ip_address}: {str(e)}")
    
    return None

def get_device_info(user_agent):
    device_type = 'Unknown'
    if user_agent.is_mobile:
        device_type = 'Mobile'
    elif user_agent.is_tablet:
        device_type = 'Tablet'
    elif user_agent.is_pc:
        device_type = 'PC'
    elif user_agent.is_bot:
        device_type = 'Bot'
        
    return {
        'device_type': device_type,
        'os_family': user_agent.os.family,
        'os_version': user_agent.os.version_string,
        'browser_family': user_agent.browser.family,
        'browser_version': user_agent.browser.version_string,
        'user_agent_string': str(user_agent.ua_string)
    }
