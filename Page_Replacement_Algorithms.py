# %%

from random import randint

# %%

number_of_pages = 10
reference_string = [randint(1, 5) for n in range(0, number_of_pages)]
TOTAL_FRAMES = 3

# %%
print("Reference String: ", end="")
print(reference_string, end="\n")


# %%
def optimal(total_frames, reference_string):
    # Number of frames in the working set
    frames_to_use = total_frames

    # Array of frames to be dynamically interchanged
    optimal_frames = []
    # The number of optimal page faults
    optimal_faults = 0
    # The number of pages swapped into the page frame
    pages_in_memory = 0

    # Parse through the Frames
    for frame in range(frames_to_use):
        optimal_frames.append(-1)

    # Parse through the reference string
    for page in range(len(reference_string)):

        # Flag for if the page is in the frame
        in_optimal_memory = False

        # Parse through the frames in the FIFO_frames
        for frame in range(frames_to_use):
            if (
                optimal_frames[frame] == reference_string[page]
            ):  # Hit because the page is in the frame already
                in_optimal_memory = True

                print(f"\n{reference_string[page]:d} ->", end=" ")
                for frame in range(frames_to_use):
                    if optimal_frames[frame] != -1:
                        print("[", optimal_frames[frame], "]", end=" ")
                    else:
                        print("[ - ]", end=" ")
                print(" Hit", end="")
                break

        if not in_optimal_memory:
            if (
                pages_in_memory >= frames_to_use
            ):  # Page fault, there's no space in frame and reference page needs to
                # be swapped in.

                # Field to hold the index for furthest away
                furthest_in_reference_string = 0
                # Field for page that is going to be removed.
                page_to_remove = 0

                # Parse through the working set
                for frame in range(
                    len(optimal_frames)
                ):  # Loop through items currently in FIFO_frames
                    is_page_used_in_short_time = False

                    # Look at future page request in reference string
                    for future_page in range(
                        page, len(reference_string)
                    ):  # If the current page in set matches a future page
                        if optimal_frames[frame] == reference_string[future_page]:
                            # Set the flag for page is used to true
                            is_page_used_in_short_time = True
                            # Check if this is the furthest future reference away
                            if future_page > furthest_in_reference_string:
                                # (swap if it is)
                                furthest_in_reference_string = future_page
                                page_to_remove = frame
                                break
                    # If the page isn't found in future FIFO_frames at all
                    if not is_page_used_in_short_time:
                        page_to_remove = frame
                        break
                #  remove the frame
                optimal_frames[page_to_remove] = reference_string[page]

                print(f"\n{reference_string[page]:d} ->", end=" ")
                for frame in range(frames_to_use):
                    if optimal_frames[page_to_remove] != -1:
                        print("[", optimal_frames[page_to_remove], "]", end=" ")
                    else:
                        print("[ - ]", end=" ")
                print(" Miss", end="")

            # Set of frames aren't full yet
            else:
                optimal_frames[pages_in_memory] = reference_string[page]
                pages_in_memory += 1
                print(f"\n{reference_string[page]:d} ->", end=" ")
                for frame in range(frames_to_use):
                    if optimal_frames[frame] != -1:
                        print("[", optimal_frames[frame], "]", end=" ")
                    else:
                        print("[ - ]", end=" ")
                print(" Miss", end="")
            optimal_faults += 1
    return optimal_faults


# %%
def least_recently_used(total_frames, reference_string):
    # The amount of frames in the working set
    frames_to_use = total_frames

    # The number of pages that have been put into FIFO_frames (starts at 0)
    pages_in_memory = 0

    # The number of faults for the LRU algorithm
    LRU_faults = 0

    # The LRU FIFO_frames frames
    LRU_frames = []

    # Initialize the set of frames that are dynamically changed.
    for frames in range(frames_to_use):
        LRU_frames.append(-1)

    # Parse through the reference string
    for page in range(len(reference_string)):
        # Flag for if the page is in the FIFO_frames
        in_LRU_memory = False

        # Parse through the frame (MM)
        for frame in range(frames_to_use):
            # If the page is found in the FIFO_frames..
            if LRU_frames[frame] == reference_string[page]:
                in_LRU_memory = True  # Set the in FIFO_frames flag to TRUE
                break

        #  If the page was not found in the MM frame,
        #  NEED TO SWAP OUT LRU, SWAP IN RF PAGE
        if in_LRU_memory is False:
            # If the page frame is full
            if LRU_frames[pages_in_memory] is not -1:
                # Farthest possible swap to look at
                oldest_page = 999
                # Parse through the pages swapped in previously
                for past_swap in range(frames_to_use):
                    # Found in the page frame set to False
                    in_LRU_memory = False
                    # Go backwards from the current page to the first page in the
                    # reference string
                    frame = page
                    # Go backwards through swapped pages until the first page is reached
                    while frame >= 0:
                        frame -= 1
                        # If the previously swapped page was previously in the reference
                        # string
                        if LRU_frames[past_swap] == reference_string[frame]:
                            in_LRU_memory = True
                            break
                    # If it's in the working set and less than the oldest page
                    if in_LRU_memory is True and frame < oldest_page:
                        # This page in the frame becomes the new oldest_page
                        oldest_page = frame
                        # Prepare to swap oldest page for
                        pages_in_memory = past_swap

            # When the Frame is -1... set the frame equal to the reference page
            LRU_frames[pages_in_memory] = reference_string[page]
            # Recalculate the number of pages in working set (0, 1, 2,... n-1)
            pages_in_memory = (pages_in_memory + 1) % frames_to_use
            # Record the page fault
            LRU_faults += 1
            # Print
            print(f"\n{reference_string[page]:d} ->", end=" ")
            for frame in range(frames_to_use):
                if LRU_frames[frame] != -1:
                    print("[", LRU_frames[frame], "]", end=" ")
                else:
                    print("[ - ]", end=" ")
            print(" Miss", end="")
        else:
            print(f"\n{reference_string[page]:d} ->", end=" ")
            for frame in range(frames_to_use):
                if LRU_frames[frame] != -1:
                    print("[", LRU_frames[frame], "]", end=" ")
                else:
                    print("[ - ]", end=" ")
            print(" Hit", end="")
    return LRU_faults
# %%


def first_in_first_out(total_frames, reference_string):

    frames_to_use = total_frames

    # Set of pages to be dynamically swapped out with MM
    FIFO_frames = []
    # Number of page faults for the FIFO algorithm
    FIFO_faults = 0
    pages_in_memory = 0

    # index for the page that is replaced
    first_page_in = -1

    for frame in range(total_frames):
        FIFO_frames.append(-1)

    for page in range(len(reference_string)):
        # Flag for if the page is in the working set
        in_memory = False

        # Parse through the frames
        for frame in range(total_frames):
            # No page fault, reference page is found in the memory
            if FIFO_frames[frame] == reference_string[page]:
                print(f"\n{reference_string[page]:d} ->", end=" ")
                for frame in range(frames_to_use):
                    if FIFO_frames[frame] != -1:
                        print("[", FIFO_frames[frame], "]", end=" ")
                    else:
                        print("[ - ]", end=" ")
                print(" Hit", end="")
                in_memory = True
                break
            # Page fault, the requested page isn't in page frame
        if not in_memory:
            first_page_in = (first_page_in + 1) % total_frames  # Ensure the first_page_in doesn't run past
            # total_frames of FIFO_frames
            FIFO_frames[first_page_in] = reference_string[page]

            print(f"\n{reference_string[page]:d} ->", end=" ")
            for frame in range(frames_to_use):
                if FIFO_frames[frame] != -1:
                    print("[", FIFO_frames[frame], "]", end=" ")
                else:
                    print("[ - ]", end=" ")
            print(" Miss", end="")

            # if pages_in_memory>=total_frames: # A fault since there is no space and it is in FIFO_frames (a miss)
            FIFO_faults += 1
            pages_in_memory += 1
    return FIFO_faults


# %%
print("\n\t\tOptimal Page Replacement Algorithm: ")
optimal_algo_faults = optimal(TOTAL_FRAMES, reference_string)

# %%
print("\n\n\t\tLeast Recently Used Page Replacement Algorithm: ")
lru_algo_faults = least_recently_used(TOTAL_FRAMES, reference_string)

# %%
print("\n\n\t\t\tTotal Optimal Page Faults : %d." % optimal_algo_faults, end="")
print("\n\t\t\tTotal Least Recently Used Faults : %d." % lru_algo_faults)

# %%
if (optimal_algo_faults == lru_algo_faults):
    print("\n\nIt was a tie! The Optimal and Least Recently Used Page Replacement Algorithms Were Equal")
    print("The Tie Breaker will be settled with the First In First Out algorithm")

    print("\n\n\t\tFirst In First Out Page Replacement Algorithm: ")
    fifo_algo_faults = first_in_first_out(TOTAL_FRAMES, reference_string)

    print("\n\n\t\t\tTotal First in First Out Page Faults : %d." % lru_algo_faults)

    if (fifo_algo_faults < lru_algo_faults):
        print("\n\n\t\tFirst In First Out Lost to LRU and Optimal")
    else:
        print("\n\n\t\tFirst In First Out was less than LRU and Optimal Page Replacement")
else:
    print("\n\n\t\tOptimal Page Replacement Algorithm was the most efficient. ")

# # %%
# # print("\n\n\t\tFirst In First Out Page Replacement Algorithm: ")
# # fifo_algo_faults = first_in_first_out(TOTAL_FRAMES, reference_string)
#
# # %%
# print("\n\n\t\t\tTotal Optimal Page Faults : %d." % optimal_algo_faults, end="")
# print("\n\t\t\tTotal Least Recently Used Faults : %d." % lru_algo_faults)
# # print("\n\t\t\tTotal First in First Out Page Faults : %d." % lru_algo_faults)
