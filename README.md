# odsAutomationPython
Mit `ods-utils-py` lässt sich direkt aus Python auf die Automation API von Opendatasoft zugreifen. Voraussetzung ist, dass die API freigeschaltet ist. Die vollständige Dokumentation der API ist [hier](https://help.opendatasoft.com/apis/ods-automation-v1/) zu finden.

---

## Installation

Installation with
```bash
pip install ods-utils-py
```

---

## Dependencies

TODO

---

## Usage

```python
import ods_utils_py as ods_utils

num_datasets = ods_utils.get_number_of_datasets()
print(f"Currently we have {num_datasets} datasets.") 
```
---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file in the repository for the full license text.
