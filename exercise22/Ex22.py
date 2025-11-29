from mpi4py import MPI
import numpy as np
import time

# MPI initialization

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


N = 5000

start_time = time.time()


# Handle uneven division of rows when N % size != 0

rows_per_proc = N // size
remainder = N % size

if rank < remainder:
    # First 'remainder' processes get 1 extra row
    local_start = rank * (rows_per_proc + 1)
    local_end = local_start + (rows_per_proc + 1)
else:
    # Remaining processes only get rows_per_proc rows
    local_start = remainder * (rows_per_proc + 1) + (rank - remainder) * rows_per_proc
    local_end = local_start + rows_per_proc

local_rows = local_end - local_start   # number of rows assigned to this process


# local row block of the tri-diagonal matrix

localA = np.zeros((local_rows, N))

for i_local in range(local_rows):
    i_global = local_start + i_local

    for j in range(N):
        if i_global == j:
            localA[i_local, j] = 2.0
        elif i_global == j + 1 or i_global == j - 1:
            localA[i_local, j] = -1.0


# Vector x

x = np.ones(N)


# Local matrix-vector multiplication

localy = localA @ x


# Root gathers all local results

if rank == 0:
    # Allocate global result vector
    y = np.zeros(N)

    # Copy local part from root
    y[local_start:local_end] = localy

    # Receive from all other processes
    for p in range(1, size):

        # Determine row range for process p
        if p < remainder:
            p_rows = rows_per_proc + 1
            p_start = p * (rows_per_proc + 1)
            p_end = p_start + p_rows
        else:
            p_rows = rows_per_proc
            p_start = remainder * (rows_per_proc + 1) + (p - remainder) * rows_per_proc
            p_end = p_start + p_rows

        # Allocate receiving buffer
        recv_buffer = np.zeros(p_rows)

        # Receive message
        comm.Recv(recv_buffer, source=p)

        # Place into global vector
        y[p_start:p_end] = recv_buffer

    # Print result (root only)
    print(f"Norm of y: {np.linalg.norm(y)}")

else:
    # Non-root processes send their partial result
    comm.Send(localy, dest=0)


# End timing

end_time = time.time()
print(f"Rank {rank}: Time taken = {end_time - start_time:.6f} seconds for N={N} with {size} processes")
