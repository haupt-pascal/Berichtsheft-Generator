# Berichtsheft-Generator

Der Berichtsheft-Generator ist da, um sämtliche Berichte welche für die Ausbildung benötigt werden, automatisiert zu generieren. Er generiert diese anhand einer Zeitspanne und vorgefertigten gängigen Aufgaben die du, als Auszubildender, erledigst. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Vorbereitung

```python
randomList = {
    'Element',
    'Element',
    'Element',
}
```
Hier musst du die gängigsten Aufgaben eintragen, welche du erledigst. Anhand dessen werden folgend die Berichte generiert. Das ganze wird zufällig gewürfelt damit sich die Berichte auch nicht immer wiederholen und die Automatisierung nicht auffällt.

In die Vorlage_Neu.docx müssen der Name sowie die Abteilung getauscht werden, vergiss das nicht. Andernfalls 
sind alle Berichte falsch generiert.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)