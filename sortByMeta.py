import os
from tinytag import TinyTag

def get_metadata(file_path):
    # Use TinyTag to get the metadata of the audio file
    tag = TinyTag.get(file_path)

    # Return a dictionary with the song's metadata
    return {'genre': tag.genre}

def sort_songs_by_genre(directory):
    # Get a list of all audio file paths in the directory
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp3')]

    # Create a dictionary to store the songs by genre
    songs_by_genre = {}

    # Create a list to store the songs with unknown genre
    unknown_genre_songs = []

    # Sort the songs into lists by genre
    for file_path in file_paths:
        metadata = get_metadata(file_path)
        genre = metadata.get('genre')
        if genre:
            if genre not in songs_by_genre:
                songs_by_genre[genre] = []
            songs_by_genre[genre].append(file_path)
        else:
            unknown_genre_songs.append(file_path)

    return songs_by_genre, unknown_genre_songs

def main():
    # Directory containing the audio files to analyze
    directory = 'test'

    # Sort the songs by genre
    songs_by_genre, unknown_genre_songs = sort_songs_by_genre(directory)

    # Print out the songs by genre
    for genre, songs in songs_by_genre.items():
        print(f'{genre} Songs:')
        for song in songs:
            print(f'  {song}')

    # Print out the songs with unknown genre
    print('Unknown Genre Songs:')
    for song in unknown_genre_songs:
        print(f'  {song}')

if __name__ == '__main__':
    main()