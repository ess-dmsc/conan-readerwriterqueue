#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os

class ConcurrentQueue(ConanFile):
    name = "concurrentqueue"
    url = 'https://github.com/cameron314/concurrentqueue'
    description='A fast multi-producer, multi-consumer lock-free queue for C++11'
    license = "Simplified BSD/Boost Software License"
    version = "8f7e861"
    exports = "*.h"
    source_subfolder = "source_subfolder"

    def source(self):
        self.run("git clone " + self.url + ".git")
        self.run("cd " + self.name + " && git checkout " + self.version + " && cd ..")
        os.rename(self.name, self.source_subfolder)

    def build(self):
        pass # silence warning

    def package(self):
        include_dir  = os.path.join('include', 'concurrentqueue')

        self.copy('concurrentqueue.h', dst=include_dir, src=self.source_subfolder)
        self.copy('blockingconcurrentqueue.h', dst=include_dir, src=self.source_subfolder)
        self.copy("LICENSE.md", dst="license", src=self.source_subfolder)
        
    def package_id(self):
        self.info.header_only()
