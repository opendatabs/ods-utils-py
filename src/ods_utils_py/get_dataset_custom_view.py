from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # imports requests_get, requests_post, etc.
from ._config import get_base_url

def get_dataset_custom_view(dataset_id: str = None, dataset_uid: str = None) -> dict:
    """
    Returns a custom_view dictionary. Can be specified by either the dataset_id or the dataset_uid.
    Args:
        dataset_id:
        dataset_uid:

    Returns: A dictionary of the form

    custom_view = {
        "custom_view_enabled": bool
        "custom_view_title": str
        "custom_view_icon": str
        "custom_view_html": str
        "custom_view_css": str
        "table_fields": list
        "map_disabled": bool
    }

    """
    if dataset_id is not None and dataset_uid is not None:
        exit(f"Error: dataset_id ({dataset_id}) and dataset_uid ({dataset_uid}) can't both be specified.")
    if dataset_id is None and dataset_uid is None:
        exit("Error: dataset_id or dataset_uid have to be specified.")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)
    base_url = get_base_url()

    r = requests_get(url=f"{base_url}/datasets/{dataset_uid}")

    if not r.ok:
        r.raise_for_status()

    custom_view_enabled = r.json()['metadata']['visualization']['custom_view_enabled']['value']
    custom_view_title = r.json()['metadata']['visualization']['custom_view_title']['value']
    custom_view_icon = r.json()['metadata']['visualization']['custom_view_icon']['value']
    custom_view_html = r.json()['metadata']['visualization'].get('custom_view_html', {}).get('value', '')
    custom_view_css = r.json()['metadata']['visualization'].get('custom_view_css', {}).get('value', '')
    table_fields = r.json()['metadata']['visualization']['table_fields']['value']
    map_disabled = r.json()['metadata']['visualization']['map_disabled']['value']

    custom_view_dict = {
        "custom_view_enabled": custom_view_enabled,
        "custom_view_title": custom_view_title,
        "custom_view_icon": custom_view_icon,
        "custom_view_html": custom_view_html,
        "custom_view_css": custom_view_css,
        "table_fields": table_fields,
        "map_disabled": map_disabled,
    }
    return custom_view_dict
