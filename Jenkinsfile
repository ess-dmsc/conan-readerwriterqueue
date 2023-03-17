@Library('ecdc-pipeline')
import ecdcpipeline.ContainerBuildNode
import ecdcpipeline.ConanPackageBuilder

project = "conan-readerwriterqueue"

conan_user = "ess-dmsc"
conan_pkg_channel = "stable"

containerBuildNodes = [
  'centos': ContainerBuildNode.getDefaultContainerBuildNode('centos7-gcc11'),
  'debian': ContainerBuildNode.getDefaultContainerBuildNode('debian11'),
  'ubuntu': ContainerBuildNode.getDefaultContainerBuildNode('ubuntu2204')
]

packageBuilder = new ConanPackageBuilder(this, containerBuildNodes, conan_pkg_channel)
packageBuilder.defineRemoteUploadNode('centos')

builders = packageBuilder.createPackageBuilders { container ->
  packageBuilder.addConfiguration(container)
}

node {
  checkout scm

  if (env.ENABLE_MACOS_BUILDS.toUpperCase() == 'TRUE') {
    builders['macOS'] = get_macos_pipeline()
  }
  
  parallel builders

  // Delete workspace when build is done.
  cleanWs()
}

def get_macos_pipeline() {
  return {
    node('macos') {
      cleanWs()
      dir("${project}") {
        stage("macOS: Checkout") {
          checkout scm
        }  // stage

        stage("macOS: Package") {
          sh "conan create . ${conan_user}/${conan_pkg_channel} \
            --settings readerwriter:build_type=Release \
            --build=outdated"

          sh "conan create . ${conan_user}/${conan_pkg_channel} \
            --settings readerwriter:build_type=Release \
            --build=outdated"
        }  // stage
      }  // dir
    }  // node
  }  // return
}  // def
