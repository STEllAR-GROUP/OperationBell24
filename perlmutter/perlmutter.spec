octotiger@master%gcc@12.3.0 cppflags="-L/opt/cray/pe/mpich/8.1.28/gtl/lib -lmpi_gtl_cuda" +cuda~fast_fp_contract~ipo+kokkos~kokkos_hpx_kernels~rocm~sycl build_system=cmake build_type=Release cuda_arch=80 dev_path=/global/homes/j/jackyan/workspace/octotiger generator=make griddim=8 hydro_host_tasks=1 monopole_host_tasks=1 multipole_host_tasks=1 simd_extension=DISCOVER simd_library=KOKKOS theta_minimum=0.34 arch=linux-sles15-zen3
    ^boost@1.82.0%gcc@12.3.0+atomic+chrono~clanglibcpp~container~context~contract~coroutine+date_time~debug+exception~fiber+filesystem+graph~graph_parallel~icu+iostreams~json+locale+log+math~mpi+multithreaded~nowide~numpy~pic+program_options~python+random+regex+serialization+shared+signals~singlethreaded~stacktrace+system~taggedlayout+test+thread+timer~type_erasure~versionedlayout+wave build_system=generic cxxstd=17 patches=a440f96,a7c807f visibility=hidden arch=linux-sles15-zen3
        ^bzip2@1.0.8%gcc@12.3.0~debug~pic+shared build_system=generic arch=linux-sles15-zen3
            ^diffutils@3.6%gcc@12.3.0 build_system=autotools arch=linux-sles15-zen3
        ^xz@5.4.1%gcc@12.3.0~pic build_system=autotools libs=shared,static arch=linux-sles15-zen3
        ^zlib@1.2.13%gcc@12.3.0+optimize+pic+shared build_system=makefile arch=linux-sles15-zen3
        ^zstd@1.5.5%gcc@12.3.0~programs build_system=makefile libs=shared,static arch=linux-sles15-zen3
    ^cmake@3.22.0%gcc@12.3.0~doc+ncurses+ownlibs~qt build_system=generic build_type=Release arch=linux-sles15-zen3
    ^cppuddle@git.d013eb94f83d515aec3f614620d5a9ee721b73b9=0.3.1-git.41%gcc@12.3.0~allocator_counters+buffer_content_recycling+buffer_recycling~enable_gpu_tests+executor_recycling+hpx~ipo build_system=cmake build_type=Release generator=make max_number_gpus=4 number_buffer_buckets=128 arch=linux-sles15-zen3
    ^cuda@12.2%gcc@12.3.0~allow-unsupported-compilers~dev build_system=generic arch=linux-sles15-zen3
    ^gmake@4.2.1%gcc@12.3.0~guile build_system=autotools patches=ca60bd9,fe5b60d arch=linux-sles15-zen3
    ^hdf5@1.14.1-2%gcc@12.3.0~cxx~fortran+hl~ipo~java~map~mpi+shared+szip+threadsafe+tools api=default build_system=cmake build_type=Release generator=make arch=linux-sles15-zen3
        ^libaec@1.0.6%gcc@12.3.0~ipo+shared build_system=cmake build_type=Release generator=make arch=linux-sles15-zen3
        ^pkgconf@1.9.5%gcc@12.3.0 build_system=autotools arch=linux-sles15-zen3
    ^hpx@git.310f449f3fd4ccf6cb6d0a59e3d7a5edcf27fd4a=stable-git.108%gcc@12.3.0+async_cuda+async_gpu_futures~async_mpi+cuda~examples~generic_coroutines~ipo~lci_pp_log~lci_pp_pcounter~rocm~sycl~tools build_system=cmake build_type=Release cuda_arch=80 cxxstd=17 generator=ninja instrumentation=none malloc=tcmalloc max_cpu_count=256 networking=lci,mpi sycl_target_arch=none arch=linux-sles15-zen3
        ^asio@1.21.0%gcc@12.3.0~boost_coroutine~boost_regex~separate_compilation build_system=autotools cxxstd=17 arch=linux-sles15-zen3
        ^cray-mpich@8.1.28%gcc@12.3.0+wrappers build_system=generic arch=linux-sles15-zen3
        ^git@2.35.3%gcc@12.3.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-sles15-zen3
        ^gperftools@2.10%gcc@12.3.0+debugalloc~dynamic_sized_delete_support+libunwind~sized_delete build_system=autotools arch=linux-sles15-zen3
            ^libunwind@1.6.2%gcc@12.3.0~block_signals~conservative_checks~cxx_exceptions~debug~debug_frame+docs~pic+tests+weak_backtrace~xz~zlib build_system=autotools components=none libs=shared,static arch=linux-sles15-zen3
        ^hwloc@2.8.0%gcc@12.3.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm build_system=autotools libs=shared,static arch=linux-sles15-zen3
        ^lci@git.6dcb6a8508f498bf65661e8a10497f1e7c84c18a=1.7.6-git.45%gcc@12.3.0+aligned+benchmarks~debug~debug-slow~docs+examples~gprof+ibv-td~inline-cq~ipo+multithread-progress+native+papi~pcounter+shared+tests+vector build_system=cmake build_type=Release cache-line=auto completion=am,cq,sync default-dreg=auto default-max-cqe=auto default-max-recvs=auto default-max-sends=auto default-packet-size=auto default-packets=auto default-pm=cray enable-pmix=auto fabric=ofi generator=ninja arch=linux-sles15-zen3
            ^cray-pmi@6.1.13%gcc@12.3.0 build_system=generic arch=linux-sles15-zen3
            ^libfabric@1.15.2%gcc@12.3.0~debug~kdreg build_system=autotools fabrics=cxi,sockets,tcp,udp arch=linux-sles15-zen3
            ^papi@7.0.1.2%gcc@12.3.0~cuda+example~infiniband~lmsensors~nvml~powercap~rapl~rocm~rocm_smi~sde+shared~static_tools build_system=autotools arch=linux-sles15-zen3
        ^ninja@1.10.0%gcc@12.3.0+re2c build_system=generic arch=linux-sles15-zen3
        ^python@3.9.13%gcc@12.3.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl+tix+tkinter+uuid+zlib build_system=generic patches=0d98e93,f2fd060 arch=linux-sles15-zen3
    ^hpx-kokkos@0.4.0%gcc@12.3.0+cuda~ipo~rocm~sycl build_system=cmake build_type=Release cuda_arch=80 cxxstd=17 future_type=polling generator=make arch=linux-sles15-zen3
    ^kokkos@4.0.01%gcc@12.3.0+aggressive_vectorization~compiler_warnings+cuda+cuda_constexpr+cuda_lambda~cuda_ldg_intrinsic~cuda_relocatable_device_code~cuda_uvm~debug~debug_bounds_check~debug_dualview_modify_check~deprecated_code~examples+hpx+hpx_async_dispatch~hwloc~ipo~memkind~numactl~openmp~openmptarget~pic~rocm+serial+shared~sycl~tests~threads~tuning+wrapper build_system=cmake build_type=Release cuda_arch=80 generator=make intel_gpu_arch=none patches=5e61580,b26a011 std=17 use_unsupported_sycl_arch=none arch=linux-sles15-zen3
        ^kokkos-nvcc-wrapper@4.0.01%gcc@12.3.0 build_system=generic arch=linux-sles15-zen3
    ^silo@4.11%gcc@12.3.0+fortran+fpzip+hdf5+hzip~mpi+pic+shared~silex build_system=autotools patches=451c4c5,a081263,eb2a3a0,fa050e0 arch=linux-sles15-zen3
        ^autoconf@2.69%gcc@12.3.0 build_system=autotools patches=7793209 arch=linux-sles15-zen3
        ^autoconf-archive@2023.02.20%gcc@12.3.0 build_system=autotools arch=linux-sles15-zen3
        ^automake@1.15.1%gcc@12.3.0 build_system=autotools arch=linux-sles15-zen3
        ^libtool@2.4.6%gcc@12.3.0 build_system=autotools arch=linux-sles15-zen3
        ^m4@1.4.18%gcc@12.3.0+sigsegv build_system=autotools patches=3877ab5,fc9b616 arch=linux-sles15-zen3
        ^readline@8.2%gcc@12.3.0 build_system=autotools patches=bbf97f1 arch=linux-sles15-zen3
            ^ncurses@6.4%gcc@12.3.0~symlinks+termlib abi=none build_system=autotools arch=linux-sles15-zen3
    ^vc@1.4.1%gcc@12.3.0~ipo build_system=cmake build_type=Release generator=make arch=linux-sles15-zen3