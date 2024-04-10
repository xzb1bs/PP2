import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.current_track_index = 0
        self.tracks = []
        self.load_tracks()
        self.play_current_track()

    def load_tracks(self):
        music_folder = "music"  # Folder where your music files are stored
        for file in os.listdir(music_folder):
            if file.endswith(".mp3"):
                self.tracks.append(os.path.join(music_folder, file))

    def play_current_track(self):
        if self.tracks:
            pygame.mixer.music.load(self.tracks[self.current_track_index])
            pygame.mixer.music.play()
            self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_track(self):
        self.stop()
        self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
        self.play_current_track()

    def previous_track(self):
        self.stop()
        self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
        self.play_current_track()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.playing:
                        self.stop()
                    else:
                        self.play_current_track()
                elif event.key == pygame.K_n:
                    self.next_track()
                elif event.key == pygame.K_p:
                    self.previous_track()

    def run(self):
        running = True
        while running:
            self.handle_events()
            pygame.time.Clock().tick(10) 
            
if __name__ == "__main__":
    player = MusicPlayer()
    player.run()