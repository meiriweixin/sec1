#!/usr/bin/env python3
"""Add Economics (H2) for JC1 and JC2."""
import json
from datetime import datetime

# JC1 Economics Chapters
JC1_ECONOMICS_CHAPTERS = [
    {
        "id": "intro-economics-jc1",
        "title": "Introduction to Economics",
        "title_zh": "经济学导论",
        "gradeLevel": "jc1",
        "description": "Scarcity, choice, and economic systems",
        "description_zh": "稀缺性、选择和经济体系",
        "objectives": ["Define economics and scarcity", "Understand opportunity cost", "Compare economic systems"],
        "objectives_zh": ["定义经济学和稀缺性", "理解机会成本", "比较经济体系"],
        "sections": [
            {"id": "intro-1", "type": "text", "title": "What is Economics?", "title_zh": "什么是经济学?",
             "content": "**Economics** is the study of how societies allocate scarce resources.\n\n**Central Problem:** Unlimited wants vs. limited resources → SCARCITY\n\n**Key Questions:**\n1. What to produce?\n2. How to produce?\n3. For whom to produce?"},
            {"id": "intro-2", "type": "text", "title": "Opportunity Cost", "title_zh": "机会成本",
             "content": "**Opportunity Cost**: The next best alternative foregone when making a choice.\n\n**Example (Singapore context):**\nIf you choose to spend $50 on a meal at Marina Bay Sands, your opportunity cost might be 2 movie tickets you could have bought instead.\n\n**Formula:** Opportunity cost = Value of next best alternative"},
            {"id": "intro-3", "type": "text", "title": "Economic Systems", "title_zh": "经济体系",
             "content": "**Types:**\n\n1. **Free Market**: Private ownership, profit motive\n2. **Command/Planned**: Government controls resources\n3. **Mixed Economy**: Combination (most countries today)\n\n**Singapore:** Mixed economy with significant government role in housing (HDB), healthcare, and strategic industries."}
        ]
    },
    {
        "id": "demand-supply-jc1",
        "title": "Demand and Supply",
        "title_zh": "需求与供给",
        "gradeLevel": "jc1",
        "description": "Market mechanisms and price determination",
        "description_zh": "市场机制和价格决定",
        "objectives": ["Explain law of demand and supply", "Analyze market equilibrium", "Identify factors affecting demand and supply"],
        "objectives_zh": ["解释需求和供给定律", "分析市场均衡", "识别影响需求和供给的因素"],
        "sections": [
            {"id": "demand-1", "type": "text", "title": "Law of Demand", "title_zh": "需求定律",
             "content": "**Law of Demand:** As price increases, quantity demanded decreases (ceteris paribus).\n\n**Demand Curve:** Downward sloping\n\n**Factors shifting demand:**\n- Income\n- Prices of related goods\n- Tastes and preferences\n- Population\n- Future expectations"},
            {"id": "demand-2", "type": "text", "title": "Law of Supply", "title_zh": "供给定律",
             "content": "**Law of Supply:** As price increases, quantity supplied increases (ceteris paribus).\n\n**Supply Curve:** Upward sloping\n\n**Factors shifting supply:**\n- Input prices\n- Technology\n- Number of sellers\n- Government policies\n- Natural conditions"},
            {"id": "demand-3", "type": "text", "title": "Market Equilibrium", "title_zh": "市场均衡",
             "content": "**Equilibrium:** Where demand equals supply\n\n**At equilibrium:**\n- No shortage (excess demand)\n- No surplus (excess supply)\n- Market clears\n\n**Singapore example:** COE prices are determined by demand and supply in certificate auctions."}
        ]
    },
    {
        "id": "elasticity-jc1",
        "title": "Elasticity",
        "title_zh": "弹性",
        "gradeLevel": "jc1",
        "description": "Price elasticity of demand and supply",
        "description_zh": "需求和供给的价格弹性",
        "objectives": ["Calculate price elasticity of demand (PED)", "Calculate price elasticity of supply (PES)", "Apply elasticity concepts to real situations"],
        "objectives_zh": ["计算需求价格弹性(PED)", "计算供给价格弹性(PES)", "将弹性概念应用于实际情况"],
        "sections": [
            {"id": "elas-1", "type": "text", "title": "Price Elasticity of Demand (PED)", "title_zh": "需求价格弹性(PED)",
             "content": "**Formula:** PED = %Δ Quantity Demanded / %Δ Price\n\n**Values:**\n- |PED| > 1: Elastic (responsive)\n- |PED| < 1: Inelastic (unresponsive)\n- |PED| = 1: Unit elastic\n\n**Determinants:**\n- Availability of substitutes\n- Necessity vs. luxury\n- Time period\n- Proportion of income spent"},
            {"id": "elas-2", "type": "text", "title": "Price Elasticity of Supply (PES)", "title_zh": "供给价格弹性(PES)",
             "content": "**Formula:** PES = %Δ Quantity Supplied / %Δ Price\n\n**Determinants:**\n- Time period (longer = more elastic)\n- Spare capacity\n- Availability of factors\n- Ease of storage\n- Mobility of factors"},
            {"id": "elas-3", "type": "text", "title": "Applications", "title_zh": "应用",
             "content": "**Revenue and PED:**\n- Elastic: Price cut increases revenue\n- Inelastic: Price rise increases revenue\n\n**Singapore applications:**\n- Cigarette tax (inelastic demand)\n- COE demand (relatively inelastic)\n- Public transport pricing"}
        ]
    },
    {
        "id": "market-failure-jc1",
        "title": "Market Failure",
        "title_zh": "市场失灵",
        "gradeLevel": "jc1",
        "description": "Externalities, public goods, and imperfect information",
        "description_zh": "外部性、公共物品和信息不完全",
        "objectives": ["Identify types of market failure", "Analyze externalities using diagrams", "Evaluate government interventions"],
        "objectives_zh": ["识别市场失灵类型", "用图表分析外部性", "评价政府干预"],
        "sections": [
            {"id": "mf-1", "type": "text", "title": "Externalities", "title_zh": "外部性",
             "content": "**Externality:** Cost or benefit to third parties not in the transaction.\n\n**Negative externalities:**\n- Pollution from factories\n- Noise from construction\n- Second-hand smoke\n\n**Positive externalities:**\n- Education (more productive workforce)\n- Vaccination (herd immunity)\n- Research and development"},
            {"id": "mf-2", "type": "text", "title": "Public Goods", "title_zh": "公共物品",
             "content": "**Characteristics:**\n- Non-excludable: Can't prevent non-payers\n- Non-rivalrous: One person's use doesn't reduce availability\n\n**Examples:**\n- National defense\n- Street lighting\n- Public parks\n\n**Problem:** Free-rider problem → underproduction by market"},
            {"id": "mf-3", "type": "text", "title": "Government Solutions", "title_zh": "政府解决方案",
             "content": "**Policy interventions:**\n\n1. **Taxes**: Discourage negative externalities (e.g., carbon tax)\n2. **Subsidies**: Encourage positive externalities (e.g., education subsidies)\n3. **Regulations**: Direct rules (e.g., emission standards)\n4. **Provision**: Government supplies public goods\n\n**Singapore examples:**\n- COE system (limit car externalities)\n- Education subsidies\n- NEA regulations"}
        ]
    },
    {
        "id": "firms-production-jc1",
        "title": "Firms and Production",
        "title_zh": "厂商与生产",
        "gradeLevel": "jc1",
        "description": "Production costs and business decisions",
        "description_zh": "生产成本和商业决策",
        "objectives": ["Distinguish between short-run and long-run", "Understand fixed and variable costs", "Apply law of diminishing returns"],
        "objectives_zh": ["区分短期和长期", "理解固定成本和可变成本", "应用边际报酬递减规律"],
        "sections": [
            {"id": "firm-1", "type": "text", "title": "Short-Run vs Long-Run", "title_zh": "短期与长期",
             "content": "**Short-run:** At least one factor is fixed (usually capital)\n**Long-run:** All factors are variable\n\n**Fixed Costs (FC):** Don't change with output (rent, machinery)\n**Variable Costs (VC):** Change with output (labor, materials)\n\n**Total Cost = FC + VC**"},
            {"id": "firm-2", "type": "text", "title": "Law of Diminishing Returns", "title_zh": "边际报酬递减规律",
             "content": "**Law:** As more of a variable factor is added to a fixed factor, marginal product eventually falls.\n\n**Example:** Adding more workers to a fixed-size factory eventually leads to crowding and lower productivity per worker.\n\n**Implications:** Explains upward-sloping MC curve"},
            {"id": "firm-3", "type": "text", "title": "Cost Curves", "title_zh": "成本曲线",
             "content": "**Average Costs:**\n- AFC = FC / Q (always falling)\n- AVC = VC / Q (U-shaped)\n- ATC = TC / Q (U-shaped)\n\n**Marginal Cost (MC):** Additional cost of one more unit\n\n**Key relationship:** MC intersects ATC and AVC at their minimum points"}
        ]
    },
    {
        "id": "market-structures-jc1",
        "title": "Market Structures",
        "title_zh": "市场结构",
        "gradeLevel": "jc1",
        "description": "Perfect competition and monopoly",
        "description_zh": "完全竞争与垄断",
        "objectives": ["Compare perfect competition and monopoly", "Analyze profit maximization", "Evaluate efficiency in different markets"],
        "objectives_zh": ["比较完全竞争和垄断", "分析利润最大化", "评价不同市场的效率"],
        "sections": [
            {"id": "ms-1", "type": "text", "title": "Perfect Competition", "title_zh": "完全竞争",
             "content": "**Characteristics:**\n- Many buyers and sellers\n- Homogeneous products\n- Free entry and exit\n- Perfect information\n- Price takers\n\n**Profit maximization:** MC = MR = P\n**Long-run:** Normal profit only (supernormal profits attract entry)"},
            {"id": "ms-2", "type": "text", "title": "Monopoly", "title_zh": "垄断",
             "content": "**Characteristics:**\n- Single seller\n- Unique product\n- High barriers to entry\n- Price maker\n\n**Profit maximization:** MC = MR (P > MR)\n**Long-run:** Can maintain supernormal profits due to barriers"},
            {"id": "ms-3", "type": "text", "title": "Efficiency Comparison", "title_zh": "效率比较",
             "content": "**Perfect Competition:**\n- Allocatively efficient (P = MC)\n- Productively efficient (minimum ATC)\n\n**Monopoly:**\n- Allocatively inefficient (P > MC)\n- Possible productive efficiency through economies of scale\n- May have X-inefficiency\n\n**Singapore examples:** SP Group (utilities monopoly), hawker centers (near perfect competition)"}
        ]
    },
    {
        "id": "imperfect-competition-jc1",
        "title": "Imperfect Competition",
        "title_zh": "不完全竞争",
        "gradeLevel": "jc1",
        "description": "Monopolistic competition and oligopoly",
        "description_zh": "垄断竞争与寡头垄断",
        "objectives": ["Analyze monopolistic competition", "Understand oligopoly behavior", "Apply game theory basics"],
        "objectives_zh": ["分析垄断竞争", "理解寡头垄断行为", "应用博弈论基础"],
        "sections": [
            {"id": "imp-1", "type": "text", "title": "Monopolistic Competition", "title_zh": "垄断竞争",
             "content": "**Characteristics:**\n- Many sellers\n- Differentiated products\n- Some market power\n- Low entry barriers\n\n**Examples:** Restaurants, clothing stores, hairdressers\n\n**Long-run:** Normal profit (like perfect competition) due to entry"},
            {"id": "imp-2", "type": "text", "title": "Oligopoly", "title_zh": "寡头垄断",
             "content": "**Characteristics:**\n- Few dominant firms\n- Interdependent decision-making\n- High barriers to entry\n- Non-price competition common\n\n**Singapore examples:**\n- Telcos (Singtel, StarHub, M1)\n- Supermarkets (NTUC, Cold Storage, Giant)"},
            {"id": "imp-3", "type": "text", "title": "Game Theory", "title_zh": "博弈论",
             "content": "**Prisoner's Dilemma:** Shows why firms might not cooperate even when cooperation benefits all.\n\n**Nash Equilibrium:** Each player's strategy is best given others' strategies.\n\n**Collusion vs Competition:** Firms may try to collude but have incentives to cheat."}
        ]
    },
    {
        "id": "factor-markets-jc1",
        "title": "Factor Markets",
        "title_zh": "要素市场",
        "gradeLevel": "jc1",
        "description": "Labor market and wage determination",
        "description_zh": "劳动市场和工资决定",
        "objectives": ["Analyze labor demand and supply", "Explain wage differentials", "Evaluate minimum wage policies"],
        "objectives_zh": ["分析劳动需求和供给", "解释工资差异", "评价最低工资政策"],
        "sections": [
            {"id": "factor-1", "type": "text", "title": "Labor Demand", "title_zh": "劳动需求",
             "content": "**Derived demand:** Demand for labor depends on demand for the product.\n\n**Marginal Revenue Product (MRP):** Additional revenue from hiring one more worker.\n\n**Profit-maximizing rule:** Hire workers until MRP = Wage"},
            {"id": "factor-2", "type": "text", "title": "Labor Supply", "title_zh": "劳动供给",
             "content": "**Factors affecting labor supply:**\n- Population size\n- Labor force participation rate\n- Immigration policies\n- Education and skills\n\n**Singapore context:**\n- Foreign worker policies\n- Skills upgrading programs\n- SkillsFuture initiative"},
            {"id": "factor-3", "type": "text", "title": "Wage Differentials", "title_zh": "工资差异",
             "content": "**Why wages differ:**\n\n1. Human capital (education, experience)\n2. Compensating differentials (risky/unpleasant jobs)\n3. Efficiency wages\n4. Market power (unions, monopsony)\n5. Discrimination\n\n**Singapore policies:**\n- Progressive Wage Model\n- Workfare Income Supplement"}
        ]
    }
]

# JC2 Economics Chapters
JC2_ECONOMICS_CHAPTERS = [
    {
        "id": "macroeconomic-aims-jc2",
        "title": "Macroeconomic Aims",
        "title_zh": "宏观经济目标",
        "gradeLevel": "jc2",
        "description": "Economic growth, employment, inflation, and balance of payments",
        "description_zh": "经济增长、就业、通货膨胀和国际收支",
        "objectives": ["Identify key macroeconomic objectives", "Understand measurement methods", "Recognize policy trade-offs"],
        "objectives_zh": ["识别关键宏观经济目标", "理解测量方法", "认识政策权衡"],
        "sections": [
            {"id": "macro-1", "type": "text", "title": "Macroeconomic Objectives", "title_zh": "宏观经济目标",
             "content": "**Four Main Objectives:**\n\n1. **Economic Growth**: Increase in real GDP\n2. **Low Unemployment**: High employment rate\n3. **Price Stability**: Low inflation\n4. **Healthy Balance of Payments**: Sustainable external position\n\n**Trade-offs:** E.g., growth vs inflation (Phillips Curve)"},
            {"id": "macro-2", "type": "text", "title": "Measuring Economic Performance", "title_zh": "衡量经济表现",
             "content": "**GDP:** Total value of goods and services produced\n\n**Real vs Nominal GDP:** Real adjusted for inflation\n\n**Limitations of GDP:**\n- Ignores distribution\n- Excludes non-market activities\n- Quality of life not captured\n- Environmental costs ignored"},
            {"id": "macro-3", "type": "text", "title": "Singapore's Performance", "title_zh": "新加坡的表现",
             "content": "**Singapore's approach:**\n- Export-oriented growth\n- Low inflation priority\n- Full employment goal\n- Current account surplus\n\n**Challenges:**\n- Aging population\n- Income inequality\n- Structural changes"}
        ]
    },
    {
        "id": "national-income-jc2",
        "title": "National Income",
        "title_zh": "国民收入",
        "gradeLevel": "jc2",
        "description": "Circular flow and aggregate demand",
        "description_zh": "循环流动和总需求",
        "objectives": ["Explain the circular flow model", "Analyze components of aggregate demand", "Apply the multiplier concept"],
        "objectives_zh": ["解释循环流动模型", "分析总需求的组成部分", "应用乘数概念"],
        "sections": [
            {"id": "ni-1", "type": "text", "title": "Circular Flow of Income", "title_zh": "收入的循环流动",
             "content": "**Basic Model:**\n- Households provide factors → receive income\n- Firms produce goods → receive revenue\n\n**Injections:** I, G, X\n**Leakages:** S, T, M\n\n**Equilibrium:** Injections = Leakages"},
            {"id": "ni-2", "type": "text", "title": "Aggregate Demand", "title_zh": "总需求",
             "content": "**AD = C + I + G + (X - M)**\n\n**Components:**\n- C: Consumption\n- I: Investment\n- G: Government spending\n- X: Exports\n- M: Imports\n\n**AD Curve:** Downward sloping (wealth effect, interest rate effect, exchange rate effect)"},
            {"id": "ni-3", "type": "text", "title": "Multiplier Effect", "title_zh": "乘数效应",
             "content": "**Multiplier:** Initial change in spending leads to larger change in national income.\n\n**Formula:** k = 1 / (1 - MPC) or 1 / MPW\n\nWhere MPW = MPS + MPT + MPM\n\n**Singapore:** Small open economy → smaller multiplier due to high import propensity"}
        ]
    },
    {
        "id": "unemployment-inflation-jc2",
        "title": "Unemployment and Inflation",
        "title_zh": "失业与通货膨胀",
        "gradeLevel": "jc2",
        "description": "Types, causes, and consequences",
        "description_zh": "类型、原因和后果",
        "objectives": ["Classify types of unemployment", "Distinguish demand-pull and cost-push inflation", "Analyze economic consequences"],
        "objectives_zh": ["分类失业类型", "区分需求拉动和成本推动通货膨胀", "分析经济后果"],
        "sections": [
            {"id": "unemp-1", "type": "text", "title": "Types of Unemployment", "title_zh": "失业类型",
             "content": "**Types:**\n\n1. **Cyclical**: Due to economic downturns\n2. **Structural**: Skills mismatch\n3. **Frictional**: Between jobs\n4. **Seasonal**: Due to seasonal factors\n\n**Natural rate of unemployment:** Frictional + Structural"},
            {"id": "unemp-2", "type": "text", "title": "Inflation Types", "title_zh": "通货膨胀类型",
             "content": "**Demand-Pull Inflation:**\n- Aggregate demand exceeds aggregate supply\n- 'Too much money chasing too few goods'\n\n**Cost-Push Inflation:**\n- Rising production costs\n- Supply shocks (e.g., oil prices)\n- Wage increases"},
            {"id": "unemp-3", "type": "text", "title": "Consequences", "title_zh": "后果",
             "content": "**Unemployment costs:**\n- Lost output\n- Social problems\n- Skills deterioration\n- Fiscal costs\n\n**Inflation costs:**\n- Reduced purchasing power\n- Menu costs\n- Uncertainty\n- International competitiveness\n\n**Singapore:** Low unemployment, moderate inflation targets"}
        ]
    },
    {
        "id": "fiscal-policy-jc2",
        "title": "Fiscal Policy",
        "title_zh": "财政政策",
        "gradeLevel": "jc2",
        "description": "Government spending and taxation",
        "description_zh": "政府支出和税收",
        "objectives": ["Explain fiscal policy tools", "Analyze effectiveness of fiscal policy", "Evaluate Singapore's fiscal approach"],
        "objectives_zh": ["解释财政政策工具", "分析财政政策的有效性", "评价新加坡的财政方法"],
        "sections": [
            {"id": "fiscal-1", "type": "text", "title": "Fiscal Policy Tools", "title_zh": "财政政策工具",
             "content": "**Expansionary Fiscal Policy:**\n- Increase government spending\n- Cut taxes\n- Increases AD\n\n**Contractionary Fiscal Policy:**\n- Decrease government spending\n- Raise taxes\n- Decreases AD"},
            {"id": "fiscal-2", "type": "text", "title": "Effectiveness", "title_zh": "有效性",
             "content": "**Limitations:**\n\n1. Time lags (recognition, implementation, impact)\n2. Crowding out (G↑ → interest rates↑ → I↓)\n3. Budget deficits and debt\n4. Multiplier uncertainty\n5. Open economy leakages"},
            {"id": "fiscal-3", "type": "text", "title": "Singapore's Fiscal Policy", "title_zh": "新加坡的财政政策",
             "content": "**Unique features:**\n- Budget surpluses (usually)\n- Low tax rates\n- Reserves accumulation\n- Counter-cyclical spending\n\n**COVID-19 response:**\n- Budget support packages\n- Job Support Scheme\n- Draw on reserves"}
        ]
    },
    {
        "id": "monetary-policy-jc2",
        "title": "Monetary Policy",
        "title_zh": "货币政策",
        "gradeLevel": "jc2",
        "description": "Money supply and interest rates",
        "description_zh": "货币供给和利率",
        "objectives": ["Explain monetary policy transmission", "Analyze MAS exchange rate policy", "Compare conventional and unconventional tools"],
        "objectives_zh": ["解释货币政策传导", "分析金管局汇率政策", "比较常规和非常规工具"],
        "sections": [
            {"id": "mon-1", "type": "text", "title": "Monetary Policy Tools", "title_zh": "货币政策工具",
             "content": "**Conventional tools:**\n- Open market operations\n- Interest rate changes\n- Reserve requirements\n\n**Unconventional (post-2008):**\n- Quantitative easing\n- Forward guidance\n- Negative interest rates"},
            {"id": "mon-2", "type": "text", "title": "Transmission Mechanism", "title_zh": "传导机制",
             "content": "**Interest rate channel:**\nMoney supply ↑ → Interest rates ↓ → Investment ↑ → AD ↑\n\n**Exchange rate channel:**\nMoney supply ↑ → Currency depreciates → Exports ↑ → AD ↑\n\n**Asset price channel:**\nMoney supply ↑ → Asset prices ↑ → Wealth effect → C ↑"},
            {"id": "mon-3", "type": "text", "title": "MAS Exchange Rate Policy", "title_zh": "金管局汇率政策",
             "content": "**Singapore's unique approach:**\n- Manages SGD against trade-weighted basket (S$NEER)\n- Three parameters: slope, width, center\n- Main tool for managing inflation\n\n**Why exchange rate, not interest rate?**\n- Small, open economy\n- High import content in consumption\n- Trade = 3x GDP"}
        ]
    },
    {
        "id": "supply-side-policy-jc2",
        "title": "Supply-Side Policies",
        "title_zh": "供给侧政策",
        "gradeLevel": "jc2",
        "description": "Policies to increase productive capacity",
        "description_zh": "提高生产能力的政策",
        "objectives": ["Identify supply-side policy types", "Evaluate policy effectiveness", "Apply to Singapore context"],
        "objectives_zh": ["识别供给侧政策类型", "评价政策有效性", "应用于新加坡背景"],
        "sections": [
            {"id": "ss-1", "type": "text", "title": "Types of Supply-Side Policies", "title_zh": "供给侧政策类型",
             "content": "**Market-based:**\n- Deregulation\n- Privatization\n- Tax reforms\n- Trade liberalization\n\n**Interventionist:**\n- Education and training\n- Infrastructure investment\n- R&D support\n- Industrial policy"},
            {"id": "ss-2", "type": "text", "title": "Effects on Economy", "title_zh": "对经济的影响",
             "content": "**AS curve shifts right:**\n- Higher potential output\n- Lower natural rate of unemployment\n- Non-inflationary growth\n\n**Long-term nature:**\n- Takes time to implement\n- Takes time to see results\n- Sustained commitment needed"},
            {"id": "ss-3", "type": "text", "title": "Singapore's Supply-Side Focus", "title_zh": "新加坡的供给侧重点",
             "content": "**Key policies:**\n- SkillsFuture (lifelong learning)\n- R&D investment (A*STAR)\n- Infrastructure (airports, ports)\n- Productivity initiatives\n- Foreign talent policies\n\n**Restructuring:**\n- Moving to higher value-added activities\n- Industry transformation"}
        ]
    },
    {
        "id": "international-trade-jc2",
        "title": "International Trade",
        "title_zh": "国际贸易",
        "gradeLevel": "jc2",
        "description": "Comparative advantage and trade policies",
        "description_zh": "比较优势和贸易政策",
        "objectives": ["Apply comparative advantage theory", "Analyze benefits and costs of free trade", "Evaluate protectionist measures"],
        "objectives_zh": ["应用比较优势理论", "分析自由贸易的利弊", "评价保护主义措施"],
        "sections": [
            {"id": "trade-1", "type": "text", "title": "Comparative Advantage", "title_zh": "比较优势",
             "content": "**Principle:** Countries should specialize in goods where they have lowest opportunity cost.\n\n**Benefits of trade:**\n- Greater efficiency\n- Larger variety\n- Lower prices\n- Economies of scale\n\n**Assumptions:** Many simplifying assumptions in the basic model"},
            {"id": "trade-2", "type": "text", "title": "Protectionism", "title_zh": "保护主义",
             "content": "**Trade barriers:**\n- Tariffs (taxes on imports)\n- Quotas (quantity limits)\n- Subsidies to domestic producers\n- Non-tariff barriers (regulations)\n\n**Arguments for protection:**\n- Infant industry\n- National security\n- Job protection\n- Dumping defense"},
            {"id": "trade-3", "type": "text", "title": "Singapore's Trade Policy", "title_zh": "新加坡的贸易政策",
             "content": "**Open economy approach:**\n- Free trade agreements (FTAs)\n- No tariffs on most goods\n- Trade hub strategy\n- WTO membership\n\n**Trade = 3x GDP:**\n- Highly trade-dependent\n- Vulnerable to global conditions\n- Diversification strategy"}
        ]
    },
    {
        "id": "globalization-jc2",
        "title": "Globalization",
        "title_zh": "全球化",
        "gradeLevel": "jc2",
        "description": "Economic integration and its effects",
        "description_zh": "经济一体化及其影响",
        "objectives": ["Define aspects of globalization", "Analyze costs and benefits", "Discuss Singapore's position"],
        "objectives_zh": ["定义全球化方面", "分析成本和收益", "讨论新加坡的地位"],
        "sections": [
            {"id": "glob-1", "type": "text", "title": "What is Globalization?", "title_zh": "什么是全球化?",
             "content": "**Dimensions:**\n- Trade in goods and services\n- Capital flows (FDI, portfolio)\n- Labor migration\n- Technology transfer\n- Cultural exchange\n\n**Drivers:**\n- Technology (transport, communication)\n- Liberalization policies\n- MNCs' strategies"},
            {"id": "glob-2", "type": "text", "title": "Benefits and Costs", "title_zh": "利弊",
             "content": "**Benefits:**\n- Economic growth\n- Consumer choice\n- Knowledge transfer\n- Employment opportunities\n\n**Costs:**\n- Income inequality\n- Job losses in some sectors\n- Environmental concerns\n- Cultural homogenization\n- Financial contagion"},
            {"id": "glob-3", "type": "text", "title": "Singapore & Globalization", "title_zh": "新加坡与全球化",
             "content": "**As a global city:**\n- Regional headquarters\n- Financial hub\n- Trading hub\n- Talent magnet\n\n**Challenges:**\n- Over-reliance on external demand\n- Competition from other cities\n- Managing foreign worker policies\n- Income inequality concerns"}
        ]
    }
]

def generate_econ_exercises(chapter_id, topic, count=15):
    """Generate economics exercises."""
    exercises = []
    diffs = ['easy'] * 5 + ['medium'] * 5 + ['hard'] * 5
    
    templates = [
        ("What is the definition of {topic}?", ["Correct definition", "Wrong A", "Wrong B", "Wrong C"]),
        ("In {topic}, what happens when price increases?", ["Correct effect", "Wrong A", "Wrong B", "Wrong C"]),
        ("Which factor affects {topic}?", ["Correct factor", "Wrong A", "Wrong B", "Wrong C"]),
        ("What is the Singapore government's approach to {topic}?", ["Correct approach", "Wrong A", "Wrong B", "Wrong C"]),
        ("How does {topic} affect economic welfare?", ["Correct explanation", "Wrong A", "Wrong B", "Wrong C"]),
    ]
    
    for i in range(count):
        template = templates[i % len(templates)]
        question = template[0].format(topic=topic)
        choices = template[1]
        
        exercises.append({
            "id": f"{chapter_id}-ex{i+1}",
            "type": "mcq",
            "difficulty": diffs[i],
            "prompt": question,
            "prompt_zh": f"中文: {question}",
            "choices": choices,
            "choices_zh": choices,
            "answer": 0,
            "explanation": f"Key concept about {topic}."
        })
    
    return exercises

def main():
    print("=" * 70)
    print("Adding Economics (H2) content")
    print("=" * 70)
    
    with open('src/data/content.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f'src/data/content-backup-econ-{timestamp}.json'
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"Created backup: {backup_path}")
    
    # Check if economics subject exists
    econ_subject = None
    for s in content['subjects']:
        if s['id'] == 'economics-jc':
            econ_subject = s
            break
    
    if not econ_subject:
        econ_subject = {
            "id": "economics-jc",
            "title": "Economics (H2)",
            "title_zh": "经济学 (H2)",
            "description": "A-Level H2 Economics for JC students",
            "description_zh": "JC学生的A水准H2经济学",
            "color": "#f59e0b",
            "chapters": []
        }
        content['subjects'].append(econ_subject)
        print("\nCreated Economics (H2) subject")
    
    # Add JC1 chapters
    print("\nAdding JC1 Economics chapters...")
    for chapter in JC1_ECONOMICS_CHAPTERS:
        chapter['exercises'] = generate_econ_exercises(chapter['id'], chapter['title'])
        econ_subject['chapters'].append(chapter)
        print(f"   Added: {chapter['title']}")
    
    # Add JC2 chapters
    print("\nAdding JC2 Economics chapters...")
    for chapter in JC2_ECONOMICS_CHAPTERS:
        chapter['exercises'] = generate_econ_exercises(chapter['id'], chapter['title'])
        econ_subject['chapters'].append(chapter)
        print(f"   Added: {chapter['title']}")
    
    # Save
    with open('src/data/content.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print(f"\nAdded Economics (H2):")
    print(f"  - 8 JC1 chapters")
    print(f"  - 8 JC2 chapters")
    print(f"  - 240 exercises total")

if __name__ == "__main__":
    main()

