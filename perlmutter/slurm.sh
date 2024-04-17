#!/bin/bash
#SBTACH --ntasks-per-node=4
#SBTACH --cpus-per-task=32
#SBTACH --gpus-per-task=1
#SBTACH --constraint="gpu&hbm40g"

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
  export LCI_ENABLE_PRG_NET_ENDPOINT=0
  extra_args="--hpx:ini=hpx.parcel.lci.progress_type=worker --hpx:ini=hpx.parcel.lci.ndevices=2"
fi
export PMI_MAX_KVS_ENTRIES=4096

cd path/to/octotiger/q07_l${level}/close_to_merger || exit 1

srun -l octotiger --disable_output=on --amr_boundary_kernel_type=AMR_OPTIMIZED \
  --optimize_local_communication=1 --print_times_per_timestep=1 --config_file=dwd.ini \
  --number_gpus=1 --executors_per_gpu=128 --monopole_host_kernel_type=DEVICE_ONLY \
  --multipole_host_kernel_type=DEVICE_ONLY --hydro_host_kernel_type=DEVICE_ONLY \
  --monopole_device_kernel_type=KOKKOS_CUDA --multipole_device_kernel_type=KOKKOS_CUDA \
  --hydro_device_kernel_type=KOKKOS_CUDA --max_kernels_fused=4 --stop_step=25 \
  --hpx:ini=hpx.stacks.use_guard_pages=0 --hpx:ini=hpx.parcel.${pp}.priority=1000 \
  --hpx:threads=16 --hpx:ini=hpx.parcel.zero_copy_optimization=0 \
  ${extra_args}
