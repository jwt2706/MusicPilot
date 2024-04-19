import os
from tinytag import TinyTag

def get_metadata(file_path):
    tag = TinyTag.get(file_path)
    return {'genre': tag.genre}

def sort_songs_by_genre(directory):
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp3')]
    songs_by_genre = {}
    unknown_genre_songs = []

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
    directory = 'test'
    songs_by_genre, unknown_genre_songs = sort_songs_by_genre(directory)

    for genre, songs in songs_by_genre.items():
        print(f'{genre} Songs:')
        for song in songs:
            print(f'  {song}')

    print('Unknown Genre Songs:')
    for song in unknown_genre_songs:
        print(f'  {song}')

if __name__ == '__main__':
    main()