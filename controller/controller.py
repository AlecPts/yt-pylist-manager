# from model.linked_list import LinkedPlaylist
#
# class Controller:
#     # Initialize controller
#     def __init__(self):
#         self.playlist = LinkedPlaylist()
#
#     def add_video(self, video_url):
#         self.playlist.add(video_url)
#
#     def get_all_videos(self):
#         videos = []
#         pos = 1
#         while (video := self.playlist.access_by_position(pos)) is not None:
#             videos.append(video)
#             pos += 1
#         return videos