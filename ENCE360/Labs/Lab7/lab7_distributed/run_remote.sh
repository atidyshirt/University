#!/bin/bash


export N=2

if [[ $2 ]]; then
  export N=$2
fi

mpirun -n $N -hostfile remote_hosts --mca btl_tcp_if_exclude lo,vmnet8,virbr0 $1  $3
