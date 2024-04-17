[+]  octotiger@git.bef65a2a702b850895f0940ffc2a568fe32d3e65=0.10.0-git.166%gcc@12.2.0~boost_multiprecision~cuda+cxx20~fast_fp_contract~ipo+kokkos+kokkos_hpx_kernels~rocm~sycl build_system=cmake build_type=Release generator=make griddim=8 hydro_host_tasks=1 monopole_host_tasks=1 multipole_host_tasks=16 simd_extension=SVE simd_library=STD theta_minimum=0.34 arch=linux-rocky8-a64fx
[e]      ^boost@1.83%gcc@12.2.0+atomic+chrono~clanglibcpp~container+context~contract~coroutine+date_time~debug+exception~fiber+filesystem+graph~graph_parallel~icu+iostreams~json+locale+log+math~mpi+multithreaded~nowide~numpy~pic+program_options~python+random+regex+serialization+shared+signals~singlethreaded~stacktrace+system~taggedlayout+test+thread+timer~type_erasure~versionedlayout+wave build_system=generic context-impl=fcontext cxxstd=17 patches=a440f96 visibility=hidden arch=linux-rocky8-a64fx
[e]      ^cmake@3.20.2%gcc@12.2.0~doc+ncurses+ownlibs build_system=generic build_type=Release arch=linux-rocky8-a64fx
[+]      ^cppuddle@git.d013eb94f83d515aec3f614620d5a9ee721b73b9=0.3.1-git.41%gcc@12.2.0+allocator_counters+buffer_content_recycling+buffer_recycling~enable_gpu_tests+executor_recycling+hpx~ipo build_system=cmake build_type=Release generator=make max_number_gpus=1 number_buffer_buckets=48 arch=linux-rocky8-a64fx
[e]      ^gmake@4.2.1%gcc@12.2.0~guile build_system=generic patches=ca60bd9,fe5b60d arch=linux-rocky8-a64fx
[+]      ^hdf5@1.14.3%gcc@12.2.0~cxx~fortran+hl~ipo~java~map~mpi+shared+szip+threadsafe+tools api=default build_system=cmake build_type=Release generator=make arch=linux-rocky8-a64fx
[+]          ^libaec@1.0.6%gcc@12.2.0~ipo+shared build_system=cmake build_type=Release generator=make arch=linux-rocky8-a64fx
[e]          ^pkgconf@1.4.2%gcc@12.2.0 build_system=autotools arch=linux-rocky8-a64fx
[+]          ^zlib-ng@2.1.4%gcc@12.2.0+compat+opt build_system=autotools arch=linux-rocky8-a64fx
[+]      ^hpx@git.40eef48f5b941f400164f79c2c2eefbeb35db49e=stable-git.71%gcc@12.2.0~async_cuda+async_gpu_futures~async_mpi~cuda~examples+generic_coroutines~ipo~lci_pp_log~lci_pp_pcounter~rocm~sycl~tests~tools build_system=cmake build_type=Release cxxstd=17 generator=ninja instrumentation=none malloc=mimalloc max_cpu_count=64 networking=lci,mpi sycl_target_arch=none arch=linux-rocky8-a64fx
[+]          ^asio@1.28.0%gcc@12.2.0~boost_coroutine~boost_regex~separate_compilation build_system=autotools cxxstd=17 arch=linux-rocky8-a64fx
[e]          ^git@2.39.3%gcc@12.2.0+man+nls+perl+subtree~svn~tcltk build_system=autotools arch=linux-rocky8-a64fx
[+]          ^hwloc@2.9.1%gcc@12.2.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm build_system=autotools libs=shared,static arch=linux-rocky8-a64fx
[+]              ^libpciaccess@0.17%gcc@12.2.0 build_system=autotools arch=linux-rocky8-a64fx
[+]                  ^util-macros@1.19.3%gcc@12.2.0 build_system=autotools arch=linux-rocky8-a64fx
[+]              ^libxml2@2.10.3%gcc@12.2.0+pic~python+shared build_system=autotools arch=linux-rocky8-a64fx
[+]                  ^libiconv@1.17%gcc@12.2.0 build_system=autotools libs=shared,static arch=linux-rocky8-a64fx
[+]                  ^xz@5.4.1%gcc@12.2.0~pic build_system=autotools libs=shared,static arch=linux-rocky8-a64fx
[+]              ^ncurses@6.4%gcc@12.2.0~symlinks+termlib abi=none build_system=autotools arch=linux-rocky8-a64fx
[+]          ^lci@git.6dcb6a8508f498bf65661e8a10497f1e7c84c18a=1.7.6-git.45%gcc@12.2.0+aligned+benchmarks~debug~debug-slow~docs+examples~gprof+ibv-td~inline-cq~ipo+multithread-progress+native~papi~pcounter+shared+tests~vector build_system=cmake build_type=Release cache-line=256 completion=am,cq,sync default-dreg=auto default-max-cqe=auto default-max-recvs=auto default-max-sends=auto default-packet-size=auto default-packets=auto default-pm=auto enable-pm=auto fabric=ibv generator=ninja arch=linux-rocky8-a64fx
[e]              ^rdma-core@40.0%gcc@12.2.0+static build_system=cmake build_type=Release generator=make arch=linux-rocky8-a64fx
[+]          ^mimalloc@2.1.2%gcc@12.2.0~build_tests~debug_full~ipo~local_dynamic_tls+override+padding~secure~see_asm~show_errors~skip_collect_on_exit~use_cxx~xmalloc build_system=cmake build_type=Release generator=make libs=object,shared,static arch=linux-rocky8-a64fx
[e]          ^ninja@1.8.2%gcc@12.2.0+re2c build_system=generic arch=linux-rocky8-a64fx
[e]          ^openmpi@4.1.5%gcc@12.2.0~atomics~cuda~cxx~cxx_exceptions~gpfs~internal-hwloc~internal-pmix~java~legacylaunchers+lustre~memchecker~openshmem~orterunprefix+pmi+romio+rsh~singularity~static+vt~wrapper-rpath build_system=autotools fabrics=ucx schedulers=slurm arch=linux-rocky8-a64fx
[e]          ^python@3.6.8%gcc@12.2.0+bz2+crypt+ctypes+dbm~debug+libxml2+lzma+nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tkinter+uuid+zlib build_system=generic patches=ebdca64 arch=linux-rocky8-a64fx
[+]      ^hpx-kokkos@0.4.0%gcc@12.2.0~cuda~ipo~rocm~sycl build_system=cmake build_type=Release cxxstd=17 future_type=polling generator=make arch=linux-rocky8-a64fx
[+]      ^kokkos@4.1.00%gcc@12.2.0+aggressive_vectorization~compiler_warnings~cuda~cuda_constexpr~cuda_lambda~cuda_ldg_intrinsic~cuda_relocatable_device_code~cuda_uvm~debug~debug_bounds_check~debug_dualview_modify_check~deprecated_code~examples+hpx+hpx_async_dispatch~hwloc~ipo~memkind~numactl~openmp~openmptarget~pic~rocm+serial+shared~sycl~tests~threads~tuning~wrapper build_system=cmake build_type=Release generator=make intel_gpu_arch=none patches=b26a011,b475d96 std=17 use_unsupported_sycl_arch=none arch=linux-rocky8-a64fx
[+]      ^silo@4.11%gcc@12.2.0+fortran+fpzip+hdf5+hzip+mpi+pic+shared~silex build_system=autotools patches=251244d,451c4c5,a081263,eb2a3a0,fa050e0 arch=linux-rocky8-a64fx
[e]          ^autoconf@2.69%gcc@12.2.0 build_system=autotools patches=7793209 arch=linux-rocky8-a64fx
[+]          ^autoconf-archive@2023.02.20%gcc@12.2.0 build_system=autotools arch=linux-rocky8-a64fx
[e]          ^automake@1.16.1%gcc@12.2.0 build_system=autotools arch=linux-rocky8-a64fx
[+]          ^gnuconfig@2022-09-17%gcc@12.2.0 build_system=generic arch=linux-rocky8-a64fx
[e]          ^libtool@2.4.6%gcc@12.2.0 build_system=autotools arch=linux-rocky8-a64fx
[e]          ^m4@1.4.18%gcc@12.2.0+sigsegv build_system=autotools patches=3877ab5,fc9b616 arch=linux-rocky8-a64fx
[e]          ^perl@5.26.3%gcc@12.2.0~cpanm+opcode+open+shared+threads build_system=generic patches=8cf4302 arch=linux-rocky8-a64fx
[+]          ^readline@8.2%gcc@12.2.0 build_system=autotools patches=bbf97f1 arch=linux-rocky8-a64fx
[+]      ^vc@1.4.1%gcc@12.2.0~ipo build_system=cmake build_type=Release generator=make arch=linux-rocky8-a64fx