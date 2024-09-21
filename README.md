<p align="center">
<a href="https://imgbb.com/"><img src="https://i.ibb.co/0cnvC3R/JTCP-LOGO.png" alt=JTCP-Logo" border="0" width=250 height=250/></a>
</p>

-----------

# JTCP
**JTCP** (**J**SON **t**o **C**SS **p**reprocessor) is a project that was made for no reason whatsoever and doesn't bring much to this world, but still may be used 🦅

## Installation
To install and use JTCP, you need to visit the **Releases page** on this github repository, and download the latest `.zip` archive, then unarchive it and you will find the `jtcp.exe` executable (Windows only) that you can use. If you are curious / unsure because of security concerns, the executable was built via **PyInstaller**, and you can use JTCP with no issues whatsoever by just running the `.py` file directly from the source code of this repository. The executable is there just for easier usage.

## How to use?
To use JTCP, _either by using `.py` script or the executable file_, you need to run this command:
```sh
jtcp *.json
```
Where `*` is your `.json` file name, for example:
```sh
jtcp example.json
```
After that, a new `.css` file will be created with the desired CSS styles.

## Format
Here's how you write JSON properly to use with JTCP:
```json
[
  {
    "name": "body",
    "class": ["class_name1", "class_name2"],
    "id": ["some_id_lol_idk"],
    "style": {
      "font-family": "14",
      "color": "red"
    }
  },
  {
    "name": "_",
    "class": ["class_name_hmhmhm"],
    "style": {
      "color": "blue"
    }
  },
  {
    "name": "_",
    "id": ["button_id"],
    "other_attr": ["hover"],
    "style": {
      "color": "black"
    }
  }
]
```
Basically, the whole JSON file is a single huge list, where each element of that list is a dictionary (object, `{...}`), containing following elements:
- `"name"` is the name of the CSS style, for example if the name is set to `body` it will output something like `body ... { ... }`. If the name is set to `"_"`, its handled as it was an empty name (`""`).
- `"class"` is a list of strings, where each element is a string (class name) for that CSS style.
- `"id"` is a list of IDs, where each element is a string (ID name) for that CSS style.
- `"other_attr"` is a list containing other attributes that don't follow in the previous categories, f.e. to add `:hover` to your CSS style, you will need to use something like: `"other_attr": ["hover"]`.
- `"style"` is a dictionary (object, `{...}`), where each key & value pair is a CSS style attribute. For example this:
```json
"style": {
  "color": "red"
}
```
would result in this CSS output:
```css
{
  color: red
}
```
