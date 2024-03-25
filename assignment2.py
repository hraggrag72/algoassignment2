# Hrag Ayntabli
# 100894158
# Algorithms and Data Structures
# Assignment 2

import pygame
import time

# Initialize pygame mixer for sound effects
pygame.mixer.init()
swap_sound = pygame.mixer.Sound("swap_noise.mp3")

def play_swap_sound(played):
    if not played:
        swap_sound.play()
        return True
    return played

def merge_sort_visual(arr, depth=0, max_depth=0, prefix='', side='root'):
    padding = ' ' * ((max_depth - depth) * 2)  # Adjust spacing
    if len(arr) > 1:
        if depth == 0:  # For the root call, adjust the mid to prefer an even left split
            mid = len(arr) // 2 - 1 if len(arr) % 2 == 0 else len(arr) // 2
        else:
            mid = len(arr) // 2
        
        left_half = arr[:mid]
        right_half = arr[mid:]

        if depth == 0:
            # Only before printing for root
            time.sleep(1)
            print(f"{arr} -> Splitting at root into: {left_half}    |    {right_half}")
        else:
            # Delay before printing splits at other depths
            time.sleep(1)
            print(f"{prefix}{padding}{left_half}    |    {right_half}")

        # Working on left side
        time.sleep(1)
        print(f"{prefix}{padding}--> Working on left side: {left_half}")
        left_sorted = merge_sort_visual(left_half, depth + 1, max_depth, prefix + padding, 'left')
        
        # Working on right side
        time.sleep(1)
        print(f"{prefix}{padding}--> Working on right side: {right_half}")
        right_sorted = merge_sort_visual(right_half, depth + 1, max_depth, prefix + padding, 'right')

        # Merging process with sound control
        merged, sound_played = merge(left_sorted, right_sorted)
        time.sleep(1)
        print(f"{prefix}{padding}{merged} <- Merging on {side} side")
        
        # Side completion message
        if depth > 0:
            print(f"{prefix}{padding}<-- {side.capitalize()} side complete")
        else:
            print(f"{prefix}<-- Root sorting complete")

        return merged
    else:
        # Base case: if the array is a single element, it's already sorted
        return arr

def merge(left, right):
    result = []
    i = j = 0
    sound_played = False

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            sound_played = play_swap_sound(sound_played)  # Play swap sound effect once per merge

    # Append any remaining elements to the result
    result.extend(left[i:])
    result.extend(right[j:])

    return result, sound_played

def calculate_max_depth(n):
    depth = 0
    while n > 1:
        n = n // 2
        depth += 1
    return depth

# Main
if __name__ == "__main__":
    input_array = input("Enter the elements of the array separated by space: ")
    arr = list(map(int, input_array.strip().split()))
    max_depth = calculate_max_depth(len(arr))
    print("Original array:")
    print(arr)
    sorted_arr = merge_sort_visual(arr, 0, max_depth)
    print("Sorted array:")
    print(sorted_arr)
