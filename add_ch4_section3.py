import json

# Load file
with open("chapters/sec1_humanities_chapters.json", "r", encoding="utf-8") as f:
    data = json.load(f)

humanities = data["subjects"][0]

# Chapter 4 Section 3: Reading and Interpreting Maps
ch4_section3 = {
    "id": "reading-interpreting-maps",
    "type": "text",
    "title": "Reading and Interpreting Maps",
    "title_zh": "阅读和解释地图",
    "content": """**How to Read and Interpret Maps Effectively**

Map reading is an essential skill for understanding geography, navigating, and making informed decisions.

**Step-by-Step Guide to Reading Maps**

**Step 1: Identify the Map Title**

The title tells you:
- What area is shown (Singapore, Southeast Asia, World)
- What theme is presented (physical, political, climate)
- Time period (if historical map)

Example: "Political Map of Southeast Asia, 2024"

**Step 2: Check the Legend/Key**

The legend explains all symbols, colors, and patterns:

**Common Symbols**:
- ★ Capital city
- ● Major city
- ○ Town
- ✈ Airport
- ⛰ Mountain peak
- ~ River
- === Highway/expressway
- --- Road
- -·-·- International boundary

**Color Meanings**:
- **Blue** - Water (oceans, rivers, lakes)
- **Green** - Low elevation, forests, parks
- **Brown/Yellow** - Higher elevation, mountains
- **Red** - Major roads, important features
- **Purple** - Special features (military, restricted areas)

**Step 3: Note the Scale**

Understand how to measure real-world distances:
- Use a ruler to measure map distance
- Apply the scale to calculate actual distance
- Remember: Small-scale = large area, less detail

**Step 4: Orient with the Compass Rose**

- Find north (usually at top)
- Determine directions between locations
- Understand relative positions

**Step 5: Use Grid References**

- Identify eastings (horizontal) and northings (vertical)
- Locate specific features using coordinates
- Cross-reference with index if available

**Interpreting Different Map Types**

**Physical Maps - What to Look For**:

1. **Elevation Patterns**:
   - Green/yellow = lowlands (good for agriculture, settlements)
   - Brown/dark brown = highlands (less populated, tourism, forestry)
   - Flat areas = plains (farming, cities)

2. **Water Features**:
   - Rivers: Transportation routes, water supply, settlement locations
   - Coastlines: Ports, trade, fishing industries
   - Lakes/reservoirs: Water storage, recreation

3. **Climate Clues**:
   - Distance from equator (latitude)
   - Proximity to water bodies
   - Mountain ranges (create rain shadows)

**Singapore Physical Map Example**:
- Very flat terrain (highest point only 163m)
- Numerous reservoirs (water security)
- Coastal island with many smaller islands
- Mangrove areas in northwest (Sungei Buloh)

**Political Maps - What to Look For**:

1. **Boundaries**:
   - International borders (thick lines)
   - State/regional borders (thin lines)
   - Administrative divisions

2. **Cities**:
   - Capital cities (starred)
   - Population centers (circle size indicates population)
   - Urban vs. rural areas

3. **Names**:
   - Country names (ALL CAPS)
   - City names (Regular case)
   - Water body names (Italics)

**Singapore Political Map Example**:
- City-state (no internal political divisions)
- 5 regions for planning (not administrative)
- Neighboring countries: Malaysia (Johor), Indonesia (Riau Islands)
- Closest major cities: Johor Bahru, Batam

**Thematic Maps - What to Look For**:

**Population Density Map**:
- Dark colors = high density (many people per km²)
- Light colors = low density
- Patterns: Urban vs. rural, coastal vs. inland

**Singapore**: Very high density (8,000+ people per km²), concentrated in HDB estates

**Climate Map**:
- Color zones represent different climates
- Look for patterns related to latitude, altitude, proximity to water

**Singapore**: Tropical rainforest climate (all year hot and wet)

**Economic/Resource Map**:
- Symbols show industries, crops, minerals
- Understand economic activities by region

**Singapore**: Service economy (finance, trade, tourism), limited natural resources

**Analyzing Maps: Key Questions**

**Location Questions**:
- Where is this place?
- What are its coordinates?
- What is it near? (relative location)

**Place Questions**:
- What are its physical features?
- What is the climate?
- What makes it unique?

**Region Questions**:
- What region is it part of? (Southeast Asia, tropics)
- What do places in this region have in common?
- How is it different from other regions?

**Movement Questions**:
- How do people/goods move through this area?
- What transportation routes exist?
- What barriers to movement are there?

**Human-Environment Interaction Questions**:
- How have humans adapted to this environment?
- How have humans modified this environment?
- What environmental challenges exist?

**Practical Map Reading Skills**

**1. Finding Your Location on a Map**:
- Identify landmarks around you
- Match landmarks to map symbols
- Use compass or GPS for orientation
- Cross-reference street names

**2. Planning a Route**:
- Identify start and end points
- Find the shortest or fastest route
- Note landmarks along the way
- Estimate distance using scale
- Consider terrain (hills, rivers to cross)

**3. Understanding Contour Lines** (Topographic Maps):

Contour lines show elevation:
- Each line represents specific height (e.g., 10m intervals)
- Lines close together = steep slope
- Lines far apart = gentle slope
- Concentric circles = hill or mountain
- Contour lines never cross (except cliffs)

**Reading Slope**:
```
Gentle slope: ________________
              ________________
              ________________

Steep slope:  |||||||||||||||
              |||||||||||||||
              |||||||||||||||
```

**4. Measuring Distance**:

Method 1: Straight line
- Use ruler on map
- Apply scale
- Calculate

Method 2: Curved route (like roads)
- Use string or paper strip
- Follow the route
- Straighten and measure
- Apply scale

**Common Map Reading Mistakes**

**Mistake 1**: Ignoring the scale
- Fix: Always check scale before estimating distances

**Mistake 2**: Confusing north with "up"
- Fix: Always use compass rose, not map orientation

**Mistake 3**: Misreading symbols
- Fix: Always refer to the legend

**Mistake 4**: Ignoring contour lines
- Fix: Use contours to understand terrain difficulty

**Mistake 5**: Not updating maps
- Fix: Check publication date, use current maps for navigation

**Modern Map Tools**

**Google Maps Features**:
1. **Satellite View**: See actual aerial photos
2. **Street View**: 360° ground-level photos
3. **Terrain View**: Shows elevation and landforms
4. **Traffic View**: Real-time traffic conditions
5. **Transit View**: Public transport routes

**Using GPS with Maps**:
- Shows your exact position
- Tracks movement in real-time
- Provides turn-by-turn navigation
- Works with topographic maps for hiking

**Singapore Map Reading Applications**

**1. MRT System Map**:
- Not geographically accurate (schematic)
- Shows connections, not exact locations
- Read by following colored lines
- Transfer stations have multiple colors

**2. HDB Estate Maps**:
- Show block numbers, facilities
- Help locate specific addresses
- Usually include void deck locations

**3. Park Connector Maps**:
- Show cycling/walking routes
- Link parks and green spaces
- Include distances and estimated times

**4. Heritage Trail Maps**:
- Highlight historical sites
- Numbered routes to follow
- Include brief descriptions

**5. OneMap Singapore**:
- Official government mapping service
- Combines physical, political, and thematic data
- Interactive layers (planning areas, flood zones, heritage sites)
- Useful for students, researchers, planners

**Practice Exercise: Analyzing a Map of Singapore**

Given a map of Singapore, you should be able to:

1. **Identify**:
   - Title and type of map
   - Scale (1:X,XXX)
   - Key landmarks (Marina Bay, Changi Airport, Sentosa)

2. **Locate**:
   - Your school using address
   - Nearest MRT station
   - Neighboring countries

3. **Measure**:
   - Distance from east to west (approx. 50 km)
   - Distance from north to south (approx. 27 km)
   - Distance from your home to school

4. **Describe**:
   - Singapore's position (1°N of equator, 103°E)
   - Physical features (flat, coastal, many islands)
   - Major regions (Central, East, West, North, Northeast)

5. **Explain**:
   - Why Singapore's location is strategic for trade
   - How land reclamation has changed the coastline
   - Why water reservoirs are important (limited freshwater)

**Conclusion**

Effective map reading combines:
- Technical skills (scale, coordinates, symbols)
- Analytical thinking (patterns, relationships, significance)
- Practical application (navigation, planning, decision-making)

Regular practice with different map types will improve your geographic literacy and spatial awareness!""",
    "content_zh": """**如何有效阅读和解释地图**

地图阅读是理解地理、导航和做出明智决策的基本技能。

**阅读地图的分步指南**

**步骤1：识别地图标题**

标题告诉您：
- 显示什么区域（新加坡、东南亚、世界）
- 呈现什么主题（自然、政治、气候）
- 时间段（如果是历史地图）

例子："2024年东南亚政治地图"

**步骤2：检查图例/图标**

图例解释所有符号、颜色和图案：

**常见符号**：
- ★ 首都
- ● 主要城市
- ○ 城镇
- ✈ 机场
- ⛰ 山峰
- ~ 河流
- === 高速公路/快速路
- --- 道路
- -·-·- 国际边界

**颜色含义**：
- **蓝色** - 水（海洋、河流、湖泊）
- **绿色** - 低海拔、森林、公园
- **棕色/黄色** - 较高海拔、山脉
- **红色** - 主要道路、重要特征
- **紫色** - 特殊特征（军事、限制区域）

**步骤3：注意比例尺**

了解如何测量真实世界的距离：
- 使用尺子测量地图距离
- 应用比例尺计算实际距离
- 记住：小比例尺 = 大区域，细节较少

**步骤4：使用罗盘玫瑰定向**

- 找到北方（通常在顶部）
- 确定位置之间的方向
- 理解相对位置

**步骤5：使用网格参考**

- 识别东向（水平）和北向（垂直）
- 使用坐标定位特定特征
- 如有索引，交叉参考

**解释不同类型的地图**

**自然地图 - 要寻找什么**：

1. **海拔模式**：
   - 绿色/黄色 = 低地（适合农业、定居点）
   - 棕色/深棕色 = 高地（人口较少、旅游、林业）
   - 平坦区域 = 平原（农业、城市）

2. **水特征**：
   - 河流：运输路线、供水、定居点位置
   - 海岸线：港口、贸易、渔业
   - 湖泊/水库：蓄水、娱乐

3. **气候线索**：
   - 距赤道的距离（纬度）
   - 靠近水体
   - 山脉（造成雨影）

**新加坡自然地图例子**：
- 非常平坦的地形（最高点仅163米）
- 众多水库（水安全）
- 沿海岛屿，有许多小岛
- 西北部的红树林地区（双溪布洛）

**政治地图 - 要寻找什么**：

1. **边界**：
   - 国际边界（粗线）
   - 州/地区边界（细线）
   - 行政区划

2. **城市**：
   - 首都（带星号）
   - 人口中心（圆圈大小表示人口）
   - 城市与农村地区

3. **名称**：
   - 国家名称（全大写）
   - 城市名称（常规大小写）
   - 水体名称（斜体）

**新加坡政治地图例子**：
- 城市国家（无内部政治区划）
- 5个规划区域（非行政区）
- 邻国：马来西亚（柔佛）、印度尼西亚（廖内群岛）
- 最近的主要城市：新山、巴淡岛

**主题地图 - 要寻找什么**：

**人口密度地图**：
- 深色 = 高密度（每平方公里人数多）
- 浅色 = 低密度
- 模式：城市与农村、沿海与内陆

**新加坡**：非常高密度（8,000+人/平方公里），集中在组屋区

**气候地图**：
- 颜色区域代表不同气候
- 寻找与纬度、海拔、靠近水的模式

**新加坡**：热带雨林气候（全年炎热潮湿）

**经济/资源地图**：
- 符号显示工业、作物、矿物
- 按地区了解经济活动

**新加坡**：服务经济（金融、贸易、旅游），自然资源有限

**分析地图：关键问题**

**位置问题**：
- 这个地方在哪里？
- 它的坐标是什么？
- 它靠近什么？（相对位置）

**地点问题**：
- 它的物理特征是什么？
- 气候如何？
- 什么使它独特？

**区域问题**：
- 它属于什么区域？（东南亚、热带）
- 该区域的地方有什么共同点？
- 它与其他区域有何不同？

**移动问题**：
- 人/货物如何通过这个区域移动？
- 存在什么运输路线？
- 有什么移动障碍？

**人与环境互动问题**：
- 人类如何适应这个环境？
- 人类如何改造这个环境？
- 存在什么环境挑战？

**实用地图阅读技能**

**1. 在地图上找到您的位置**：
- 识别周围的地标
- 将地标与地图符号匹配
- 使用罗盘或GPS定向
- 交叉参考街道名称

**2. 规划路线**：
- 识别起点和终点
- 找到最短或最快路线
- 注意沿途地标
- 使用比例尺估计距离
- 考虑地形（山丘、需要穿越的河流）

**3. 理解等高线**（地形图）：

等高线显示海拔：
- 每条线代表特定高度（例如10米间隔）
- 线条紧密 = 陡坡
- 线条稀疏 = 缓坡
- 同心圆 = 山丘或山峰
- 等高线永远不会交叉（悬崖除外）

**4. 测量距离**：

方法1：直线
- 在地图上使用尺子
- 应用比例尺
- 计算

方法2：曲线路线（如道路）
- 使用线或纸条
- 跟随路线
- 拉直并测量
- 应用比例尺

**常见地图阅读错误**

**错误1**：忽略比例尺
- 修复：在估计距离之前始终检查比例尺

**错误2**：将北方与"上"混淆
- 修复：始终使用罗盘玫瑰，而非地图方向

**错误3**：误读符号
- 修复：始终参考图例

**错误4**：忽略等高线
- 修复：使用等高线理解地形难度

**错误5**：不更新地图
- 修复：检查出版日期，使用当前地图导航

**现代地图工具**

**谷歌地图功能**：
1. **卫星视图**：查看实际航空照片
2. **街景**：360°地面照片
3. **地形视图**：显示海拔和地形
4. **交通视图**：实时交通状况
5. **公交视图**：公共交通路线

**使用GPS和地图**：
- 显示您的确切位置
- 实时跟踪移动
- 提供逐步导航
- 适用于徒步旅行的地形图

**新加坡地图阅读应用**

**1. 地铁系统地图**：
- 不是地理精确的（示意图）
- 显示连接，而非确切位置
- 通过跟随彩色线条阅读
- 换乘站有多种颜色

**2. 组屋区地图**：
- 显示组屋号码、设施
- 帮助定位特定地址
- 通常包括底层空地位置

**3. 公园连道地图**：
- 显示骑行/步行路线
- 连接公园和绿色空间
- 包括距离和预计时间

**4. 遗产小径地图**：
- 突出历史遗址
- 编号路线跟随
- 包括简要描述

**5. OneMap新加坡**：
- 官方政府地图服务
- 结合自然、政治和主题数据
- 交互式图层（规划区、洪水区、遗产遗址）
- 对学生、研究人员、规划者有用

**练习：分析新加坡地图**

给定新加坡地图，您应该能够：

1. **识别**：
   - 标题和地图类型
   - 比例尺（1:X,XXX）
   - 关键地标（滨海湾、樟宜机场、圣淘沙）

2. **定位**：
   - 使用地址找到您的学校
   - 最近的地铁站
   - 邻国

3. **测量**：
   - 从东到西的距离（约50公里）
   - 从北到南的距离（约27公里）
   - 从您家到学校的距离

4. **描述**：
   - 新加坡的位置（赤道以北1°，东经103°）
   - 物理特征（平坦、沿海、许多岛屿）
   - 主要区域（中部、东部、西部、北部、东北部）

5. **解释**：
   - 为什么新加坡的位置对贸易至关重要
   - 填海造陆如何改变了海岸线
   - 为什么水库很重要（淡水有限）

**结论**

有效的地图阅读结合：
- 技术技能（比例尺、坐标、符号）
- 分析思维（模式、关系、意义）
- 实际应用（导航、规划、决策）

定期练习不同类型的地图将提高您的地理素养和空间意识！"""
}

humanities["chapters"][3]["sections"].append(ch4_section3)
print("✅ Added Chapter 4 Section 3: Reading and Interpreting Maps")

# Save final version
with open("chapters/sec1_humanities_chapters.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n" + "="*60)
print("🎉 ALL HUMANITIES LESSON CONTENT IS NOW COMPLETE! 🎉")
print("="*60)
print("\n📊 Final Summary:")
print("  ✅ Chapter 1 (Understanding History): 3 sections, 15 exercises")
print("  ✅ Chapter 2 (Early Southeast Asia): 3 sections, 15 exercises")
print("  ✅ Chapter 3 (Physical Geography): 3 sections, 15 exercises")
print("  ✅ Chapter 4 (Map Skills): 3 sections, 15 exercises")
print("\n📚 Total: 4 chapters, 12 sections, 60 exercises")
print("\nNext step: Run integrate_humanities.py to update content.json")
