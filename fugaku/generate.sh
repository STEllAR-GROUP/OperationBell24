#!/bin/bash

NAME=l10-beg
PARCEL_PORT=mpi

for NODE in 4096
do

TIME=00:59:00
QUEUE=large


cat << EOF > level_${NODE}.sbatch
#!/bin/bash
#PJM -L node=${NODE}
#PJM --mpi shape=${NODE} 
#PJM -L rscgrp=${QUEUE}
#PJM -L elapse=${TIME}
#PJM -g ra010008
#PJM -x PJM_LLIO_GFSCACHE=/vol0004
#PJM -S # Direction of output statistic information file (-s or -S)


. /vol0004/ra010008/data/u10393/spackfugaku/share/spack/setup-env.sh
spack load /t7wrrvkwyrmqbrsafzoef27eictsyje6 # April update hpx 1.9.1
spack spec /t7wrrvkwyrmqbrsafzoef27eictsyje6 
which octotiger

date

mpiexec -stdout-proc ./${PARCEL_PORT}-${NODE}.%j/%m/%/500r/stdout -stderr-proc ./${PARCEL_PORT}-${NODE}.%j/%m/%/500r/stderr  octotiger  --hpx:print-bind --config_file dwd.ini --multipole_host_kernel_type=KOKKOS  --monopole_host_kernel_type=KOKKOS --hydro_host_kernel_type=KOKKOS --hpx:ini=hpx.parcel.mpi.multithreaded!=0 --hpx:ini=hpx.stacks.use_guard_pages=0 --hpx:ini=hpx.parcel.bootstrap=mpi --hpx:ini=hpx.parcel.mpi.enable=1 --hpx:ini=hpx.parcel.mpi.zero_copy_optimization=0 --print_times_per_timestep=1

date

EOF


done

