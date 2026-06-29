import fal_client

result = fal_client.subscribe(
    "bytedance/seedance-2.0/text-to-video",
    arguments={
        "prompt": "桜並木を歩く白い猫。映画のような映像。",
        "resolution": "720p",
        "duration": "10",
        "aspect_ratio": "16:9",
        "generate_audio": True,
    },
)

print(result)
print(result["video"]["url"])