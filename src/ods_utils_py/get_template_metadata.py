from typing import Any, Dict, Optional
from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # requests_get, requests_put, ...
from ._config import get_base_url


def get_template_metadata(template_name: str, field_name: Optional[str] = None, *, dataset_id: Optional[str] = None,
    dataset_uid: Optional[str] = None) -> Dict[str, Any]:
    """
    Generic getter for dataset metadata.

    - If field_name is None:
        GET /datasets/{uid}/metadata/{template_name}/
        → returns the full template JSON
    - Else:
        GET /datasets/{uid}/metadata/{template_name}/{field_name}/
        → returns the field object

    Args:
        template_name: e.g. "dcat_ap_ch"
        field_name:    e.g. "rights" (None → full template)
        dataset_id:    dataset_id (mutually exclusive with dataset_uid)
        dataset_uid:   dataset_uid
    """
    if dataset_id is not None and dataset_uid is not None:
        raise ValueError("dataset_id and dataset_uid are mutually exclusive")
    if dataset_id is None and dataset_uid is None:
        raise ValueError("Either dataset_id or dataset_uid must be specified")
    if dataset_id is not None:
        dataset_uid = get_uid_by_id(dataset_id)

    base_url = get_base_url()
    if field_name is None:
        url = f"{base_url}/datasets/{dataset_uid}/metadata/{template_name}/"
    else:
        url = f"{base_url}/datasets/{dataset_uid}/metadata/{template_name}/{field_name}/"

    r = requests_get(url=url)
    r.raise_for_status()
    return r.json()


