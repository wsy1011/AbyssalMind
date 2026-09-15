"""One-time editorial corrections and registration of the first brief."""
from pathlib import Path
import json
import shutil
ROOT = Path(__file__).resolve().parents[1]
p = ROOT / 'content/articles/phased-fuel-transitions-for-asia-europe-corridor.md'
s = p.read_text(encoding='utf-8-sig')
s = s.replace('/D:/Code/AbyssalMind/assets/', '../../assets/')
s = s.replace('近期开启转型时，生物燃料和部分 LNG 路线呈现较平衡的减排与成本组合，但受到原料规模、甲烷泄漏和可持续性约束。','论文摘要给出的分阶段结果是：大豆基生物柴油可作为近期方案，电制燃料在模型中于 2040 年后占据重要地位。这是情景结论，不是统一换燃料的时间表。生物 LNG 与传统 LNG 也必须区分：前者有减排潜力，后者在当前生产条件下可能因甲烷泄漏而具有更高的生命周期排放。')
s = s.replace('可再生电力会显著改善 e-LNG、e-LH₂ 和 e-LNH₃ 的生命周期表现','可再生电力会显著改善多种电制燃料的生命周期表现')
s = s.replace('亚欧绿色航运走廊同时受到全球 IMO 规则和欧盟 FuelEU Maritime 的影响。','论文将亚欧绿色航运走廊置于 IMO 净零框架与 FuelEU Maritime 的潜在双重约束下。作者明确指出 IMO 框架的正式通过曾被推迟，因此下文所述 IMO 路径均指论文模拟设置，不是对当前已生效规则的核验。')
s = s.replace('研究覆盖 1,300 个情景，并比较 IMO Net-Zero Framework、FuelEU Maritime 以及两项规则叠加的情景。','作者在主文报告总体评估覆盖 1,300 个情景；图 1 图注对应的是 324 个独立确定性 LCA 情景，不能将这两个数量混作统计样本量。研究还区分两组比较维度：一组是 IMO、FuelEU 及二者叠加的政策设置；另一组是 BAU（维持 HFO 的基准）、ME（经济性与合规平衡）及 MCR（最大减碳）策略。')
s = s.replace('## Figure 1｜','功能单位以每吨货物运输一海里计，采用从原料获取、生产、储运到船上燃烧的 well-to-wake 边界。生命周期评估使用 GaBi 9.2.1，系统动力学使用 Vensim PLE 10.4.0。主文还报告 Monte Carlo 和敏感性分析；本稿未独立复算模型，也未审计补充材料全部参数。\n\n## Figure 1｜',1)
s = s.replace('**图 1 解读。**','**原图定位：** PDF 第 3 页／期刊第 1258 页，图 1a–d。箱体表示情景分布，彩色点区分 2024 年基准与 2050 年政策投影。它们不是船队实测样本的置信区间。\n\n**图 1 解读。**')
s = s.replace('**图 2 解读。**','**原图定位：** PDF 第 4 页／期刊第 1259 页，图 2。地图依据论文引用的能源与基础设施资料，不能当作今天的实时加注港口清单。\n\n**图 2 解读。**')
s = s.replace('东亚拥有较大的可再生发电装机规模，西欧的可再生电力占比更高；','圆环中的东亚 1,630 GW 是总装机，39.8% 是图示可再生装机比例，对应约 649 GW；西欧的图示比例为 53.8%。装机比例不等于实际发电量占比；')
s = s.replace('**图 3 解读。**','**原图定位：** PDF 第 5 页／期刊第 1260 页，图 3a–d。灰色柱为欧盟当前混合电力情景，彩色柱为风、光、水电三个独立模拟的均值，误差线表示最小—最大值，并非抽样误差。\n\n**图 3 解读。**')
s = s.replace('论文同时提醒，e-MeOH 仍可能受到合成过程中的 N₂O 和 CH₄ 排放影响。','上述百分比是生命周期能耗降幅，不是燃料价格或 GHG 减排百分比。图 3a 的 GHG 与图 3b 的碳强度口径不同：e-MeOH 在 b 中很低，不能推出它在 a 中也接近零。作者将其剩余 GHG 负担联系到合成过程中的 N₂O 和 CH₄ 排放。')
s = s.replace('**图 4 解读。**','**原图定位：** PDF 第 6 页／期刊第 1261 页，图 4a–f。纵轴为模拟年排放量（百万吨 CO₂e），对应以各区域港口为起终点的往返航行案例，并非六个国家或地区的全部航运排放。\n\n**图 4 解读。**')
s = s.replace('两套规则叠加时，合规成本会进一步改变船东对电制氢和电制氨路线的判断。','读图时应关注 ME 与 MCR 的距离和随时间的变化：例如中国与欧盟在 FuelEU 单独情景下，两条路径一度明显分离；在论文的 IMO 及叠加情景中，它们更接近。这不是“罚金越高，减排必然越多”的简单关系。')
s = s.replace('**图 5 解读。**','**原图定位：** PDF 第 7 页／期刊第 1262 页，图 5。A 表示 FuelEU 单独情景，B 表示两项政策叠加；A1/B1 为掺混，A2/B2 为改造，A3–A5/B3–B5 为新建双燃料方案。柱状图纵轴为 kg CO₂e/MJ，不能直接与图 4 的年排放量相比较；右侧径向图是 2050 年相对 HFO 的燃料使用成本倍数。\n\n**图 5 解读。**')
s = s.replace('## 对行业的含义','## 对行业的含义（Abyssal Mind 解读）')
s = s.replace('这是一项情景研究，不是对未来燃料价格或船队采用率的确定性预测。','这是一项情景研究，不是对未来燃料价格或船队采用率的确定性预测。主文明确列出以下边界：\n\n- 固定往返航线，并假设整个航程使用一致燃料混合比例，未模拟途中灵活采购与换燃料。\n- bio-LNG 的供给弹性被设为高于其他生物燃料，这会影响其扩张优势。\n- IMO 2040 年后的目标采用外部来源延伸；零碳燃料奖励机制未纳入。\n- EU ETS 未被显式建模，作者用 FuelEU 罚金代表更广泛的欧盟政策经济激励，因此模型合规成本不能直接用于企业账单。\n- 船舶经营者行为反应、未来监管变化及宏观冲击未被纳入。\n\n')
s = s.replace('图 1—5 为基于 Zotero PDF Figure 工作流从论文 PDF 页面提取的图版裁切，图注和解释依据论文原文。原始 PDF 保存在 `assets/articles/phased-fuel-transitions/source.pdf`。','论文在线发表于 2026 年 8 月 18 日。作者公开的数据入口：[Zenodo 数据集](https://doi.org/10.5281/zenodo.19872982)。\n\n图 1—5 来自 Zotero PDF Figure 对附件 NKT67I83 生成的完整图版缓存；本文直接复制插件 PNG，未重绘、修改数据或裁去面板与图例。来源记录与 SHA-256 校验值见 `assets/articles/phased-fuel-transitions/provenance.json`（项目根目录下）。\n\n原图版权 © The Author(s) 2026，依 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) 标注来源。图下的中文说明为 Abyssal Mind 独立解读，非原图注的逐字译文。本文为本地研究解读草稿；复用原图须遵守非商业、禁止演绎条件。')
p.write_text(s,encoding='utf-8')
# Keep trial extractions and source PDF outside the published assets, without deleting them.
assets = ROOT/'assets/articles/phased-fuel-transitions'
archive = ROOT/'.local/research/phased-fuel-transitions'
archive.mkdir(parents=True,exist_ok=True)
for f in assets.iterdir():
    if f.name.startswith('page-') or (f.name.startswith('figure-0')) or f.name=='source.pdf':
        dest=archive/f.name
        assert not dest.exists(), dest
        shutil.move(str(f),str(dest))
fulltext=ROOT/'content/article-briefs/phased-fuel-transitions-fulltext.txt'
if fulltext.exists(): shutil.move(str(fulltext),str(archive/fulltext.name))
ignore=ROOT/'.gitignore'
old=ignore.read_text(encoding='utf-8') if ignore.exists() else ''
if '.local/' not in old: ignore.write_text(old+'\n.local/\n',encoding='utf-8')
catalog=ROOT/'content/articles.json'
data=json.loads(catalog.read_text(encoding='utf-8-sig'))
slug='phased-fuel-transitions-for-asia-europe-corridor'
data['articles']=[a for a in data['articles'] if a['id']!=slug]
data['articles'].append({'id':slug,'type':'research','status':'draft','title':'分阶段燃料转型：亚欧绿色航运走廊如何走向脱碳？','dek':'结合论文五张原图，理解清洁电力、政策组合与船舶技术如何共同塑造燃料转型路径。','language':'zh-CN','publishedAt':None,'updatedAt':'2026-09-15','author':'Abyssal Mind','domains':['shipping','energy','transport','economy','policy'],'topics':['green-shipping-corridors'],'regions':['Asia','Europe'],'tags':['alternative-fuels','life-cycle-assessment','system-dynamics'],'source':{'title':'Phased fuel transitions for decarbonizing the Asia–Europe Green Shipping Corridor','url':'https://doi.org/10.1038/s41893-026-01878-9','kind':'paper','doi':'10.1038/s41893-026-01878-9','zoteroItemKey':'XVQJF47V','publishedAt':'2026-08-18'},'image':{'src':'assets/articles/phased-fuel-transitions/figure-2.png','alt':'论文图2：亚欧走廊加注港口与可再生装机分布','credit':'Li et al. (2026), CC BY-NC-ND 4.0'},'readingTime':12,'featured':False,'body':f'articles/{slug}.md','preview':f'articles/{slug}.html'})
catalog.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
