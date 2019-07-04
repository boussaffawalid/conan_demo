cmake_minimum_required(VERSION 3.4.0 FATAL_ERROR)
project(demo VERSION 1.0.0)

option(USE_CONAN "use conan to build" ON)


if(USE_CONAN)
	include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
else()
	include(deps.cmake)
    find_package(zlib ${ZLIB_VERSION} EXACT REQUIRED)
endif()
