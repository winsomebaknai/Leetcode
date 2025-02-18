'''
Problem:-
Bob has a playlist of n songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob

Input Format 

The first line contains an integer N, denoting the number of songs in Bob's playlist.

The following input contains N integers, ith  integer denoting the singer of the ith  song.

Output Format

Output a single integer, the number of favourite singers of Bob

Sample Input
5
1 1 2 2 4
Sample Output
2


-----------------------------------------------------------------------

python code Traditional way
'''

def count_favorite_singers():
    n = int(input())
    singers = list(map(int, input().split()))
    
    frequency = {}
    for singer in singers:
        if singer in frequency:
            frequency[singer] += 1
        else:
            frequency[singer] = 1
    
    max_frequency = 0
    for count in frequency.values():
        if count > max_frequency:
            max_frequency = count
    
    fav_singer = 0
    for count in frequency.values():
        if count == max_frequency:
            fav_singer += 1
    
    return fav_singer

result = count_favorite_singers()
print(result)


#with python functions

def count_favorite_singers(singers):
    # Step 1: Count the frequency of each singer
    frequency = {}
    for singer in singers:
        if singer in frequency:
            frequency[singer] += 1
        else:
            frequency[singer] = 1

    # Step 2: Find the maximum frequency
    max_frequency = max(frequency.values())

    # Step 3: Count how many singers have the maximum frequency
    fav_singer = sum(1 for count in frequency.values() if count == max_frequency)

    # Return the result
    return fav_singer

# Input handling
n = int(input())  # Number of songs
singers = list(map(int, input().split()))  # List of singers

# Call the function and print the result
result = count_favorite_singers(singers)
print(result)