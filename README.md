Pelican-modified - File modification date fetching for Pelican
==================================================================

`pelican-modified` is an open source Pelican plugin to fetch file modification date for data files used in the Pelican. The plugin provides an automatic way to print modificatin date of data files used to generate datatables or glossaies (see for example [pelican-datatable](https://github.com/toni-heittola/pelican-datatable), [pelican-bglossary](https://github.com/toni-heittola/pelican-bglossary), and [pelican-btex](https://github.com/toni-heittola/pelican-btex) plugins).

**Author**

Toni Heittola (toni.heittola@gmail.com), [GitHub](https://github.com/toni-heittola), [Home page](http://www.cs.tut.fi/~heittolt/)

Installation instructions
=========================

## Pelican installation

Make sure the directory where the plugin was installed is set in `pelicanconf.py`. For example if you installed in `plugins/pelican-modified`, add:

    PLUGIN_PATHS = ['plugins']

Enable pelican-modified:

    PLUGINS = ['pelican-modified']

Usage
=====

File modification date is injected to {date::<path to file>} tags within the content.

Example:

    Date of modification: {date::content/data/data.yaml}

## Parameters

Parameters for the plugin can be set in `pelicanconf.py' with following parameters:

| Parameter                 | Type      | Default       | Description  |
|---------------------------|-----------|---------------|--------------|
| MODIFIED_DATEFORMAT       | String    | '%Y-%m-%d'    | Date format given to strftime |
