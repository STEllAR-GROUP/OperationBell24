#!/bin/bash
#SBTACH --ntasks-per-node=1
#SBTACH --cpus-per-task=48

# Users need to use `sbatch` to submit this script to SLURM, specifying the desired node count.

pp=${1:-lci}
level=${2:-11}

extra_args=""
if [[ "$pp" == "lci" ]]; then
  export LCI_SERVER_MAX_SENDS=64
  export LCI_SERVER_MAX_RECVS=4096
  export LCI_SERVER_NUM_PKTS=65536
  export LCI_SERVER_MAX_CQES=65536
  export LCI_PACKET_SIZE=12288
  export LCI_USE_DREG=0
  extra_args="--hpx:ini=hpx.parcel.lci.progress_type=worker --hpx:ini=hpx.parcel.lci.ndevices=2"
fi

cd path/to/octotiger/q07_l${level}/close_to_merger || exit 1

srun -l octotiger --disable_output=on --amr_boundary_kernel_type=AMR_OPTIMIZED \
  --optimize_local_communication=1 --print_times_per_timestep=1 --config_file=dwd.ini \
  --monopole_host_kernel_type=KOKKOS --multipole_host_kernel_type=KOKKOS \
  --hydro_host_kernel_type=KOKKOS --monopole_device_kernel_type=OFF \
  --multipole_device_kernel_type=OFF --hydro_device_kernel_type=OFF \
  --stop_step=10 --hpx:ini=hpx.stacks.use_guard_pages=0 \
  --hpx:ini=hpx.parcel.${pp}.priority=1000 \
  --hpx:threads=48 --hpx:ini=hpx.parcel.zero_copy_optimization=0 \
  ${extra_args}
