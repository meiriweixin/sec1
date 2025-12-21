import json

# Load file
with open("chapters/sec1_humanities_chapters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

humanities = data["subjects"][0]

# Chapter 4 Section 2: Coordinates and Scale
ch4_section2 = {
    "id": "coordinates-scale",
    "type": "text",
    "title": "Coordinates and Map Scale",
    "title_zh": "坐标和地图比例尺",
    "content": """**Understanding Coordinates**

Coordinates help us pinpoint exact locations on a map or globe using a grid system.

**The Global Grid System**

**Latitude Lines** (Parallels):
- Run **east-west** (horizontal)
- Measure distance **north or south** of the equator
- Range: 0° (Equator) to 90°N (North Pole) and 90°S (South Pole)
- Major lines:
  - **Equator** (0°) - divides Earth into Northern and Southern hemispheres
  - **Tropic of Cancer** (23.5°N)
  - **Tropic of Capricorn** (23.5°S)
  - **Arctic Circle** (66.5°N)
  - **Antarctic Circle** (66.5°S)

**Longitude Lines** (Meridians):
- Run **north-south** (vertical)
- Measure distance **east or west** of the Prime Meridian
- Range: 0° (Prime Meridian) to 180°E and 180°W
- Major line:
  - **Prime Meridian** (0°) - passes through Greenwich, London
  - **International Date Line** (180°)

**How to Write Coordinates**

Format: (Latitude, Longitude)

Examples:
- **Singapore**: 1.3°N, 103.8°E (or 1.3, 103.8)
- **London**: 51.5°N, 0.1°W
- **Sydney**: 33.9°S, 151.2°E
- **New York**: 40.7°N, 74.0°W

**Singapore's Location**:
- Just 1.3° north of the **Equator** (tropical climate!)
- 103.8° east of the **Prime Meridian**
- Between Malaysia (north) and Indonesia (south)
- Strategic position on major sea trade routes

**Four-Figure and Six-Figure Grid References**

Used on detailed maps (like topographic maps) for precise locations.

**Four-Figure Grid Reference**:
1. Read the **easting** (number along the bottom, left to right)
2. Read the **northing** (number along the side, bottom to top)
3. Example: Grid square **5238** means:
   - Easting: 52
   - Northing: 38

**Six-Figure Grid Reference** (more precise):
1. Divide each grid square into tenths
2. Estimate how many tenths across and up
3. Example: **523384** means:
   - Easting: 52 + 3 tenths = 52.3
   - Northing: 38 + 4 tenths = 38.4

**Use in Singapore**:
- Emergency services use precise coordinates
- Orienteering competitions use grid references
- Military and police use six-figure references

**Understanding Map Scale**

**Map scale** shows the relationship between distance on a map and actual distance on the ground.

**Three Ways to Show Scale**

**1. Ratio/Representative Fraction (RF)**

Format: 1:X or 1/X

Examples:
- **1:50,000** means 1 cm on the map = 50,000 cm (500m) in reality
- **1:100,000** means 1 cm on the map = 100,000 cm (1 km) in reality

**Small-scale maps** (e.g., 1:1,000,000):
- Show large areas (whole countries, continents)
- Less detail
- Good for general reference

**Large-scale maps** (e.g., 1:10,000):
- Show small areas (neighborhoods, towns)
- More detail
- Good for navigation and planning

**2. Linear/Bar Scale**

A visual ruler showing actual distances

**Advantage**: Still accurate even if map is photocopied or resized

**3. Statement Scale**

Written description:
- "1 centimeter equals 5 kilometers"
- "1 inch equals 1 mile"

**Calculating Distances Using Scale**

**Example 1**: Using 1:50,000 scale
- Measure map distance: 4 cm
- Calculate: 4 cm × 50,000 = 200,000 cm = 2 km

**Example 2**: Using statement scale (1 cm = 2 km)
- Measure map distance: 3.5 cm
- Calculate: 3.5 cm × 2 km = 7 km

**Singapore Example**:
On a 1:50,000 map of Singapore:
- Distance from City Hall MRT to Changi Airport: ~8 cm on map
- Real distance: 8 cm × 50,000 = 400,000 cm = 4 km (approximately correct!)

**Compass Directions**

**Cardinal Directions** (main directions):
- **N** - North (top)
- **S** - South (bottom)
- **E** - East (right)
- **W** - West (left)

**Intercardinal Directions** (in-between):
- **NE** - Northeast
- **SE** - Southeast
- **SW** - Southwest
- **NW** - Northwest

**Using a Compass Rose**:
1. Find the compass rose on the map
2. Align north with the top of the map
3. Determine the direction between two points

**Example**:
- Jurong is **west** of the city center
- Changi Airport is **east** of the city center
- Malaysia is **north** of Singapore

**Bearing** (precise direction):
- Measured in degrees (0°-360°)
- 0° (or 360°) = North
- 90° = East
- 180° = South
- 270° = West

**Practical Applications in Singapore**

**1. Using Google Maps**:
- Shows your exact coordinates (tap on location)
- Measures distances between points
- Provides turn-by-turn directions with compass bearings

**2. Emergency Services**:
- Police/ambulance use GPS coordinates for precise locations
- Especially important in large parks or nature reserves

**3. National Parks**:
- Trail maps use grid references
- MacRitchie Reservoir, Bukit Timah Nature Reserve maps show coordinates

**4. Urban Planning**:
- URA Master Plan uses coordinate systems
- Developers use precise coordinates for land plots

**Map Reading Skills Summary**

To read a map effectively:
1. Check the **title** (what does it show?)
2. Read the **legend** (understand symbols)
3. Note the **scale** (how to measure distances)
4. Use the **compass rose** (find directions)
5. Use **grid references** (locate specific points)
6. Consider **coordinates** (global positioning)

**Practice**: Next time you use Google Maps, try to:
- Find your current coordinates
- Identify which direction you're facing
- Calculate distance to your destination
- Use the scale bar to estimate walking time""",
    "content_zh": """**理解坐标**

坐标帮助我们使用网格系统在地图或地球仪上精确定位位置。

**全球网格系统**

**纬线**（平行线）：
- 沿**东西方向**（水平）
- 测量距**赤道的南北距离**
- 范围：0°（赤道）到90°N（北极）和90°S（南极）
- 主要线条：
  - **赤道**（0°）- 将地球分为北半球和南半球
  - **北回归线**（23.5°N）
  - **南回归线**（23.5°S）
  - **北极圈**（66.5°N）
  - **南极圈**（66.5°S）

**经线**（子午线）：
- 沿**南北方向**（垂直）
- 测量距**本初子午线的东西距离**
- 范围：0°（本初子午线）到180°E和180°W
- 主要线条：
  - **本初子午线**（0°）- 穿过伦敦格林威治
  - **国际日期变更线**（180°）

**如何书写坐标**

格式：（纬度，经度）

例子：
- **新加坡**：1.3°N，103.8°E（或1.3，103.8）
- **伦敦**：51.5°N，0.1°W
- **悉尼**：33.9°S，151.2°E
- **纽约**：40.7°N，74.0°W

**新加坡的位置**：
- 距**赤道**仅1.3°（热带气候！）
- 距**本初子午线**东103.8°
- 位于马来西亚（北）和印度尼西亚（南）之间
- 主要海上贸易路线的战略位置

**四位和六位网格参考**

用于详细地图（如地形图）的精确位置。

**四位网格参考**：
1. 读取**东向**（底部的数字，从左到右）
2. 读取**北向**（侧面的数字，从下到上）
3. 例子：网格方格**5238**表示：
   - 东向：52
   - 北向：38

**六位网格参考**（更精确）：
1. 将每个网格方格分成十份
2. 估计横向和纵向的十分之几
3. 例子：**523384**表示：
   - 东向：52 + 3/10 = 52.3
   - 北向：38 + 4/10 = 38.4

**在新加坡的使用**：
- 紧急服务使用精确坐标
- 定向越野比赛使用网格参考
- 军队和警察使用六位参考

**理解地图比例尺**

**地图比例尺**显示地图上的距离与地面实际距离之间的关系。

**三种显示比例尺的方式**

**1. 比率/代表性分数（RF）**

格式：1:X或1/X

例子：
- **1:50,000**表示地图上1厘米 = 实际50,000厘米（500米）
- **1:100,000**表示地图上1厘米 = 实际100,000厘米（1公里）

**小比例尺地图**（例如1:1,000,000）：
- 显示大区域（整个国家、大陆）
- 细节较少
- 适合一般参考

**大比例尺地图**（例如1:10,000）：
- 显示小区域（社区、城镇）
- 细节更多
- 适合导航和规划

**2. 线性/条形比例尺**

显示实际距离的视觉标尺

**优点**：即使地图被复印或调整大小，仍然准确

**3. 陈述比例尺**

书面描述：
- "1厘米等于5公里"
- "1英寸等于1英里"

**使用比例尺计算距离**

**例子1**：使用1:50,000比例尺
- 测量地图距离：4厘米
- 计算：4厘米 × 50,000 = 200,000厘米 = 2公里

**例子2**：使用陈述比例尺（1厘米 = 2公里）
- 测量地图距离：3.5厘米
- 计算：3.5厘米 × 2公里 = 7公里

**新加坡例子**：
在1:50,000的新加坡地图上：
- 从政府大厦地铁到樟宜机场的距离：地图上约8厘米
- 实际距离：8厘米 × 50,000 = 400,000厘米 = 4公里（大约正确！）

**罗盘方向**

**基本方向**（主要方向）：
- **N** - 北（顶部）
- **S** - 南（底部）
- **E** - 东（右侧）
- **W** - 西（左侧）

**中间方向**（之间）：
- **NE** - 东北
- **SE** - 东南
- **SW** - 西南
- **NW** - 西北

**使用罗盘玫瑰**：
1. 在地图上找到罗盘玫瑰
2. 将北方与地图顶部对齐
3. 确定两点之间的方向

**例子**：
- 裕廊在市中心**西部**
- 樟宜机场在市中心**东部**
- 马来西亚在新加坡**北部**

**方位**（精确方向）：
- 以度数测量（0°-360°）
- 0°（或360°）= 北
- 90° = 东
- 180° = 南
- 270° = 西

**新加坡的实际应用**

**1. 使用谷歌地图**：
- 显示您的确切坐标（点击位置）
- 测量点之间的距离
- 提供带罗盘方位的逐步方向

**2. 紧急服务**：
- 警察/救护车使用GPS坐标精确定位
- 在大型公园或自然保护区尤其重要

**3. 国家公园**：
- 步道地图使用网格参考
- 麦里芝水库、武吉知马自然保护区地图显示坐标

**4. 城市规划**：
- URA总体规划使用坐标系统
- 开发商使用精确坐标进行土地规划

**地图阅读技能总结**

有效阅读地图：
1. 检查**标题**（显示什么？）
2. 阅读**图例**（理解符号）
3. 注意**比例尺**（如何测量距离）
4. 使用**罗盘玫瑰**（找方向）
5. 使用**网格参考**（定位特定点）
6. 考虑**坐标**（全球定位）

**练习**：下次使用谷歌地图时，尝试：
- 找到您当前的坐标
- 识别您面向的方向
- 计算到目的地的距离
- 使用比例尺估计步行时间"""
}

humanities["chapters"][3]["sections"].append(ch4_section2)
print("✅ Added Chapter 4 Section 2: Coordinates and Map Scale")

# Save progress
with open("chapters/sec1_humanities_chapters.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved. Now adding final Section 3...")
