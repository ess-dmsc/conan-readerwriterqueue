#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os

class ReaderWriterQueue(ConanFile):
    name = "readerwriterqueue"
    url = 'https://github.com/cameron314/readerwriterqueue'
    description='A fast single-producer, single-consumer lock-free queue for C++'
    license = "Simplified BSD/Boost Software License"
    version = "07e22ec"
    exports = "*.h"
    source_subfolder = "source_subfolder"

    def source(self):
        self.run("git clone " + self.url + ".git")
        self.run("cd " + self.name + " && git checkout " + self.version + " && cd ..")
        os.rename(self.name, self.source_subfolder)

    def build(self):
        pass # silence warning

    def package(self):
        include_dir  = os.path.join('include', 'readerwriterqueue')

        self.copy('readerwriterqueue.h', dst=include_dir, src=self.source_subfolder)
        self.copy('atomicops.h', dst=include_dir, src=self.source_subfolder)
        self.copy("LICENSE.md", dst="license", src=self.source_subfolder)
        
    def package_id(self):
        self.info.header_only()
