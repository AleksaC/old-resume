#!/usr/bin/env python

import os
from lxml import etree

file_path = "/etc/ImageMagick-6/policy.xml"

with open(file_path, "r+") as f:
    file_contents = f.read()

    root = etree.fromstring(file_contents)
    policy = root.xpath('//policy[@pattern="PDF"]')[0]
    policy.attrib["rights"] = "read|write"

    f.seek(file_contents.decode().find("<policymap>"))
    f.write(etree.tostring(root))
    f.truncate()
