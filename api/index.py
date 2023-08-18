import json
from urllib.parse import unquote
from flask import Flask, abort, redirect
from flask_cors import CORS
from .hmcl import get_Latest_Version, version_sha1, version_verify, history_version
from .mcuuid import generate_json
from .blacklist import check_isinblacklist
from .zdjd import isZdjd, human2zdjd, zdjd2human

app = Flask(__name__)
CORS(app, resources=r"/*")


@app.route("/")
def index():
    return redirect(r"https://github.com/yokinanya/LuoYu7Api")


@app.route("/hmcl/<channel>/<version>/<options>")
def hmcl(channel, version, options):
    if version == "latest":
        version = get_Latest_Version(channel)
    if version == "history":
        versions_list = history_version(channel)
        response = json.dumps(versions_list)
        if options == "json":
            return response, 200, {"Content-Type": "application/json"}
        else:
            return abort(404)
    else:
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


@app.route("/zdjd/<mode>/<t>")
def zdjd(t: str, mode: str):
    t = unquote(t, 'utf-8')
    mode_list = ["zdjd2human", "human2zdjd", "auto"]
    callback = {}
    if mode not in mode_list:
        return abort(404)
    elif mode == "zdjd2human":
        callback["isZdjd"] = bool(isZdjd(t))
        if bool(isZdjd(t)) is True:
            human = zdjd2human(t)
            callback["result"] = human
        else:
            callback["result"] = "你输入的是假嘟语，请重新输入"
        response = json.dumps(callback)
        return response, 200, {"Content-Type": "application/json"}
    elif mode == "human2zdjd":
        callback["isZdjd"] = bool(isZdjd(t))
        zdjd = human2zdjd(t)
        callback["result"] = zdjd
        response = json.dumps(callback)
        return response, 200, {"Content-Type": "application/json"}
    elif mode == "auto":
        callback["isZdjd"] = bool(isZdjd(t))
        if isZdjd(t) is True:
            human = zdjd2human(t)
            callback["result"] = human
        else:
            zdjd = human2zdjd(t)
            callback["result"] = zdjd
        response = json.dumps(callback)
        return response, 200, {"Content-Type": "application/json"}
    else:
        return abort(404)