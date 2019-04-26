# autograde240
*A tool for autograding 18240 assignments*

Intended for Python 2.7.5, with an intention of moving over to Python 3 in the
near future.

## Requirements
- Python 2.7.5 or newer Python 2 installs
- Synopsys VCS

## Usage
Check usage by running
```bash
autograde240 -h
```

Ensure your file hierarchy looks like the following:
```
.
+-- STAFF
|   +-- config.json
|   +-- *.sv
+-- studentID1
|   +-- *.sv
+-- studentID2
|   +-- *.sv
...
```
Where the `STAFF` and `studentID#` folders are in the same level. **This must be
satisfied for the tool to work properly**.

Run the `autograde240` executable inside of the `STAFF` folder.

## Config files
All config files must be of the `.json` format, and structured like so:
```json
{                                   # main config object
    "assignment": "hwX",            # string
    "rubric": [                     # array of rubric item objects
        {                           # rubric item object
            "problem": 1,           # number
            "files": null,          # array of strings, each being the file
                                      name that the students should have
                                      submitted
            "modules": null,        # array of strings, each being the module
                                      that should exist in their files
            "tb_files": null,       # array of strings, each being the file
                                      where testbenches are written
            "testbenches": null     # array of strings, each being the name of
                                      the testbenches to run student code against
        }
    ]
}
```
Where the text following the `#` denotes the data type and a brief description.

