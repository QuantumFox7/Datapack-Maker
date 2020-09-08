from easygui import multenterbox
from os import getcwd, mkdir, chdir, path

title = "Quantum Fox's Datapack Maker V1"
(packname, version, author) = multenterbox("Please enter the required information to create datapack", title, ["Pack Name", "Version", "Author"])
Dir = getcwd()

dirstm = [path.join(Dir, f"{packname}"),
          path.join(Dir, f"{packname}\\data"),
          path.join(Dir, f"{packname}\\data\\minecraft"),
          path.join(Dir, f"{packname}\\data\\{packname}"),
          path.join(Dir, f"{packname}\\data\\minecraft\\tags"),
          path.join(Dir, f"{packname}\\data\\minecraft\\tags\\functions"),
          path.join(Dir, f"{packname}\\data\\{packname}\\functions"),
          path.join(Dir, f"{packname}\\data\\{packname}\\recipes")
          ]

packmcmeta = '''{
    "pack": {
        "pack_format": 1, 
        "description": "packname Vversion, by author"
    }
}
'''.replace("packname", packname.replace(" ", "")).replace("version", version).replace("author", author)

loadjson = '''{
    "values": [
        "test:load"
    ]
}
'''

tickjson = '''{
    "values": [
        "test:tick"
    ]
}
'''

readmetxt = "Create custom recipes on https://crafting.thedestruc7i0n.ca/ and then paste them in this folder!"

def CreateFile(name, contents, path):
    chdir(path)
    file = open(name, "w")
    file.write(contents) 
    file.close()

def Construct():
    for Path in dirstm: mkdir(Path)
    CreateFile("pack.mcmeta", packmcmeta, path.join(Dir, f"{packname}"))
    CreateFile("load.json", loadjson, path.join(Dir, f"{packname}\\data\\minecraft\\tags\\functions"))
    CreateFile("tick.json", tickjson, path.join(Dir, f"{packname}\\data\\minecraft\\tags\\functions"))
    CreateFile("load.mcfunction", "", path.join(Dir, f"{packname}\\data\\{packname}\\functions"))
    CreateFile("tick.mcfunction", "", path.join(Dir, f"{packname}\\data\\{packname}\\functions"))
    CreateFile("template.mcfunction", "", path.join(Dir, f"{packname}\\data\\{packname}\\functions"))
    CreateFile("README.txt", readmetxt, path.join(Dir, f"{packname}\\data\\{packname}\\recipes"))

Construct()
