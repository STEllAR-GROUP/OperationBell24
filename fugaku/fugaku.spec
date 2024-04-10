octotiger@master%gcc@12.2.0~cuda~fast_fp_contract~ipo+kokkos+kokkos_hpx_kernels~rocm~sycl build_system=cmake build_type=Release griddim=8 hydro_host_tasks=8 monopole_host_tasks=1 multipole_host_tasks=16 simd_extension=SVE simd_library=STD theta_minimum=0.34 arch=linux-rhel8-a64fx
    ^boost@1.80.0%gcc@12.2.0+atomic+chrono~clanglibcpp~container+context~contract~coroutine+date_time~debug+exception~fiber+filesystem+graph~graph_parallel~icu+iostreams~json+locale+log+math~mpi+multithreaded~nowide~numpy~pic+program_options~python+random+regex+serialization+shared+signals~singlethreaded~stacktrace+system~taggedlayout+test+thread+timer~type_erasure~versionedlayout+wave build_system=generic context-impl=fcontext cxxstd=17 patches=a440f96 visibility=hidden arch=linux-rhel8-a64fx
        ^bzip2@1.0.6%gcc@12.2.0~debug~pic+shared build_system=generic arch=linux-rhel8-a64fx
        ^zlib@1.2.11%gcc@12.2.0+optimize+pic+shared build_system=makefile arch=linux-rhel8-a64fx
    ^cmake@3.24.3%gcc@12.2.0~doc+ncurses~ownlibs~qt build_system=generic build_type=Release arch=linux-rhel8-a64fx
        ^curl@7.61.1%gcc@12.2.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2+nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-rhel8-a64fx
        ^expat@2.4.8%gcc@12.2.0+libbsd build_system=autotools arch=linux-rhel8-a64fx
            ^libbsd@0.11.5%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
                ^libmd@1.0.4%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
        ^libarchive@3.5.2%gcc@12.2.0+iconv build_system=autotools compression=bz2lib,lz4,lzma,lzo2,zlib crypto=mbedtls libs=shared,static programs=none xar=expat arch=linux-rhel8-a64fx
            ^libiconv@1.16%gcc@12.2.0 build_system=autotools libs=shared,static arch=linux-rhel8-a64fx
            ^lz4@1.8.3%gcc@12.2.0 build_system=makefile libs=shared,static arch=linux-rhel8-a64fx
            ^lzo@2.10%gcc@12.2.0 build_system=autotools libs=shared,static arch=linux-rhel8-a64fx
            ^mbedtls@2.28.0%gcc@12.2.0+pic build_system=makefile build_type=Release libs=static arch=linux-rhel8-a64fx
            ^xz@5.2.4%gcc@12.2.0~pic build_system=autotools libs=shared,static arch=linux-rhel8-a64fx
        ^libuv@1.46.0%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
        ^ncurses@6.1%gcc@12.2.0~symlinks+termlib abi=none build_system=autotools arch=linux-rhel8-a64fx
        ^rhash@1.4.2%gcc@12.2.0 build_system=makefile patches=093518c,3fbfe46 arch=linux-rhel8-a64fx
    ^cppuddle@0.3.0%gcc@12.2.0+allocator_counters+buffer_content_recycling+buffer_recycling~enable_gpu_tests+hpx~ipo build_system=cmake build_type=RelWithDebInfo max_number_gpus=1 number_buffer_buckets=128 arch=linux-rhel8-a64fx
    ^hdf5@1.12.2%gcc@12.2.0~cxx~fortran+hl~ipo~java~mpi+shared+szip+threadsafe+tools api=default build_system=cmake build_type=RelWithDebInfo arch=linux-rhel8-a64fx
        ^libaec@1.0.6%gcc@12.2.0~ipo+shared build_system=cmake build_type=RelWithDebInfo arch=linux-rhel8-a64fx
        ^pkgconf@1.4.2%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
    ^hpx@1.9.1%gcc@12.2.0~async_cuda~async_mpi~cuda~disable_async_gpu_futures~examples+generic_coroutines~ipo~rocm~sycl~tools build_system=cmake build_type=RelWithDebInfo cxxstd=17 instrumentation=none malloc=jemalloc max_cpu_count=64 networking=mpi sycl_target_arch=none arch=linux-rhel8-a64fx
        ^asio@1.21.0%gcc@12.2.0~boost_coroutine~boost_regex~separate_compilation build_system=autotools cxxstd=17 arch=linux-rhel8-a64fx
        ^fujitsu-mpi@head%gcc@12.2.0 build_system=generic arch=linux-rhel8-a64fx
        ^git@2.39.1%gcc@12.2.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-rhel8-a64fx
        ^hwloc@2.2.0%gcc@12.2.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm build_system=autotools libs=shared,static arch=linux-rhel8-a64fx
        ^jemalloc@5.2.1%gcc@12.2.0~debug~documentation+fill~prof~stats build_system=autotools jemalloc_prefix=none libs=shared,static arch=linux-rhel8-a64fx
        ^ninja@1.11.1%gcc@12.2.0 build_system=generic arch=linux-rhel8-a64fx
        ^python@3.10.8%fj@4.10.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib build_system=generic patches=0aba3bf,0d98e93,7d40923,f2fd060 arch=linux-rhel8-a64fx
    ^hpx-kokkos@0.4.0%gcc@12.2.0~cuda~ipo~rocm~sycl build_system=cmake build_type=RelWithDebInfo cxxstd=17 future_type=polling arch=linux-rhel8-a64fx
    ^kokkos@develop%gcc@12.2.0+aggressive_vectorization~compiler_warnings~cuda~cuda_constexpr~cuda_lambda~cuda_ldg_intrinsic~cuda_relocatable_device_code~cuda_uvm~debug~debug_bounds_check~debug_dualview_modify_check~deprecated_code~examples~explicit_instantiation+hpx+hpx_async_dispatch~hwloc~ipo~memkind~numactl~openmp~openmptarget~pic+profiling~profiling_load_print~pthread~qthread~rocm+serial+shared~sycl~tests~tuning~wrapper build_system=cmake build_type=RelWithDebInfo intel_gpu_arch=none std=17 arch=linux-rhel8-a64fx
    ^silo@4.10.2%gcc@12.2.0+fortran+fpzip+hdf5+hzip~mpi+pic+shared~silex build_system=autotools patches=3a1e831,7b5a1dc,eb2a3a0,fa050e0 arch=linux-rhel8-a64fx
        ^autoconf@2.69%gcc@12.2.0 build_system=autotools patches=7793209 arch=linux-rhel8-a64fx
        ^autoconf-archive@2022.02.11%gcc@12.2.0 build_system=autotools patches=139214f arch=linux-rhel8-a64fx
        ^automake@1.16.1%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
        ^gnuconfig@2021-08-14%gcc@12.2.0 build_system=generic arch=linux-rhel8-a64fx
        ^libtool@2.4.6%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
        ^m4@1.4.18%gcc@12.2.0+sigsegv build_system=autotools patches=3877ab5,fc9b616 arch=linux-rhel8-a64fx
        ^readline@7.0%gcc@12.2.0 build_system=autotools arch=linux-rhel8-a64fx
    ^vc@1.4.1%gcc@12.2.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-rhel8-a64fx
        ^virtest@master%gcc@12.2.0~ipo build_system=cmake build_type=RelWithDebInfo arch=linux-rhel8-a64fx
