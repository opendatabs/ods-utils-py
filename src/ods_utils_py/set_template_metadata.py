from typing import Any, Dict, Optional
from .get_uid_by_id import get_uid_by_id
from ._requests_utils import *  # requests_get, requests_put, ...
from ._config import get_base_url
from .set_dataset_public import set_dataset_public


def set_template_metadata( template_name: str, payload: Dict[str, Any], field_name: Optional[str] = None, *,
    dataset_id: Optional[str] = None,dataset_uid: Optional[str] = None, publish: bool = True) -> Dict[str, Any]:
    """
    Generic setter for dataset metadata.

    - If field_name is None:
        PUT /datasets/{uid}/metadata/{template_name}/
        → payload must be the full template JSON
    - Else:
        PUT /datasets/{uid}/metadata/{template_name}/{field_name}/
        → payload must be the field object

    Args:
        template_name: e.g. "dcat_ap_ch"
        payload:       full template or field object
        field_name:    e.g. "license" (None → full template)
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

    r = requests_put(url=url, json=payload)
    r.raise_for_status()

    if publish:
        set_dataset_public(dataset_uid=dataset_uid)
    return r.json()
