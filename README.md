# Python Screenshots Capturer

A dead simple Python script to capture screenshots. Written mostly for demonstration purposes. Dependencies:

* [Keyboard](https://github.com/boppreh/keyboard)
* [MSS](https://github.com/BoboTiG/python-mss)
* Built-in modules (OS, Sys, Datetime)

How this program was built (Russian): https://www.youtube.com/watch?v=rJe_osIzqUY

## How to use it

Install the above dependencies manually or use [Poetry](https://python-poetry.org) to do the job for you:

```
poetry install
```

Run:

```
python python_screenshots/screenshots.py
```

Or with Poetry:

```
poetry run python python_screenshots\screenshots.py
```

Keep the window opened (it does not have to stay in focus) and press the `PrtScr` key to make a PNG screenshot. By default, screenshots are created in the same directory where your script resides, under the `screens` subdirectory.

To provide a custom subdirectory:

```
python python_screenshots/screenshots.py my/sub_dir
```

Stop the script with `Ctrl+Shift+X`.

## Building

To build an executable file you can use `pyinstaller`:

```
poetry run pyinstaller python_screenshots/screenshots.py -F
```

## Development

Install Poetry and run:

```
poetry install
```

Have fun.

## License

(c) [Ilya Bodrov-Krukowski](http://bodrovis.tech/), licensed under the [beer-ware license](https://fedoraproject.org/wiki/Licensing/Beerware).
