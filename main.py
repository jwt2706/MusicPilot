import essentia
import essentia.standard as es
import os

def is_audio_file(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in ['.wav', '.mp3', '.aiff', '.aif', '.flac', '.ogg']

def analyze_audio_file(file_path):
    loader = es.MonoLoader(filename=file_path)
    audio = loader()

    # Calculate various audio features using Essentia
    rhythm_extractor = es.RhythmExtractor2013()
    bpm, beats, beats_confidence, _, _ = rhythm_extractor(audio)
    key = es.KeyExtractor()(audio)
    loudness = es.Loudness()(audio)
    spectral_centroid = es.SpectralCentroidTime()(audio)
    zero_crossing_rate = es.ZeroCrossingRate()(audio)

    # Print out the analyzed information
    print(f'File: {file_path}')
    print(f'BPM: {bpm} (Confidence: {beats_confidence})')
    print(f'Key: {key}')
    print(f'Loudness: {loudness}')
    print(f'Spectral Centroid: {spectral_centroid}')
    print(f'Zero Crossing Rate: {zero_crossing_rate}')

if __name__ == '__main__':
    file_path = input('Enter the path to an audio file: ')

    if is_audio_file(file_path):
        analyze_audio_file(file_path)
    else:
        print('Invalid audio file. Please provide a valid audio file path.')

