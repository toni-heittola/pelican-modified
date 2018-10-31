# -*- coding: utf-8 -*-
"""
Plugin for Pelican to show file modification date
=================================================
Author: Toni Heittola (toni.heittola@gmail.com)

"""

import re
import copy
from past.builtins import long
import os.path
import shutil
import logging
from pelican import signals, contents

logger = logging.getLogger(__name__)
__version__ = '0.0.1'

# Default parameter values
modified_default_settings = {
    'date-format': '%Y-%m-%d',
}

modified_settings = copy.deepcopy(modified_default_settings)

def parse_tags(instance):
    global modified_settings

    regex = r"{date::(.*?)}"
    from datetime import datetime
    if instance._content is not None:
        content = instance._content
        if '{date::' in content:
            matches = re.finditer(regex, content, re.MULTILINE | re.IGNORECASE)
            map = {}

            for match_id, match in enumerate(matches):
                filename = match.group(1)

                if os.path.exists(filename):
                    modification_timestamp = os.path.getmtime(filename)
                    modification_date = datetime.utcfromtimestamp(modification_timestamp).strftime(modified_settings['date-format'])
                    map[match.group()] = modification_date

            for map_item in map:
                content = content.replace(map_item, map[map_item])

            instance._content = content

def init_default_config(pelican):
    global modified_default_settings

    if 'MODIFIED_DATEFORMAT' in pelican.settings:
        modified_default_settings['date-format'] = pelican.settings['MODIFIED_DATEFORMAT']


def register():
    signals.initialized.connect(init_default_config)
    #signals.page_generator_init.connect(init)
    #signals.article_generator_init.connect(init)

    #signals.article_generator_context.connect(add_head)
    #signals.page_generator_context.connect(add_head)

    signals.content_object_init.connect(parse_tags)
    #signals.article_generator_finalized.connect(move_resources)
