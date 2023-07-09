import json
from flask import Flask, abort, redirect
from flask_cors import CORS
from .hmcl import get_Latest_Version, version_sha1, version_verify
from .mcuuid import generate_json
from .blacklist import check_isinblacklist

app = Flask(__name__)
CORS(app, resources=r"/*")


@app.route("/")
def index():
    return redirect(r"https://github.com/yokinanya/LuoYu7Api")


@app.route("/hmcl/<channel>/<version>/<options>")
def hmcl(channel, version, options):
    if version == "latest":
        version = get_Latest_Version(channel)
    if version_verify(channel, version) is True:
        version_json = {}
        exesha1, jarsha1 = version_sha1(channel, version)
        version_json[
            "exe"
        ] = f"https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/hmcl-{channel}-{version}.exe"
        version_json["exesha1"] = exesha1
        version_json[
            "jar"
        ] = f"https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/hmcl-{channel}-{version}.jar"
        version_json["jarsha1"] = jarsha1
        version_json["version"] = version
        version_json[
            "universal"
        ] = r"https://www.mcbbs.net/forum.php?mod=viewthread&tid=142335"
        response = json.dumps(version_json)
        if options == "json":
            return response, 200, {"Content-Type": "application/json"}
        elif options == "exe":
            return redirect(f"{version_json['exe']}")
        elif options == "jar":
            return redirect(f"{version_json['jar']}")
        else:
            return abort(404)
    else:
        return abort(404)


@app.route("/mcuuid/<nickname>")
def mcuuid(nickname):
    uuidj = generate_json(nickname)
    response = json.dumps(uuidj)
    return response, 200, {"Content-Type": "application/json"}


@app.route("/qqban/<qqid>")
def qqban(qqid: int):
    callback = {}
    status, reason, type = check_isinblacklist(qqid)
    callback["qqid"] = int(qqid)
    callback["status"] = status
    callback["reason"] = reason
    callback["type"] = type
    response = json.dumps(callback)
    return response, 200, {"Content-Type": "application/json"}
