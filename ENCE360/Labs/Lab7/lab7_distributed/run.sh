#!/bin/bash


export N=2

if [[ $2 ]]; then
  export N=$2
fi

mpirun -n $N -hostfile hosts --mca btl_tcp_if_exclude lo,vmnet8 $1 $3
