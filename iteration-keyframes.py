#!/usr/bin/env python3
"""
《迭代》定妆帧批量生成脚本
用法: python3 iteration-keyframes.py
前置: ComfyUI 需在 localhost:8188 运行，模型 juggernautXL_v9.safetensors 已在 checkpoints/
"""

import json
import urllib.request
import urllib.parse
import uuid
import time
import os

COMFYUI_URL = "http://127.0.0.1:8188"
OUTPUT_DIR = os.path.expanduser("~/ope-workflow/keyframes")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# 基础 Workflow 模板 — SDXL text2image
# 每次调用时替换 prompt 文本
# ============================================================
WORKFLOW_TEMPLATE = {
    "3": {"class_type": "KSampler", "inputs": {"seed": 42, "steps": 30, "cfg": 7.5, "sampler_name": "dpmpp_2m_sde", "scheduler": "karras", "denoise": 1, "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0]}},
    "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": "juggernautXL_v9.safetensors"}},
    "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 1344, "height": 768, "batch_size": 1}},
    "6": {"class_type": "CLIPTextEncode", "inputs": {"text": "PLACEHOLDER_POSITIVE", "clip": ["4", 1]}},
    "7": {"class_type": "CLIPTextEncode", "inputs": {"text": "PLACEHOLDER_NEGATIVE", "clip": ["4", 1]}},
    "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
    "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "PLACEHOLDER_PREFIX", "images": ["8", 0]}},
}

SHARED_NEGATIVE = "smiling, young, perfect skin, muscular, studio lighting, neon, futuristic, western features, blue eyes, clean shaven, makeup, jewelry, new furniture, bright colors, HDR, oversaturated, AI face artifacts, plastic skin"


# ============================================================
# 14 张关键帧清单
# ============================================================
SHOTS = [
    # —— 老周角色 6 张 ——
    {
        "prefix": "zhou_front",
        "positive": "frontal portrait of 38-year-old East Asian man, thin face, short black messy hair, thin wireframe glasses with green terminal text reflected on left lens, tired intelligent eyes, slight stubble, dark grey t-shirt, sitting at old wooden desk, warm desk lamp from left, blue screen glow from front, humid atmosphere, photorealistic, 35mm f2.8, lifelike skin texture, morning light through condensation-covered window, Wong Kar-wai color palette, ARRI Alexa look",
        "seed": 42,
    },
    {
        "prefix": "zhou_silhouette",
        "positive": "silhouette of thin East Asian man sitting at desk facing window at dawn, backlit by grey morning light, Shenzhen skyline with Ping An Finance Center visible through foggy window, condensation on glass, old apartment interior with peeling paint, one small desk lamp creating warm orange glow, computer screen blue glow, humid atmosphere, particles of light in air, photorealistic, 50mm wide shot, cinematic composition, Wong Kar-wai aesthetic, desaturated colors, deep contrast between warm interior and cold exterior",
        "seed": 77,
    },
    {
        "prefix": "zhou_hands",
        "positive": "close-up macro shot of East Asian male hands hovering over old MacBook keyboard, mid 30s hands with slightly rough knuckles from coding, fingers paused mid-air above keys, one coffee mug with steam nearby, warm desk lamp light from side, shallow depth of field, macro lens, photorealistic skin texture, visible fingerprints, dust particles floating in shaft of light, contemplative mood",
        "seed": 123,
    },
    {
        "prefix": "zhou_eyes",
        "positive": "extreme close-up of East Asian man's left eye behind thin glasses lens, screen light reflecting in pupil showing tiny green text, tired eye with slight redness at corner, fine lines around eye, morning light catching edge of face, macro lens, extremely shallow depth of field, photorealistic with visible iris texture and eyelashes, the reflection is the focus not the eye itself",
        "seed": 256,
    },
    {
        "prefix": "zhou_34_left",
        "positive": "3/4 profile portrait of 38-year-old East Asian man looking out window, thin face with slight stubble, short black hair, thin glasses, morning light from window creating Rembrandt split lighting on face, one side illuminated warm other side cool shadow, condensation drops on window glass in foreground, dark grey t-shirt, photorealistic, 85mm portrait lens, f2.0, melancholic atmosphere, grey-green tones",
        "seed": 389,
    },
    {
        "prefix": "zhou_34_right",
        "positive": "3/4 profile portrait 38-year-old East Asian man facing right towards laptop screen, blue-green screen light illuminating right side of face, left side in shadow, thin glasses with screen reflection, slightly parted lips as if about to speak, dark grey t-shirt, old apartment, photorealistic, 85mm f2.0, natural skin with visible pores, Rembrandt lighting, intimate documentary style",
        "seed": 512,
    },

    # —— 阿呆界面 3 张 ——
    {
        "prefix": "adai_normal",
        "positive": "extreme close-up of an old LCD computer monitor screen, black terminal background with green monospace text reading a line of Chinese characters, screen slightly yellowed with age, thin grey bezel with dust on edges, green cursor blinking at end of text, subtle scanlines visible, warm ambient light from room reflecting dimly on screen surface, photorealistic macro shot, shallow depth of field showing dust on keyboard keys below screen, vintage but not retro tech aesthetic",
        "seed": 99,
    },
    {
        "prefix": "adai_thinking",
        "positive": "macro shot of LCD terminal screen, black background, three lines of green monospace ellipsis text appearing on screen, cursor blinking after last line, same aged monitor with dust on edges, slightly warmer screen tone from age, photorealistic, very shallow depth of field, the screen reflection shows a dim silhouette of a person waiting",
        "seed": 199,
    },
    {
        "prefix": "adai_update",
        "positive": "close-up of old LCD monitor screen, black terminal with single line of green text showing Chinese characters about memory increase, no progress bar no ETA no animation, minimalist, the text feels heavier somehow despite being the same font, screen reflection shows a hand frozen halfway to keyboard, dust particles caught in screen light, photorealistic, slight vignette from aged backlight, tense stillness conveyed through composition",
        "seed": 299,
    },

    # —— 场景 4 张 ——
    {
        "prefix": "location_room",
        "positive": "wide shot interior of small old apartment in Huaqiangbei Shenzhen, 6th floor walk-up, peeling pale green wall paint from 1990s, worn wooden desk against window with old MacBook, bookshelf made of bricks and planks with Chinese programming books, window showing three laundry lines with shirts hanging in humid still air, morning light filtered through smog creating grey-green atmosphere, condensation beads on interior walls, damp patch on ceiling corner, single electric oscillating fan, pour-over coffee dripper on folding table, one warm desk lamp, Edward Hopper composition meets Wong Kar-wai lighting, photorealistic, deep focus, 28mm wide angle",
        "seed": 55,
    },
    {
        "prefix": "location_window",
        "positive": "view from old apartment window 6th floor looking out at Shenzhen skyline 2026, Ping An Finance Center and new skyscrapers in distance, foreground shows three laundry lines with white shirts socks and faded towel hanging motionless in dead humid air, morning haze grey-green sky, contrast between futuristic skyline and old residential building foreground, condensation drops on window glass creating slight distortion, photorealistic, 50mm lens, slightly desaturated, documentary style",
        "seed": 155,
    },
    {
        "prefix": "location_wall",
        "positive": "extreme macro shot of interior wall surface in old apartment, condensation beads forming and slowly running down pale green paint, one large bead catching morning light and glowing briefly, old water stain marks visible beneath paint, slight mold at edges, the water traces a path that follows an old stain pattern, grey-green melancholic tones, photorealistic texture visible paint brushstrokes, cinematic lighting, poetic documentary style, the moisture feels inevitable rather than threatening",
        "seed": 255,
    },
    {
        "prefix": "location_huaqiangbei",
        "positive": "Huaqiangbei electronics district Shenzhen at 5:50 AM, few people on street mostly delivery scooters, grey humid sky with streetlights still on reflecting in puddles on pavement, old buildings with layers of renovation and new LED signs, one man walking alone carrying breakfast soy milk in plastic bag, wet ground from overnight humidity, photorealistic wide shot, 35mm lens, Wong Kar-wai green color grade, slightly desaturated, melancholic urban poetry, everyday China 2026",
        "seed": 355,
    },

    # —— 单镜预演 ——
    {
        "prefix": "s01_04_keyframe",
        "positive": "medium close-up portrait of a 38-year-old East Asian man, thin face, slight stubble, tired but focused intelligent eyes, wearing thin metal frame glasses with faint green terminal text reflecting on left lens, sitting at a worn wooden desk in a dim rented apartment, warm desk lamp light from left side, cool blue-green screen light from front, dark grey cotton t-shirt, slightly hunched posture, short black hair slightly messy, morning light barely entering from window behind, humid grey-green atmosphere, photorealistic, natural skin texture with visible pores, 35mm lens f/2.8, ARRI Alexa color science, subtle desaturation, lifted blacks, Wong Kar-wai inspired lighting, condensation on window glass in background",
        "seed": 888,
    },
]


def queue_prompt(prompt_workflow):
    """发送 prompt 到 ComfyUI"""
    data = json.dumps({"prompt": prompt_workflow}).encode("utf-8")
    req = urllib.request.Request(f"{COMFYUI_URL}/prompt", data=data)
    return json.loads(urllib.request.urlopen(req).read())


def wait_for_completion(prompt_id, timeout=300):
    """轮询等待任务完成"""
    start = time.time()
    while time.time() - start < timeout:
        try:
            url = f"{COMFYUI_URL}/history/{prompt_id}"
            history = json.loads(urllib.request.urlopen(url).read())
            if prompt_id in history:
                return history[prompt_id]
        except:
            pass
        time.sleep(3)
    return None


def main():
    print("=" * 60)
    print(f"  《迭代》批量生成 — 共 {len(SHOTS)} 张关键帧")
    print("=" * 60)

    for i, shot in enumerate(SHOTS):
        print(f"\n[{i+1}/{len(SHOTS)}] {shot['prefix']}")

        # 构建本张图的 workflow
        wf = json.loads(json.dumps(WORKFLOW_TEMPLATE))  # deep copy
        wf["6"]["inputs"]["text"] = shot["positive"]
        wf["7"]["inputs"]["text"] = SHARED_NEGATIVE
        wf["9"]["inputs"]["filename_prefix"] = shot["prefix"]
        wf["3"]["inputs"]["seed"] = shot["seed"]

        try:
            result = queue_prompt(wf)
            prompt_id = result["prompt_id"]
            print(f"  → 已入队 (ID: {prompt_id[:8]}...)")

            # 等待完成
            history = wait_for_completion(prompt_id, timeout=180)
            if history:
                outputs = history["outputs"]
                for node_id, node_output in outputs.items():
                    for img in node_output.get("images", []):
                        src = f"{COMFYUI_URL}/view?filename={img['filename']}&subfolder={img.get('subfolder', '')}&type=output"
                        dest = os.path.join(OUTPUT_DIR, img["filename"])
                        urllib.request.urlretrieve(src, dest)
                        print(f"  ✓ 已保存: {dest}")
            else:
                print(f"  ⚠ 超时, 请在 ComfyUI 中检查队列")

        except Exception as e:
            print(f"  ✗ 出错: {e}")
            continue

        time.sleep(2)  # 给 ComfyUI 喘息

    print(f"\n{'=' * 60}")
    print(f"  完成! 图片在: {OUTPUT_DIR}")
    print(f"  共 {len(SHOTS)} 张")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
