from flask import Flask, redirect, abort
import xml.etree.ElementTree as ET
import requests
import json

app = Flask(__name__)


# /hmcl/dev/json

@app.route('/hmcl/<channel>/<version>/<options>')
def hmcl(channel, version, options):
    if version == "latest":
        version = get_Latest_Version(channel)
    if version_verify(channel, version) is True:
        version_json = {}
        version_json['exe'] = f"https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/hmcl-{channel}-{version}.exe"
        version_json['jar'] = f"https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/hmcl-{channel}-{version}.jar"
        version_json['version'] = version
        version_json['universal'] = r"https://www.mcbbs.net/forum.php?mod=viewthread&tid=142335"
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


def get_Latest_Version(channel):
    ExistingVersionXML = requests.get(
        f'https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/maven-metadata.xml').text
    ExistingVersion = ET.fromstring(ExistingVersionXML)
    element = ExistingVersion.find('versioning/latest')
    if element is not None:
        return element.text
    else:
        return None

def version_verify(channel, version):
    if requests.get(f'https://repo1.maven.org/maven2/org/glavo/hmcl/hmcl-{channel}/{version}/').status_code == 404:
        return False
    else:
        return True
