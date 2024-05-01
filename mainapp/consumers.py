# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.video_id = self.scope['url_route']['kwargs']['video_id']
        self.room_group_name = f"video_{self.video_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data['action']

        if action == 'like':
            # Handle like logic here
            await self.handle_like(data)
        elif action == 'comment':
            # Handle comment logic here
            await self.handle_comment(data)
        elif action == 'load_comments':
            # Handle loading comments logic here
            await self.send_comments()

    async def send_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=event['message'])

    async def handle_like(self, data):
        # Increment the likes count for the video (you need to have a Video model)
        # Replace this with your actual Video model logic
        video_id = data['video_id']
        video = await self.get_video(video_id)
        video.likes += 1
        video.save()

        # Broadcast the updated likes count to all clients in the group
        await self.send_likes_count(video.likes)

    async def handle_comment(self, data):
        # Add the comment to the video's comments field (you need to have a Video model)
        # Replace this with your actual Video model logic
        video_id = data['video_id']
        comment_text = data['comment']
        video = await self.get_video(video_id)
        video.comments += f"{comment_text}\n"
        video.save()

        # Broadcast the updated comments to all clients in the group
        await self.send_comments()

    async def send_likes_count(self, likes_count):
        # Send the updated likes count to all clients in the group
        response_data = {
            'action': 'update_likes_count',
            'video_id': self.video_id,
            'likes_count': likes_count,
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': json.dumps(response_data)
            }
        )

    async def send_comments(self):
        # Get the comments for the video (you need to have a Video model)
        # Replace this with your actual Video model logic
        video = await self.get_video(self.video_id)
        comments = video.comments.split('\n')

        # Send the updated comments to all clients in the group
        response_data = {
            'action': 'update_comments',
            'video_id': self.video_id,
            'comments': comments,
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': json.dumps(response_data)
            }
        )

    async def get_video(self, video_id):
        # Replace this with your actual Video model retrieval logic
        # This is just a placeholder method
        pass  # Implement your logic to get the video from the database
