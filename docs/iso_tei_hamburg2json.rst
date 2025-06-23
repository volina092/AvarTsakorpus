Spoken ISO/TEI convertor
========================

This document explains how to convert media-aligned texts in ISO/TEI format to Tsakorpus JSON. See general information about source convertors and their configuration files :doc:`here </src_convertors>`.

Convertor: ``/src_convertors/iso_tei_hamburg2json.py``.

Spoken ISO/TEI format
---------------------

TEI_ is a format for annotating texts. *ISO/TEI for spoken language* is a subset of TEI that describes how spoken language data can be encoded in TEI. Despite formalizing some aspects, both TEI in general and spoken ISO/TEI allow for too much variation: same data can be encoded in thousands different ways. This is why it is impossible to create a convertor that could work with *any* spoken ISO/TEI data. This convertor can work with a `specific version of spoken ISO/TEI <https://www.aclweb.org/anthology/W19-0310.pdf>`_ used in the INEL_ project.

.. _TEI: https://tei-c.org/
.. _INEL: https://www.slm.uni-hamburg.de/inel.html

Configuration
-------------

The additional parameters concern extraction of document-level and speaker-level metadata from CoMa files.

- ``coma_meta_conversion`` -- dictionary that establishes a mapping from key names used in CoMa communication metadata to tsakorpus document-level metadata fields.

- ``coma_meta_speaker_conversion`` -- dictionary that establishes a mapping from key names used in CoMa speaker metadata to tsakorpus metadata fields.

- ``coma_meta_speaker_lang_conversion`` -- dictionary that establishes a mapping from key names used in the *Languages* section of CoMa speaker metadata to tsakorpus metadata fields.

See also documentation on :doc:`general parameters </src_convertors>` and :doc:`glosses-to-tags conversion </src_convertors_gloss>`.
