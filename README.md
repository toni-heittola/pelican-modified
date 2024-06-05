Pelican-modified - Fetching file modification time
==================================================

`pelican-modified` is an open source Pelican plugin to fetch file modification time for data files used in the Pelican. The plugin provides an automatic way to print modification time of data files used to generate datatables or glossaries (see for example [pelican-datatable](https://github.com/toni-heittola/pelican-datatable), [pelican-bglossary](https://github.com/toni-heittola/pelican-bglossary), and [pelican-btex](https://github.com/toni-heittola/pelican-btex) plugins).

**Author**

Toni Heittola (toni.heittola@gmail.com), [GitHub](https://github.com/toni-heittola), [Home page](https://homepages.tuni.fi/toni.heittola/)

Installation instructions
=========================

## Pelican installation

Make sure the directory where the plugin was installed is set in `pelicanconf.py`. For example if you installed in `plugins/pelican-modified`, add:

    PLUGIN_PATHS = ['plugins']

Enable pelican-modified:

    PLUGINS = ['pelican-modified']

Usage
=====

File modification time is injected to {modified::<path to file>} tags within the content.

Example:

    Date of modification: {modified::content/data/data.yaml}

## Parameters

Parameters for the plugin can be set in `pelicanconf.py' with following parameters:

| Parameter                 | Type      | Default       | Description  |
|---------------------------|-----------|---------------|--------------|
| MODIFIED_FORMAT           | String    | '%Y-%m-%d'    | Format given to strftime |
