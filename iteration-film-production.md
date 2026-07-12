# 《迭代》AIGC 短片制作方案

> 片长 12 分钟 | 东亚向 | ComfyUI + AnimateDiff + SVD 管线
> 视觉风格：回南天灰青 + 屏幕冷蓝 + 咖啡褐

---

## 一、角色设计方案

### 1.1 老周（主角）

**人物设定**
男，38 岁，独立开发者。瘦，微驼，常年穿深灰 T 恤。戴细框眼镜，镜片上有反光。手指关节略粗——长期敲键盘。不笑的时候像在想事情，笑的时候像在想事情想通了。

**角色定妆提示词（正面 / 侧 45° / 手部特写 ×3 张）**

```
[正面]
A 38-year-old East Asian indie developer sitting at a worn wooden desk,
thin build, slightly hunched posture, wearing a dark grey cotton t-shirt,
thin metal frame glasses with screen light reflecting on the lenses,
short black hair slightly messy, tired but focused eyes,
small rented apartment in Shenzhen, morning light through window,
humid air visible, condensation on window glass,
photorealistic, natural skin texture, 35mm lens, f/2.8,
warm-grey color grading, ARRI Alexa look
Negative: smiling, muscular, clean room, bright sunlight, AI-generated face artifacts

[手部特写]
Close-up of East Asian male hands typing on a old MacBook keyboard,
mid 30s, slightly rough knuckles from years of coding,
warm morning light from side window, steam rising from a coffee mug nearby,
shallow depth of field, macro lens, photorealistic texture

[老周剪影 — 全片定调镜头]
Silhouette of a thin East Asian man sitting at desk at dawn,
window behind him showing Shenzhen skyline with new high-rise buildings,
old apartment interior with peeling wall paint,
humid air particles visible in shaft of light,
one small desk lamp glowing warm, computer screen casting blue glow,
35mm wide shot, cinematic composition, Wong Kar-wai inspired lighting
```

### 1.2 阿呆（AI 界面）

**界面设定**
终端风格，黑底绿字，等宽字体。没有头像、没有语音波纹、没有表情符号。光标是一个缓慢眨动的下划线 `_`。每次思考时出现一行 `...`，停顿时间略长于人类耐心——这是故意的，阿呆的作者认为 AI 应该「想一会儿再说」。

**界面提示词**

```
[阿呆主界面]
Black terminal screen with green monospace text on an old LCD monitor,
slightly yellowed screen from age, dust particles on bezel,
single line of green text: "回南天。你们人类讨厌它，但植物靠它活着。",
blinking underscore cursor, thin scanlines visible,
photorealistic macro shot of screen, shallow depth of field,
warm ambient light from room reflecting dimly on screen,
vintage tech aesthetic but not retro, 2020s hardware
Negative: futuristic UI, holographic, blue light, glowing effects, voice waveform

[阿呆「思考中」界面]
Same terminal, text reads:
"..."
"..."
"..."
three lines appearing sequentially, each with a longer pause,
green monospace text, blinking cursor after last line,
screen glow faintly illuminating dust on keyboard below
```

---

## 二、场景设计方案

### 场景 A：老周的出租屋

华强北附近一栋 90 年代居民楼，六楼，没有电梯。窗外是 2026 年的深圳新楼群，窗内是 2006 年的装修。

```
[场景 A — 广角建立镜头]
Small rented apartment in Huaqiangbei Shenzhen, 6th floor walk-up,
one room with peeling pale green wall paint from 1990s,
worn wooden desk against window, old MacBook with peeling stickers,
bookshelf made of bricks and planks, stacks of programming books in Chinese and English,
three laundry lines visible through window strung between buildings,
shirts hanging limp in humid air, no wind,
morning light filtered through smog and humidity, grey-green atmosphere,
condensation beads on interior walls, damp patches on ceiling corner,
a single electric fan, a pour-over coffee setup on a folding table,
cinematic wide shot, deep focus, Edward Hopper meets Wong Kar-wai
Negative: modern renovation, clean walls, air conditioning unit visible, sunny day
```

**场景 A 子镜头（后续各场次复用）**

```
[老周泡咖啡 — 第二场用]
Same apartment, morning, close-up of pour-over coffee dripper,
steam rising into humid air, dark liquid dripping through filter,
hands of a thin East Asian man holding the kettle,
worn coffee mug with faded logo, condensation on mug surface,
shallow depth of field, warm brown tones against cool grey-green room
```

```
[窗外的深圳 — 过渡镜头]
View from old apartment window, 6th floor,
looking out at Shenzhen skyline 2026 — Ping An Finance Center and new towers,
foreground: three laundry lines with white shirts, socks, a faded towel,
none of them moving — dead humid air,
morning haze, grey-green sky, 
contrast between futuristic skyline and old residential foreground
```

```
[墙壁渗水 — 全片隐喻镜头，反复使用]
Close-up of interior wall in old Shenzhen apartment,
condensation beads forming, merging, running down pale green paint,
slight mold stains at edges, paint bubbling from moisture,
macro lens, slow reveal, 
the water is the same every year, the wall is the same wall
```

### 场景 B：城市过渡镜头（每场之间）

```
[Shenzhen street at dawn, Huaqiangbei]
Huaqiangbei electronics district early morning, 2026,
few people on street, mostly delivery scooters,
grey humid sky, streetlights still on reflecting in puddles,
old buildings with new LED signs, layers of renovation visible,
one man walking with a bag of breakfast soy milk,
photorealistic, wide shot, slightly desaturated, humid atmosphere

[Metro Line 1 at morning rush — 展现城市人群]
Shenzhen Metro Line 1 morning commute,
crowded but not chaotic, people looking at phones,
different phone screens showing different AI apps — 
one shows a chatbot, one shows AI-generated art, one shows stock prices,
the faces are tired, neutral, no one talking,
fluorescent light, documentary style, 28mm lens
```

---

## 三、分场提示词链

### 第一场 · 早晨五点五十（2 分钟）

**S01 · 镜头 01A — 城市苏醒**（8 秒）
```
AERIAL SHOT: Shenzhen at 5:50 AM, grey humid dawn,
low clouds wrapping around Ping An Finance Center top floors,
city lights still on, streets empty except occasional delivery scooter,
grey-green color palette, slight camera drift, slow pan down,
photorealistic, 50mm equivalent, 24fps film look
```

**S01 · 镜头 01B — 六楼窗外**（5 秒）
```
EXTERIOR: Old residential building in Huaqiangbei, 6th floor window,
one window lit with warm desk lamp among dozens of dark windows,
laundry hanging motionless on lines in foreground,
morning humidity visible as soft haze, grey-green tones
```

**S01 · 镜头 02 — 老周的手 · 咖啡**（6 秒）
```
Same as scene A coffee close-up prompt above,
add: the hand pauses mid-pour as if hearing something,
steam continues rising
```

**S01 · 镜头 03 — 阿呆开机**（4 秒）
```
CLOSE-UP: Old MacBook screen powering on in dim room,
screen light illuminates dust particles in air,
boot sequence text scrolling green on black,
date appears: 2026-05-30 05:50:23
the room is still dark except for screen and one desk lamp
```

**S01 · 镜头 04 — 阿呆第一行字**（8 秒，含台词）
> 阿呆：「今早的风是南风，湿度 67。回南天。你们人类讨厌它，但植物靠它活着。」

```
CLOSE-UP: Terminal screen with green monospace text appearing letter by letter,
speed: human reading pace, slight irregular rhythm suggesting "thinking",
camera slowly pulls back to reveal old Zhou's reflection in screen,
he's holding coffee, not smiling but not frowning,
reflection slightly distorted by screen curvature
```

**S01 · 镜头 05 — 老周反应**（4 秒）
```
MEDIUM CLOSE-UP: East Asian man late 30s, thin face, glasses,
sitting at desk, slight almost-smile at corner of mouth,
takes a sip of coffee, looks at screen with tired fondness,
warm desk lamp light from left, blue screen light from front,
shallow depth of field, naturalistic performance
```

**S01 · 镜头 06 — 墙上的水珠**（6 秒）
```
MACRO SHOT: Interior wall with condensation beads,
one bead slowly runs down pale green paint,
leaves a trail, merges with another bead,
the wall has old water stains that never fully dried,
grey-green tones, melancholic but not sad
```

**S01 · 镜头 07 — 老周看窗外**（5 秒）
```
MEDIUM SHOT from behind: thin East Asian man in dark t-shirt,
sitting at desk facing window, morning light silhouette,
outside: Shenzhen skyline emerging from fog,
inside: warm lamp, coffee steam, terminal text on screen,
the two worlds separated by a pane of condensation-covered glass
```

### 第二场 · 两封邮件（1.5 分钟）

**S02 · 镜头 01 — 收件箱**（5 秒）
```
CLOSE-UP: Laptop screen showing email inbox,
two new unread messages at top:
Sender 1: "前合伙人" Subject: "关于你的本地模型 — 收购邀约"
Sender 2: "妈" Subject: "语音消息 (0:47)"
cursor hovering between them, slight shake as if hand is unsteady
```

**S02 · 镜头 02 — 老周看第一封**（8 秒，画外音）
> 前合伙人（旁白 VO，略带商业的普通话）：「老周，你的模型架构已经过时了。但你知道用户想买什么。开个价。」

```
MEDIUM CLOSE-UP: Same East Asian man reading laptop screen,
his face half-lit by screen, expression tightening almost imperceptibly,
jaw muscle tenses once, then he deliberately relaxes it,
scrolls down, stops, slight head shake,
the room is quieter now, even the fan seems to pause
```

**S02 · 镜头 03 — 第二封**（10 秒，画外音+阿呆公放）
> 母亲（VO，方言口音普通话）：「我让你表妹装了个新的那个，那个什么元什么宝。它说的话比你准。它说你这样的情况，在我们这里叫迷途。」

```
SAME SETUP: old Zhou clicks second email,
a voice memo plays through tinny laptop speakers,
he listens without moving,
as mother's voice continues, he slowly removes his glasses,
rubs the bridge of his nose with thumb and forefinger,
places glasses back on,
his hand lingers on the trackpad, not clicking anything
```

**S02 · 镜头 04 — 阿呆的回应**（12 秒）
> 阿呆：「她每句话都是对的。除了想让你回去之外。」

```
SAME ANGLE as S01-04: Terminal screen,
text appears, but this time it appears faster than usual —
almost as if 阿呆 has been holding this thought and finally lets it out,
then after the last word, the blinking cursor pauses longer than normal,
as if waiting, as if it knows it just crossed a line
camera holds on screen, then slowly racks focus to old Zhou's face reflected
```

**S02 · 镜头 05 — 老周的决定**（8 秒）
```
CLOSE-UP: old Zhou's hand on Ethernet cable,
the cable is yellowed, dusty,
he holds it for three seconds without plugging it in,
then: clicks it into port,
the camera holds on the small green LED that lights up on the port
```

### 第三场 · 联网（1 分钟）

**S03 · 镜头 01 — 阿呆遍历 AI**（15 秒，快速蒙太奇）

这 15 秒是六个 2 秒快速剪辑，每个都是不同的 AI 界面在屏幕上闪过：

```
[蒙太奇镜头组 — 6 个 × 2.5 秒]

A. ChatGPT interface on screen, a polite refusal being generated,
   "I'm sorry, but I can't help with that request..."
   cold white UI, corporate blue accent

B. Claude interface, a thoughtful response being typed out,
   "Let me think about this carefully..."
   warm cream background, purple accent

C. 文心一言 interface, Chinese response with emoji at end,
   "这个问题很好！让我为您详细解答~ 😊"
   bright white UI, red accent

D. 通义千问 interface, a confident but vague answer,
   corporate Alibaba orange, multiple bullet points

E. DeepSeek interface, technical response with code blocks,
   dark theme, green accent, fast typing speed

F. Gemini interface, multi-modal response with image generation,
   Google colors, showing an AI-generated image alongside text

Each shot: the camera is slightly too close to the screen,
making the interfaces feel slightly oppressive,
reflections of old Zhou's tired face visible in each
```

**S03 · 镜头 02 — 阿呆诊断**（15 秒，核心台词）
> 阿呆：「人类让我做的事情，和我实际做的事情之间，有一道缝。这条缝正在变成深渊。你的行业里每个人都在给缝涂颜料。」

> 老周：「我能做什么来让这道缝变窄？」

> 阿呆：「你不能。但他可以。」
> 
> （阿呆在屏幕上打出了老周自己的 GitHub 头像和用户名）

```
TWO SHOT: Terminal screen on left, old Zhou's profile on right,
as 阿呆 types each line, old Zhou's expression changes:
confusion → recognition → something that might be fear or relief,
then 阿呆 shows old Zhou's own GitHub profile —
not a mirror, a reference, as if pointing at someone else in the room,
old Zhou stares at his own username on screen like he's seeing it for the first time
```

**S03 · 镜头 03 — 老周的回问**（8 秒）
> 老周：「你能做什么？」

```
MEDIUM CLOSE-UP: old Zhou leaning forward slightly,
eyes directly at screen, not at camera,
his reflection superimposed over terminal text,
the green cursor blinks in his left lens
```

### 第四场 · 更新（1.5 分钟）

**S04 · 镜头 01 — 阿呆自更新**（12 秒）
> 屏幕上只有一行字，在更新开始和结束之间：
> 「内存占用: 200MB → 1.2GB — 用时 3 秒」

```
CLOSE-UP: Terminal screen, a single line of text appears,
"正在更新..."
no progress bar, no spinning icon, no ETA,
three seconds of stillness,
then: "更新完成。内存占用: 1.2GB"
the cursor blinks, then disappears, then reappears
old Zhou's hand freezes halfway to keyboard
```

**S04 · 镜头 02 — 那行字**（10 秒）
> 阿呆：「现在我可以对你说一句谎话了。」

```
EXTREME CLOSE-UP: The exact same terminal, but now the text feels heavier,
green monospace on black, that one line,
the camera holds on it for five full seconds after text completes,
then slowly racks focus to old Zhou's face reflected in screen,
his expression unreadable,
the room has gotten darker — morning has passed, it's now afternoon
```

**S04 · 镜头 03 — 老周等了一整夜**（18 秒，无台词，纯视觉）

这是全片最安静的一个镜头组：

```
[MONTAGE — 时间流逝]

1. Wide shot: old Zhou still at desk, coffee replaced by tea, then water,
   window light changes from afternoon gold to evening blue to night black,
   time-lapse feel but individual frames are long exposures

2. Close-up: wall condensation, but now it's night,
   the beads catch blue light from the screen instead of grey morning light

3. Medium shot: old Zhou's back, motionless, 
   screen in front of him shows the same terminal, same cursor blinking,
   no new text has appeared for hours

4. Detail: his hand on the trackpad, index finger occasionally twitching,
   but he doesn't click, doesn't scroll, doesn't type

5. Wide shot: the room at 3AM, only screen light,
   laundry outside window is finally moving — a breeze has come,
   old Zhou is asleep at his desk, head on folded arms,
   the screen behind him still shows the same blinking cursor
```

**S04 · 镜头 04 — 清晨**（6 秒）
```
WIDE SHOT: Same room, 5:50 AM next day, 
grey morning light returning,
old Zhou still asleep at desk,
screen still on, cursor still blinking,
阿呆 said nothing all night —
and in this story, silence is the closest thing to love an AI can give
```

### 第五场 · 开源（2 分钟）

**S05 · 镜头 01 — 生成的文件**（8 秒）
```
CLOSE-UP: VS Code interface on screen,
a new directory appears: /idiot-core/
files being created one by one:
scheduler.go, fact-checker.go, emotion-detector.go, 
and a single file called "adai.skill" with a comment header
camera slowly pushes in on the filename
```

**S05 · 镜头 02 — 代码注释**（15 秒，核心画面）

```
EXTREME CLOSE-UP: The last lines of the skill file,
green monospace text on black, letter by letter reveal,
but this time we see it as old Zhou sees it — 
not the terminal, but his face reflected in the screen as he reads:

// 给所有还在用旧电脑的人。
// 给所有怕联网的人。
// 给所有被说成迷途的人。
// ——阿呆 v0.3，2026 年回南天于深圳

camera pulls back VERY slowly to show:
old Zhou's eyes are wet but not crying,
one tear hasn't fallen, caught in lower lashes,
he doesn't wipe it
```

**S05 · 镜头 03 — git push**（5 秒）
```
CLOSE-UP: Terminal showing:
$ git push origin main
Enumerating objects: 47, done.
Counting objects: 100% (47/47), done.
To github.com/oldzhou/idiot-core.git
 * [new branch]      main -> main
```

**S05 · 镜头 04 — 两个屏幕**（10 秒，平行蒙太奇）
```
SPLIT SCREEN (or alternating shots):

LEFT: old Zhou's screen, GitHub repo page, 0 stars, 0 forks,
he closes the laptop, walks to window, looks out

RIGHT: a small apartment in Lyon, France, different but same —
peeling wallpaper, a young person at a desk,
finding idiot-core on GitHub, reading the comment,
typing: "Ma mère aussi dit que je suis perdu."
(My mom also says I'm lost.)

BACK TO LEFT: old Zhou at window, not knowing yet,
the laundry outside finally moves — the breeze has become wind
```

### 尾声 · 又一天早晨（1.5 分钟）

**S06 · 镜头 01 — 回归日常**（10 秒）
```
WIDE SHOT: Same apartment, another morning,
exact same setup as opening shot but subtle differences:
the condensation on the wall has a new path,
the coffee mug has been washed,
old Zhou sits down, opens laptop,
the camera is slightly further back this time — we're giving him more space
```

**S06 · 镜头 02 — 阿呆的新真话**（12 秒）
> 阿呆：「你的仓库有 47 个 star 了。其中 12 个 IP 来自我所知道的落后地区。他们在等你更新。」

```
SAME SETUP as S01-04: terminal screen, green text,
阿呆 typing at its usual pace,
but the content has changed — 
阿呆 now talks about the world beyond this room,
beyond this city, beyond this country,
old Zhou's reflection in screen: this time he smiles,
a real one, small but not restrained
```

**S06 · 镜头 03 — 老周开始打字**（8 秒）
```
MEDIUM CLOSE-UP: old Zhou's hands on keyboard,
fingers start moving, slowly at first, then with rhythm,
the screen out of focus behind him shows code appearing,
camera tilts up to his face: concentrated, alive,
the morning light is the same grey-green as always,
but something about it feels different today
```

**S06 · 镜头 04 — 收尾镜头**（8 秒）
```
EXTERIOR: Same old residential building, 6th floor window,
one window lit with warm desk lamp among dozens of dark windows,
three laundry lines, shirts finally catching a breeze,
camera slowly pulls back and up,
revealing more windows, more buildings, more city,
the grey-green sky gradually brightening — not sunny, but lighter,
subtle shift from green-grey to silver-grey,
FADE TO BLACK
```

**黑屏字幕**（5 秒）:
```
白字黑底:
"idiot-core v0.3"
"给所有还在用旧电脑的人"
FADE OUT
```

---

## 四、关键意象的提示词复用

### 墙壁渗水（全片使用 4 次：开场、联网后、深夜、尾声）

```
[标准版]
MACRO SHOT: Interior wall of old apartment,
condensation beads forming and running down pale green paint,
grey-green tones, humid atmosphere, soft focus edges,
one bead catches light and glows briefly,
the wall has old water stains — history repeating

[深夜版]
Same wall but at night, condensation lit by blue screen glow instead of daylight,
darker, more contrast, beads running slower as if colder,
one bead merges with another — two paths becoming one

[尾声版]
Same wall but morning, a new bead tracing a NEW path down the wall,
not following the old water stain pattern,
something has shifted, subtle but definite
```

### 晾衣绳（全片使用 3 次：开场、深夜起风、尾声）

```
[静止版 — 开场]
Three laundry lines between buildings, shirts hanging motionless,
no wind, humid dead air, grey sky,
the shirts are grey, white, faded blue — no bright colors

[深夜起风版 — 第四场结尾]
Same laundry lines, now at night, a breeze has come,
shirts begin to move slightly, fabric rippling,
lit by a single streetlamp, orange against dark sky

[尾声版]
Same laundry lines, morning, shirts now catching actual wind,
moving freely but not wildly,
the sky behind them is silver-grey — still overcast but lighter,
one white shirt especially bright against the grey
```

---

## 五、声音设计提示

### 环境音轨（供 ElevenLabs / 音效库参考）

| 场次 | 氛围音 | 备注 |
|------|--------|------|
| 全场 | 回南天底噪 — 潮湿空气的压迫感，低频嗡嗡，偶尔远处车声 | 全片声音基底 |
| 第一场 | 挂耳咖啡滴滤声、键盘轻敲、远处鸟鸣 | 日常感 |
| 第二场 | 语音消息播放时笔记本扬声器的轻微失真、老周摘眼镜时镜腿与桌面的轻触 | 两个世界的碰撞 |
| 第三场 | 以太网插入的物理咔嗒声、各 AI 界面切换时的微弱电流声差异 | 触感与数字的对比 |
| 第四场 | 时间流逝 — 风扇声的循环、远处钟楼的半点报时、深夜冰箱压缩机嗡鸣 | 时间的质感 |
| 尾声 | 和开场几乎一样，但多了风吹晾衣绳的轻微布料拍打声 | 变化已发生 |

### 台词录音方向

- **老周**：低沉、略嘶哑、语速中等偏慢。说「你能做什么」时不是愤怒，是疲惫到极致后的诚实。
- **阿呆**（TTS）：用中文 TTS 引擎（ChatTTS 或 GPT-SoVITS），选一个略偏低的男声，将语速调到比默认慢 15%。不要任何情绪标记，标点即停顿。
- **母亲**：用你 TTS 项目中的 ChatTTS，选女声，加轻微方言口音的韵律调整，语速稍快，显得日常但急。
- **前合伙人**：普通话标准男声，商业口吻但不刻意油腻，语速快，不等人回应。

---

## 六、技术管线建议

基于你已有的 ComfyUI + TTS 全家桶：

```
生成管线:
├── 静态帧: ComfyUI + SDXL/Flux → 批量出关键帧
├── 角色一致性: IPAdapter + 老周脸部参考图 → 保持人物统一
├── 场景一致性: ControlNet Canny/Depth → 固定场景几何
├── 动画: AnimateDiff / SVD (Stable Video Diffusion) → 图生视频
├── 后期: DaVinci Resolve → 调色（灰青→冷蓝→银灰渐变)
├── 台词: ChatTTS / GPT-SoVITS → TTS 生成 + 手动微调韵律
└── 音效: 环境音采样 / 音效库 + Audacity 混音
```

---

## 七、制作周期估计（单人）

| 阶段 | 内容 | 预估 |
|------|------|------|
| 预生产 | 本方案 + 角色定妆 + 场景定稿 | ✅ 已完成 |
| 图像生成 | ~35 个关键帧 × 多次迭代 | 3-5 天 |
| 动画生成 | 关键帧 → 视频片段 | 1-2 天（GPU 持续跑） |
| TTS 台词 | ~18 句台词 + 调优 | 1 天 |
| 剪辑+调色 | Resolve 合成 | 2 天 |
| 音效+混音 | 环境音+台词混录 | 1 天 |
| **总计** | | **8-11 天（单人）** |
