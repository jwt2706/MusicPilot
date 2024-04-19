import essentia.standard as es
from sklearn.cluster import KMeans
import os, json

def convert_range_to_numerical(range_str):
    if range_str == "Variable":
        return [-float('inf'), float('inf')]
    elif "-" in range_str:
        return [float(x) for x in range_str.split("-")]
    else:
        return [float(range_str), float(range_str)]

def analyze_audio_files(file_paths):
    analyzed_files = []

    # Define a mapping from musical keys to integers
    key_to_int = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 
        'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }

    for file_path in file_paths:
        loader = es.MonoLoader(filename=file_path)
        audio = loader()

        # Calculate various audio features using Essentia
        rhythm_extractor = es.RhythmExtractor2013()
        bpm, beats, beats_confidence, _, _ = rhythm_extractor(audio)
        key, scale, key_confidence = es.KeyExtractor()(audio)
        loudness = es.Loudness()(audio)
        spectral_centroid = es.SpectralCentroidTime()(audio)
        zero_crossing_rate = es.ZeroCrossingRate()(audio)

        # Convert the key to an integer
        key = key_to_int[key]

        # Store the analyzed information in a dictionary
        analyzed_file = {
            'file_path': file_path,
            'bpm': bpm,
            'beats_confidence': beats_confidence,
            'key': key,  # the key is now an integer
            'key_confidence': key_confidence,
            'loudness': loudness,
            'spectral_centroid': spectral_centroid,
            'zero_crossing_rate': zero_crossing_rate
        }

        analyzed_files.append(analyzed_file)

    return analyzed_files

def generate_playlists(analyzed_files, moods):
    if len(analyzed_files) < len(moods):
        print(f"Warning: Not enough songs to create playlists for all moods. Only creating playlists for the first {len(analyzed_files)} moods.")
        moods = moods[:len(analyzed_files)]

    # Extract the features from the analyzed files
    features = [list(file.values())[1:] for file in analyzed_files]

    # Use K-means clustering to group similar songs together
    kmeans = KMeans(n_clusters=len(moods))
    kmeans.fit(features)

    # Create playlists from the clusters of similar songs
    playlists = {mood["name"]: [] for mood in moods}
    unused_tracks = set(file['file_path'] for file in analyzed_files)
    for i, label in enumerate(kmeans.labels_):
        for mood in moods:
            criteria = {k: convert_range_to_numerical(v) for k, v in mood.items() if k != "name"}
            if all(criteria.get(feature, [-float('inf'), float('inf')])[0] <= analyzed_files[i][feature] <= criteria.get(feature, [-float('inf'), float('inf')])[1] for feature in analyzed_files[i] if feature != 'file_path'):
                playlists[mood["name"]].append(analyzed_files[i]['file_path'])
                unused_tracks.remove(analyzed_files[i]['file_path'])

    # Only keep playlists with at least 10 songs
    playlists = {theme: songs for theme, songs in playlists.items() if len(songs) >= 10}

    return playlists, list(unused_tracks)

def main():
    # Load moods from JSON file
    with open('moods.json', 'r') as f:
        moods = json.load(f)["moods"]

    # Directory containing the audio files to analyze
    directory = 'test'

    # Get a list of all audio file paths in the directory
    file_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp3')]

    # Analyze the audio files
    print('Analyzing audio files...')
    analyzed_files = analyze_audio_files(file_paths)

    # Generate playlists
    print('Generating playlists...')
    playlists, unused_tracks = generate_playlists(analyzed_files, moods)

    # Print out the playlists
    for theme, playlist in playlists.items():
        print(f'{theme} Playlist:')
        for file_path in playlist:
            print(f'  {file_path}')

    # Print out the unused tracks
    print('Unused Tracks:')
    for file_path in unused_tracks:
        print(f'  {file_path}')

if __name__ == '__main__':
    main()